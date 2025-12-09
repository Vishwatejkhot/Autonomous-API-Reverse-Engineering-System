import os
import glob
from dataclasses import dataclass

from src.agents.evidence_agent import EvidenceAgent
from src.agents.analysis_agent import AnalysisAgent
from src.agents.codegen_agent import CodegenAgent
from src.embeddings.vector_store import VectorStore

@dataclass
class APISample:
    filename: str
    text: str

class Orchestrator:
    def __init__(self, chat_func, embed_model, fast_model, deep_model):
        self.chat = chat_func
        self.embed_model = embed_model
        self.fast_model = fast_model
        self.deep_model = deep_model

        self.vector_store = VectorStore(embed_model)

        self.evidence_agent = EvidenceAgent(chat_func, fast_model)
        self.analysis_agent = AnalysisAgent(chat_func, fast_model)
        self.codegen_agent = CodegenAgent(chat_func, deep_model)

    def load_samples(self):
        samples = []
        for path in glob.glob("api_samples/*.txt"):
            with open(path, "r") as f:
                samples.append(APISample(os.path.basename(path), f.read()))
        return samples

    def run(self):
        print("📥 Loading API samples...")
        samples = self.load_samples()

        texts = [s.text for s in samples]

        if not self.vector_store.load():
            print("🧠 Building FAISS vector index...")
            self.vector_store.build(texts)

        print("🔍 Searching relevant samples...")
        scores, idx = self.vector_store.search("Reverse engineer this API")

        retrieved = [(samples[i], scores[j]) for j, i in enumerate(idx)]

        evidence = self.evidence_agent.extract("Reverse engineer this API", retrieved)
        analysis = self.analysis_agent.analyze(evidence)
        outputs = self.codegen_agent.generate(evidence, analysis)

        os.makedirs("outputs", exist_ok=True)

        with open("outputs/api_docs.md", "w") as f: f.write(outputs.get("markdown_docs",""))
        with open("outputs/openapi.yaml", "w") as f: f.write(outputs.get("openapi_yaml",""))
        with open("outputs/sdk.py", "w") as f: f.write(outputs.get("python_sdk",""))
        with open("outputs/tests_sdk.py", "w") as f: f.write(outputs.get("pytest_tests",""))

        print("✅ Outputs generated!")
