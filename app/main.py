
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.mcp_schema import (ExchangeRateArgs, ExchangeRateResult,
                            SendEmailArgs, SendEmailResult,
                            CalendarEventArgs, CalendarEventResult)
from app.utils import fetch_rate
from app.emailer import send_mail_sync
import uuid

app = FastAPI(title='MCP Business Tools')

EVENTS = {}

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
        ev = {'event_id': event_id, 'title': payload.title, 'start_iso': payload.start_iso, 'end_iso': payload.end_iso, 'description': payload.description}
        EVENTS[event_id] = ev
        res = CalendarEventResult(**ev)
        return {'success': True, 'result': res.dict()}
    except Exception as e:
        return JSONResponse(status_code=500, content={'success': False, 'error': str(e)})

@app.get('/health')
async def health():
    return {'status': 'ok'}
