from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.mcp_schema import (
    ExchangeRateArgs, ExchangeRateResult,
    SendEmailArgs, SendEmailResult,
    CalendarEventArgs, CalendarEventResult
)
from app.utils import fetch_rate
from app.emailer import send_mail_sync
from app.llm_client import call_llm
import uuid

app = FastAPI(title='MCP Business Tools')

# In-memory store for calendar events
EVENTS = {}

# ====== MCP Tools ======

@app.post('/tool/get_exchange_rate')
async def get_exchange_rate(payload: ExchangeRateArgs):
    try:
        rate, raw = await fetch_rate(payload.from_currency, payload.to_currency)
        if rate is None:
            raise HTTPException(status_code=502, detail='no rate returned')
        result = ExchangeRateResult(rate=rate, base=payload.from_currency, target=payload.to_currency)
        return {
            'success': True,
            'result': result.dict(),
            'raw': raw
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={'success': False, 'error': str(e)})

@app.post('/tool/send_email')
def send_email(payload: SendEmailArgs):
    try:
        msg_id = send_mail_sync(payload.to, payload.subject, payload.body)
        res = SendEmailResult(message_id=msg_id, status='sent')
        return {'success': True, 'result': res.dict()}
    except Exception as e:
        return JSONResponse(status_code=500, content={'success': False, 'error': str(e)})

@app.post('/tool/create_calendar_event')
async def create_calendar_event(payload: CalendarEventArgs):
    try:
        event_id = str(uuid.uuid4())
        ev = {
            'event_id': event_id,
            'title': payload.title,
            'start_iso': payload.start_iso,
            'end_iso': payload.end_iso,
            'description': payload.description
        }
        EVENTS[event_id] = ev
        res = CalendarEventResult(**ev)
        return {'success': True, 'result': res.dict()}
    except Exception as e:
        return JSONResponse(status_code=500, content={'success': False, 'error': str(e)})

# ====== LLM Test Generation ======

class GenManualReq(BaseModel):
    product_description: str
    owner: str
    feature: str
    count: int = 5

@app.post('/generate/manual-tests')
async def gen_manual(req: GenManualReq):
    try:
        # Пример вызова LLM (нужен токен в .env)
        prompt = f"Generate {req.count} test cases for product '{req.product_description}' with feature '{req.feature}'"
        llm_res = await call_llm(prompt)

        # Здесь упрощённо: возвращаем LLM ответ как список тестов
        tests = [{'title': f"{req.feature} test #{i+1}", 'content': llm_res.get('output', '')} for i in range(req.count)]
        return {'success': True, 'tests': tests}
    except RuntimeError as e:
        # Если нет токена, LLM не будет вызван
        return JSONResponse(status_code=400, content={'success': False, 'error': str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={'success': False, 'error': str(e)})

# ====== Health ======

@app.get('/health')
async def health():
    return {'status': 'ok'}
