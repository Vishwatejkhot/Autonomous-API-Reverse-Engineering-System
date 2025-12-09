import re
import json

class EvidenceAgent:
    def __init__(self, chat_func, model):
        self.chat = chat_func
        self.model = model

    def extract(self, question, samples):
        context = ""
        for i, (sample, score) in enumerate(samples, start=1):
            context += f"### SAMPLE {i} (score={score:.3f})\n{sample.text}\n\n"

        system = (
            "You are an Evidence Extraction Agent for APIs.\n"
            "Extract factual API structure ONLY.\n"
            "Return JSON strictly following the schema."
        )

        user = f"Question: {question}\n\nAPI Samples:\n{context}"

        raw = self.chat(self.model, system, user)
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        return match.group(0) if match else raw
