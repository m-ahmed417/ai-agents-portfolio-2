import os
import json

from openai import OpenAI

from src.prompt_loader import load_prompt
from src.providers.base import BaseTriageProvider
from src.schemas import TicketRoute
from dotenv import load_dotenv


class DeepSeekProvider(BaseTriageProvider):
    def __init__(self):
        load_dotenv()
        api_key = os.getenv("DEEPSEEK_API_KEY")
        
        if not api_key:
            raise ValueError("Missing DEEPSEEK_API_KEY environment variable")
        
        self.api_key = api_key
        self.model = "deepseek-v4-pro"
        self.system_prompt = load_prompt("prompts/route_ticket_system.md")
        self.base_url = "https://api.deepseek.com"
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url,
        )
        
    
    def route_ticket(self, message: str) -> TicketRoute:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"Here is the customer message: {message}"},
            ],
            response_format={"type": "json_object"},
            stream=False,
            temperature=0,
        )

        content = response.choices[0].message.content
        data = json.loads(content)
        return TicketRoute.model_validate(data)
