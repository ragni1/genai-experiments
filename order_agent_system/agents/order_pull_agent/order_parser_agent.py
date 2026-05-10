from langchain_community.llms import Ollama
from agents.order_pull_agent.prompt import load_prompt
import json
import subprocess

class OrderParserAgent:
    def __init__(self, model_name="llama3.2:3b"):
        try:
            subprocess.run(
                ["ollama", "pull", model_name],
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8" 
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Failed to pull Ollama model {self.model_name}: {e.stderr}"
            )
        # Initialize Ollama LLM
        self.llm = Ollama(model=model_name)
        # Load prompt at initialization
        self.prompt = load_prompt()

    def parse(self, text:str):
        # Combine prompt and text
        full_prompt = f"{self.prompt}\n\nInput:\n{text}\n\nOutput:"
        
        # Call Ollama model
        # response = self.llm.invoke(full_prompt)
        response = self.llm.invoke(full_prompt)

        # Try to parse JSON from response
        try:
            self.parsed = json.loads(response)
            return self.parsed
        except Exception:
            return []

    def to_order_details(self):
        if not self.parsed:
            return []
        return [OrderDetail(o["item_name"], o["item_number"]) for o in self.parsed.values()]  


class OrderDetail:
    def __init__(self, item_name, item_number):
        self._item_name = item_name
        self._item_unit = item_number

    @property
    def item_name(self):
        return self._item_name

    @property
    def item_unit(self):
        return self._item_unit

    def to_dict(self):
        return {"item_name": self.item_name, "item_number": self.item_unit}
