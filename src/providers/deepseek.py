from src.providers.base import BaseTriageProvider
import os
from src.schemas import TicketRoute
import json
from src.prompt_loader import load_prompt
from openai import OpenAI


class DeepSeekProvider(BaseTriageProvider):
    def __init__(self):
        api_key = os.getenv("DEEPSEEK_API_KEY")
        
        if not api_key:
            raise ValueError("Missing DEEPSEEK_API_KEY environment variable")
        
        self.api_key = api_key
        self.model = "deepseek-v4-pro"
        self.system_prompt = load_prompt("prompts/route_ticket_system.md")
        self.base_url = "https://api.deepseek.com"
    
    def route_ticket(self, message: str) -> TicketRoute:
        client = OpenAI(
        api_key=self.api_key,
        base_url=self.base_url)
        
        response = client.chat.completions.create(
        model=self.model,
        messages=[
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": f"Here is the customer message: {message}"},
        ],
        response_format={"type": "json_object"},
        stream=False,
        temperature=0
        )
        
        content = response.choices[0].message.content
        data = json.loads(content)
        return TicketRoute.model_validate(data)