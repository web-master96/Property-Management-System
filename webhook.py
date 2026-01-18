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


from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/webhook")
def verify_webhook(
    hub_mode: str = None,
    hub_challenge: str = None,
    hub_verify_token: str = None,
):
    VERIFY_TOKEN = "my_secret_token"

    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)

    return {"error": "Verification failed"}


@router.post("/webhook")
async def receive_message(request: Request):
    data = await request.json()
    print("Incoming message:", data)
    return {"status": "received"}
