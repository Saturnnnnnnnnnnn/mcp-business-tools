
import os
import httpx

TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))

async def fetch_rate(from_cur: str, to_cur: str):
    url = f"https://api.exchangerate.host/convert?from={from_cur}&to={to_cur}"
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.get(url)
        r.raise_for_status()
        data = r.json()
        return data.get('info', {}).get('rate'), data
