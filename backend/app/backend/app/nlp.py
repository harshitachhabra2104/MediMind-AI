"""
Simple keyword-based NLP intent handler.
Replace this with a model-backed pipeline (BERT / Llama) later.
"""

from typing import Tuple

INTENT_KEYWORDS = {
    "symptom_check": ["fever", "cough", "headache", "shortness", "breath", "pain", "vomit", "diarrhea"],
    "prevention": ["prevent", "preventive", "vaccine", "vaccination", "mask", "sanitize", "handwash"],
    "disease_info": ["covid", "malaria", "dengue", "influenza", "tb", "tuberculosis"],
    "greeting": ["hi", "hello", "hey"],
    "thanks": ["thanks", "thank you", "thx"]
}

def detect_intent(text: str) -> Tuple[str, str]:
    t = text.lower()
    for intent, keys in INTENT_KEYWORDS.items():
        for k in keys:
            if k in t:
                return intent, k
    # default fallback
    if "symptom" in t or "i feel" in t:
        return "symptom_check", None
    return "general_query", None

def generate_reply(intent: str, keyword: str, text: str) -> str:
    if intent == "greeting":
        return "Hello! I am MediMind AI. Tell me your symptoms or ask health-related questions."
    if intent == "thanks":
        return "You're welcome! Stay safe."
    if intent == "prevention":
        return ("Basic preventive steps: wash hands frequently, practice respiratory hygiene, "
                "keep distance from sick people, and get vaccinated as per guidelines.")
    if intent == "disease_info":
        # minimal disease info stub
        if "covid" in text:
            return "COVID-19 is a viral infection. For updates, follow WHO/ICMR guidance. If severe symptoms appear, consult a doctor."
        return "Please specify the disease you want information about."
    if intent == "symptom_check":
        return ("I can help with a basic symptom check. Please answer a few short questions about your symptoms, "
                "duration, and any chronic conditions.")
    return "I could not fully understand. Can you please rephrase? If you are unwell, seek medical attention."
