"""
Repo 1 — LangChain LLM Chain con Groq (llama-3.3-70b-versatile)
Based on: https://python.langchain.com/docs/tutorials/llm_chain
"""

import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Cargar variables de entorno 
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise EnvironmentError("Falta GROQ_API_KEY en el archivo .env")

# 2. Inicializar el modelo 
# llama-3.3-70b-versatile: rápido, gratuito, muy capaz
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    groq_api_key=GROQ_API_KEY,
)

# 3. Definir el prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil que explica temas técnicos de forma clara y concisa."),
    ("user",   "Explica el siguiente tema en 3-4 oraciones: {topic}"),
])

# 4. Construir la cadena con el operador pipe
# prompt → model → output parser
chain = prompt | model | StrOutputParser()

# 5. Función para hacer preguntas
def ask(topic: str) -> str:
    """Invoca la cadena y retorna la respuesta."""
    print(f"\n📌 Tema: {topic}")
    print("-" * 50)
    response = chain.invoke({"topic": topic})
    print(response)
    return response


# 6. Preguntas de ejemplo
if __name__ == "__main__":
    topics = [
        "Retrieval-Augmented Generation (RAG)",
        "Bases de datos vectoriales y embeddings",
        "Cómo LangChain simplifica el desarrollo de aplicaciones con LLMs",
    ]

    for t in topics:
        ask(t)

    # 7. Ejemplo con streaming
    print("\n\n🌊 Ejemplo con streaming:")
    print("-" * 50)
    for chunk in chain.stream({"topic": "Por qué los transformers cambiaron el NLP"}):
        print(chunk, end="", flush=True)
    print()