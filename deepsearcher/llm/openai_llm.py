from typing import Dict, List
from deepsearcher.llm.base import BaseLLM, ChatResponse
import os


class OpenAI(BaseLLM):
    def __init__(self, model: str = "gpt-4o"):
        from openai import OpenAI as OpenAI_
        self.model = model
        self.client = OpenAI_(base_url=os.getenv("OPENAI_API_BASE","https://api.openai.com/v1/"))


    def chat(self, messages: List[Dict]) -> ChatResponse:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return ChatResponse(content=completion.choices[0].message.content, total_tokens=completion.usage.total_tokens)

