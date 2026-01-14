from fastapi import APIRouter, Request

router = APIRouter()

VERIFY_TOKEN = "property_ai_verify"

@router.get("/webhook")
async def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return int(challenge)

    return {"error": "Verification failed"}

@router.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("WhatsApp says:", data)
    return {"status": "ok"}
