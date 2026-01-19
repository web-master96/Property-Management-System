from fastapi import APIRouter, Request, Query, Response

router = APIRouter(prefix="/webhook")

VERIFY_TOKEN = "my_secret_token"

@router.get("")
def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
):
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return Response(content=hub_challenge, media_type="text/plain")

    return Response(content="Verification failed", status_code=403)


@router.post("")
async def receive_message(request: Request):
    data = await request.json()
    print("Incoming message:", data)
    return {"status": "received"}
