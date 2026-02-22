# LangChainLLM

Implementation of an **LLM Chain** with LangChain using `llama-3.3-70b-versatile` through **Groq** (100% free, no credit card required).  
Based on the official [LangChain LLM Chain Tutorial](https://python.langchain.com/docs/tutorials/llm_chain).

---

## Why Groq?

| | Gemini free | OpenAI | Groq free |
|---|---|---|---|
| Requests/day | ~50 | Paid | 14,400 |
| Requests/minute | 2 | Paid | 30 |
| Credit card required | No | Yes | No |
| Speed | Medium | High | ⚡ Very high |

---

## Architecture

```
User input (topic)
        │
        ▼
┌─────────────────────┐
│  ChatPromptTemplate  │  ← Sets assistant persona + {topic} variable
└─────────────────────┘
        │
        ▼
┌──────────────────────────────┐
│  ChatGroq                    │  ← llama-3.3-70b-versatile (free)
│  (llama-3.3-70b-versatile)   │
└──────────────────────────────┘
        │
        ▼
┌─────────────────────┐
│   StrOutputParser    │  ← Converts AIMessage to plain string
└─────────────────────┘
        │
        ▼
   Text response
```

### Components

| Component | Role |
|---|---|
| `ChatPromptTemplate` | Structures the conversation: system persona + user message with `{topic}` placeholder |
| `ChatGroq` | Calls the Groq API with the LLaMA 3.3 70B model |
| `StrOutputParser` | Converts the `AIMessage` object to a plain Python string |
| LCEL pipe (`\|`) | Composes the three components into a single executable chain |

---

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/langchain-llm-chain.git
cd langchain-llm-chain

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Open .env and paste your Groq API key
```

---

## Running the code

```bash
python main.py
```

### Expected output

```
📌 Topic: Retrieval-Augmented Generation (RAG)
--------------------------------------------------
RAG is a technique that combines an information retrieval system with a
generative language model to produce more accurate and contextually relevant
responses. Instead of relying solely on the model's internal knowledge, RAG
fetches relevant documents from an external knowledge base and uses them as
additional context for the generator...

📌 Topic: Vector databases and embeddings
--------------------------------------------------
...

🌊 Streaming example:
--------------------------------------------------
Transformers revolutionized NLP by introducing an architecture that allows
parallel processing of text sequences...
```

---

## Key concepts

**LCEL (LangChain Expression Language)** — the `|` pipe operator composes runnables left-to-right, similar to Unix pipes. Each component implements `.invoke()`, `.stream()`, and `.batch()`.

**Prompt templates** — separate the prompt structure from variable values, making prompts reusable, testable, and easy to version-control.

**Streaming** — `chain.stream()` yields partial tokens as they arrive from the API, enabling responsive UIs without waiting for the full response.

---

## Project structure

```
repo1/
├── main.py           # Main script with the LLM chain
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variable template
├── .gitignore        # Files excluded from git
└── README.md         # This file
```
