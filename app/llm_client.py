import os
import httpx
from typing import Dict, Any

LLM_API = os.getenv('EVOLUTION_API_URL', 'https://foundation-models.api.cloud.ru/v1')
LLM_TOKEN = os.getenv('EVOLUTION_API_TOKEN')
TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))

async def call_llm(prompt: str, max_tokens: int = 2000) -> Dict[str, Any]:
    if not LLM_TOKEN:
        raise RuntimeError('EVOLUTION_API_TOKEN not set in .env')
    
    url = f"{LLM_API}/generate"
    headers = {
        'Authorization': f'Bearer {LLM_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': 'evo-1',
        'input': prompt,
        'max_tokens': max_tokens
    }
    
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.post(url, headers=headers, json=payload)
        r.raise_for_status()
        return r.json()
