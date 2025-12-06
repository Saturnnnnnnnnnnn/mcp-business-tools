
from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any

class ExchangeRateArgs(BaseModel):
    from_currency: str = Field(..., example="USD")
    to_currency: str = Field(..., example="RUB")

class ExchangeRateResult(BaseModel):
    rate: float
    base: str
    target: str

class SendEmailArgs(BaseModel):
    to: EmailStr
    subject: str
    body: str
    attachments: Optional[Dict[str, Any]] = None

class SendEmailResult(BaseModel):
    message_id: Optional[str]
    status: str

class CalendarEventArgs(BaseModel):
    title: str
    start_iso: str
    end_iso: Optional[str]
    description: Optional[str]

class CalendarEventResult(BaseModel):
    event_id: str
    title: str
    start_iso: str
    end_iso: Optional[str]
