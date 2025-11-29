from fastapi import APIRouter
from schemas import ChatRequest, ChatResponse, RiskRequest
from nlp import detect_intent, generate_reply
from risk_model import estimate_risk

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    intent, keyword = detect_intent(req.message)
    reply = generate_reply(intent, keyword, req.message)
    return {"reply": reply, "intent": intent, "data": {}}

@router.post("/risk")
def risk(req: RiskRequest):
    return estimate_risk(req.age or 0, req.symptoms, req.chronic_conditions)

@router.get("/health")
def health():
    return {"status": "ok", "service": "MediMind AI Backend"}
