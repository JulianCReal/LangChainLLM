"""
Repo 1 — LangChain LLM Chain con Groq (llama-3.3-70b-versatile)
Based on: https://python.langchain.com/docs/tutorials/llm_chain
"""

import os
import sys
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ── 1. Cargar variables de entorno ────────────────────────────────────────────
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise EnvironmentError("Falta GROQ_API_KEY en el archivo .env")

# ── 2. Inicializar el modelo ──────────────────────────────────────────────────
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=GROQ_API_KEY,
)

# ── 3. Definir el prompt template ─────────────────────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that explains technical topics clearly and concisely."),
    ("user",   "Explain the following topic in 3-4 sentences: {topic}"),
])

# ── 4. Construir la cadena ────────────────────────────────────────────────────
chain = prompt | model | StrOutputParser()

# ── 5. Función para hacer preguntas con streaming ─────────────────────────────
def ask(topic: str) -> None:
    """Invoca la cadena con streaming e imprime la respuesta token a token."""
    print(f"\n📌 Topic: {topic}")
    print("-" * 50)
    for chunk in chain.stream({"topic": topic}):
        print(chunk, end="", flush=True)
    print("\n")


# ── 6. Modo interactivo ───────────────────────────────────────────────────────
def interactive_mode() -> None:
    """Loop que lee temas desde la terminal hasta que el usuario escribe 'exit'."""
    print("🤖 LangChain LLM Chain — Groq Edition")
    print("   Type a topic and press Enter. Type 'exit' to quit.\n")

    while True:
        try:
            topic = input("📝 Enter a topic: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye!")
            break

        if not topic:
            print("   ⚠️  Please enter a topic.\n")
            continue

        if topic.lower() in ("exit", "quit", "q"):
            print("👋 Goodbye!")
            break

        ask(topic)


# ── 7. Entry point ────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Modo CLI: python main.py "your topic here"
        ask(" ".join(sys.argv[1:]))
    else:
        # Modo interactivo: python main.py
        interactive_mode()