from pydantic import BaseModel
from typing import Optional, Dict

class ChatRequest(BaseModel):
    user_id: Optional[str] = "guest"
    message: str

class ChatResponse(BaseModel):
    reply: str
    intent: Optional[str] = None
    data: Optional[Dict] = None

class RiskRequest(BaseModel):
    age: Optional[int] = None
    symptoms: list
    chronic_conditions: Optional[list] = []
