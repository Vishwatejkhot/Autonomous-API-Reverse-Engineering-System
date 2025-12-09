# 🔥 Autonomous API Reverse Engineer  
### Auto-Generate Documentation • OpenAPI Specs • SDKs • Tests from Raw API Samples  
Built with Groq LLaMA-3, Sentence Transformers, FAISS & Watchdog

---

## 📌 Overview  

This project is a **fully autonomous multi-agent AI system** that can reverse-engineer any API from raw text samples (curl requests, responses, logs, Postman dumps).

It performs:

✔ Vector-based retrieval  
✔ Evidence extraction  
✔ API structure reconstruction  
✔ Documentation generation  
✔ OpenAPI generation  
✔ SDK code generation  
✔ Test code generation  
✔ Automatic updates when new files are added  

It is designed to run **continuously**, watching the `api_samples/` folder.  
Whenever a new `.txt` file is added or edited, the system automatically regenerates:

- `api_docs.md`  
- `openapi.yaml`  
- `sdk.py`  
- `tests_sdk.py`  

---

## 🧠 Features

### 🔍 1. Intelligent Retrieval  
Uses **BGE embeddings + FAISS** to retrieve the most relevant API samples.

### 📑 2. Evidence Extraction Agent  
Powered by **Groq LLaMA 3 models**  
Extracts ONLY factual API information:

- Endpoints  
- Methods  
- Path/query/body params  
- Response fields  
- Auth rules  

### 🧩 3. Analysis Agent  
Understands:

- API purpose  
- Resources  
- Relationships  
- Auth/security patterns  

### 🛠 4. Codegen Agent  
Generates 4 clean multi-line blocks:

```
<markdown> ... </markdown>
<openapi> ... </openapi>
<sdk> ... </sdk>
<tests> ... </tests>
```

Each block is saved into separate files.

### 👀 5. Auto-Update Watcher  
A background file watcher detects changes in `api_samples/` and **re-runs the entire pipeline** automatically.

---

## 📂 Project Structure

```
api-reverse-engineer/
│
├── src/
│   ├── agents/
│   │   ├── evidence_agent.py
│   │   ├── analysis_agent.py
│   │   ├── codegen_agent.py
│   │
│   ├── embeddings/
│   │   ├── vector_store.py
│   │
│   ├── watcher/
│   │   ├── folder_watcher.py
│   │
│   ├── core/
│   │   ├── orchestrator.py
│   │
├── api_samples/
├── outputs/
├── run.py
├── README.md
└── .env
```

---

## 🚀 Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourname/api-reverse-engineer.git
cd api-reverse-engineer
```

### 2. Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate    # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key to `.env`
```
GROQ_API_KEY=your_key_here
```

---

## ▶️ Usage

### Start the system:
```bash
python run.py
```

You will see:

```
📥 Loading API samples...
🧠 Building FAISS vector index...
🔍 Searching relevant samples...
✅ Outputs generated!
👀 Watching api_samples/ for changes...
```

### Now add any `.txt` file into `api_samples/`

Example:
```
POST_users_create.txt
```

The system will automatically:

- Rebuild embeddings  
- Re-extract evidence  
- Re-analyze the API  
- Regenerate docs  
- Regenerate OpenAPI  
- Regenerate SDK  
- Regenerate tests  

---

## 🛑 Stopping the System

Press:
```
CTRL + C
```

To restart automation:
```
python run.py
```

---

## 🎯 Why This Project Is Impressive

This project demonstrates:

- Real multi-agent AI workflow  
- Automated developer tooling  
- Production-level embeddings + FAISS usage  
- LLL-powered code generation  
- Real-time automation with a watcher  
- End‑to‑end system orchestration  

This is the SAME architecture used by:
- GitHub Copilot  
- Microsoft AutoDev tools  
- OpenAI Agents  
- AWS Bedrock coding workflows  



---

## 📬 Contact  
For issues or improvements, feel free to open a PR or raise an issue!

Happy building 🚀
