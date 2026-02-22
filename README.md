# LangChainLLM

Implementación de un **LLM Chain** con LangChain usando `llama-3.3-70b-versatile` a través de **Groq** (100% gratuito, sin tarjeta de crédito).  
Basado en el tutorial oficial [LangChain LLM Chain Tutorial](https://python.langchain.com/docs/tutorials/llm_chain).

---

## ¿Por qué Groq?

| | Gemini free | OpenAI | Groq free |
|---|---|---|---|
| Requests/día | ~50 | De pago | 14,400 |
| Requests/minuto | 2 | De pago | 30 |
| Tarjeta requerida | No | Sí | No |
| Velocidad | Media | Alta | ⚡ Muy alta |

---

## Arquitectura

```
Input del usuario (topic)
        │
        ▼
┌─────────────────────┐
│  ChatPromptTemplate  │  ← Define el rol del asistente + variable {topic}
└─────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│  ChatGroq                    │  ← llama-3.3-70b-versatile (gratis)
│  (llama-3.3-70b-versatile)   │
└──────────────────────────────┘
        │
        ▼
┌─────────────────────┐
│   StrOutputParser    │  ← Convierte AIMessage a string plano
└─────────────────────┘
        │
        ▼
   Respuesta en texto
```

### Componentes

| Componente | Rol |
|---|---|
| `ChatPromptTemplate` | Estructura la conversación: persona del sistema + mensaje de usuario con `{topic}` |
| `ChatGroq` | Llama a la API de Groq con el modelo LLaMA 3.3 70B |
| `StrOutputParser` | Convierte el objeto `AIMessage` a un string de Python |
| Pipe LCEL (`\|`) | Compone los tres componentes en una cadena ejecutable |

---

## Requisitos previos

- Python 3.10+
- Una [Groq API key](https://console.groq.com) (gratis, sin tarjeta)

### Cómo obtener la API key de Groq
1. Ve a [console.groq.com](https://console.groq.com)
2. Crea una cuenta con tu correo
3. Ve a **API Keys** → **Create API Key**
4. Copia la key — empieza con `gsk_...`

---

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/<tu-usuario>/langchain-llm-chain.git
cd langchain-llm-chain

# 2. Crea y activa un entorno virtual
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. Configura las variables de entorno
cp .env.example .env
# Abre .env y pega tu Groq API key
```

---

## Ejecución

```bash
python main.py
```

### Output esperado

```
📌 Tema: Retrieval-Augmented Generation (RAG)
--------------------------------------------------
RAG es una técnica que combina un sistema de recuperación de información con un
modelo generativo de lenguaje para producir respuestas más precisas y
contextualmente relevantes. En lugar de depender únicamente del conocimiento
interno del modelo, RAG busca documentos relevantes en una base de conocimiento
externa y los usa como contexto adicional para el generador...

📌 Tema: Bases de datos vectoriales y embeddings
--------------------------------------------------
...

🌊 Ejemplo con streaming:
--------------------------------------------------
Los transformers revolucionaron el NLP al introducir el mecanismo de atención...
```

---

## Conceptos clave

**LCEL (LangChain Expression Language)** — el operador `|` compone runnables de izquierda a derecha. Cada componente implementa `.invoke()`, `.stream()` y `.batch()`.

**Prompt templates** — separan la estructura del prompt de los valores variables, haciéndolos reutilizables y fáciles de versionar.

**Streaming** — `chain.stream()` devuelve tokens parciales a medida que llegan, útil para UIs responsivas.

---

## Estructura del proyecto

```
repo1/
├── main.py           # Script principal con el LLM chain
├── requirements.txt  # Dependencias de Python
├── .env.example      # Plantilla de variables de entorno
└── README.md         # Este archivo
```