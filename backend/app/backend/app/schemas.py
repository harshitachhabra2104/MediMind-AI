from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str
    intent: str
    data: dict | None = None

class RiskRequest(BaseModel):
    age: int | None = None
    symptoms: list
    chronic_conditions: list = []
