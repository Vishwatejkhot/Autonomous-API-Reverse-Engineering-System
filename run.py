import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

from src.core.orchestrator import Orchestrator
from src.watcher.folder_watcher import start_auto_update

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat(model, system, user, temperature=0.2):
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role":"system","content":system},
            {"role":"user","content":user}
        ],
        temperature=temperature
    )
    return resp.choices[0].message.content.strip()

FAST = "llama-3.1-8b-instant"
DEEP = "llama-3.3-70b-versatile"

embed_model = SentenceTransformer("BAAI/bge-small-en-v1.5")

if __name__ == "__main__":
    orchestrator = Orchestrator(chat, embed_model, FAST, DEEP)

    orchestrator.run()

    start_auto_update(orchestrator)
