class AnalysisAgent:
    def __init__(self, chat_func, model):
        self.chat = chat_func
        self.model = model

    def analyze(self, evidence_json):
        system = (
            "You are an API analysis agent.\n"
            "Summarize purpose, resources, relationships, and auth."
        )

        user = f"Evidence:\n{evidence_json}"
        return self.chat(self.model, system, user)
