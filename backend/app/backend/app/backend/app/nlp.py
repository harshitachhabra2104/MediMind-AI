INTENT_KEYWORDS = {
    "symptom_check": ["fever", "cough", "headache", "pain", "breath"],
    "prevention": ["prevent", "vaccine", "sanitize"],
    "disease_info": ["covid", "dengue", "malaria"],
    "greeting": ["hi", "hello", "hey"],
    "thanks": ["thank"]
}

def detect_intent(text):
    t = text.lower()
    for intent, words in INTENT_KEYWORDS.items():
        if any(w in t for w in words):
            return intent, None
    return "general_query", None

def generate_reply(intent, keyword, text):
    if intent == "greeting":
        return "Hi! I am MediMind AI. Ask me health-related questions."
    if intent == "prevention":
        return "Basic prevention: wash hands, wear masks, avoid sick people."
    if intent == "disease_info":
        return "Here is disease info: follow WHO and ICMR guidelines."
    if intent == "symptom_check":
        return "I can help you assess your symptoms. Tell me what you feel."
    if intent == "thanks":
        return "You're welcome. Stay healthy!"
    return "Sorry, I did not understand. Can you rephrase?"
