import re

class CodegenAgent:
    """
    Codegen Agent that generates 4 outputs in clean multi-line blocks:
        <markdown> ... </markdown>
        <openapi> ... </openapi>
        <sdk> ... </sdk>
        <tests> ... </tests>

    This avoids JSON escaping issues and produces readable files.
    """
    def __init__(self, chat_func, model):
        self.chat = chat_func       # LLM caller function
        self.model = model          # The deep model (70B)

    def _extract_block(self, raw, tag):
        """
        Extracts any block of the form:
            <tag>
            ...
            </tag>
        """
        pattern = fr"<{tag}>([\s\S]*?)</{tag}>"
        match = re.search(pattern, raw)
        if match:
            return match.group(1).strip()
        else:
            print(f"⚠️ WARNING: Missing <{tag}> block.")
            return ""

    def generate(self, evidence_json, analysis):
        """
        Generates documentation, OpenAPI spec, SDK code,
        and test code in separate multi-line blocks.
        """

        # Strict format instructions
        system = (
            "You are a senior backend engineer.\n"
            "Your output MUST consist ONLY of these 4 blocks:\n\n"
            "<markdown>\n"
            "... full markdown documentation ...\n"
            "</markdown>\n\n"
            "<openapi>\n"
            "... full OpenAPI YAML specification ...\n"
            "</openapi>\n\n"
            "<sdk>\n"
            "... full Python SDK code ...\n"
            "</sdk>\n\n"
            "<tests>\n"
            "... full pytest test code ...\n"
            "</tests>\n\n"
            "RULES:\n"
            "- DO NOT wrap output in JSON.\n"
            "- DO NOT escape newlines.\n"
            "- DO NOT include any explanation outside blocks.\n"
            "- Each block must contain valid content, not placeholders.\n"
        )

        user = f"""
Here is the extracted API structure and the analysis.

Evidence JSON:
{evidence_json}

Analysis:
{analysis}

Generate all 4 blocks now using the exact tags.
"""

        # Call the model
        raw = self.chat(self.model, system, user, temperature=0.1)

        # Extract each block
        markdown = self._extract_block(raw, "markdown")
        openapi = self._extract_block(raw, "openapi")
        sdk = self._extract_block(raw, "sdk")
        tests = self._extract_block(raw, "tests")

        # Return clean dict of outputs
        return {
            "markdown_docs": markdown,
            "openapi_yaml": openapi,
            "python_sdk": sdk,
            "pytest_tests": tests,
        }
