from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import socket

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)

SUPPORT_FILE = "supporters.jsonl"
ACCESS_LOG = "access.log"


class ClientInfo(BaseModel):
    timestamp: datetime
    ip: str | None
    user_agent: str | None
    language: str | None
    referer: str | None
    x_forwarded_for: str | None


# Pydantic models
class Message(BaseModel):
    created: datetime
    nickname: str
    message: str


class SupportRequest(BaseModel):
    nickname: str
    message: str


@app.get('/')
def hello():
    hostname = socket.gethostname()
    return {
        'comment': 'Greenland is NOT for sale!',
        'hostname': hostname
    }


@app.post('/support', response_model=Message)
def support(payload: SupportRequest, request: Request):
    record = Message(
        created=datetime.now(),
        nickname=payload.nickname,
        message=payload.message
    )

    with open(SUPPORT_FILE, "a", encoding="utf-8") as f:
        f.write(record.model_dump_json() + "\n")

    # Log client info
    client_info = ClientInfo(
        timestamp=datetime.now(),
        ip=request.client.host if request.client else None,
        user_agent=request.headers.get("user-agent"),
        language=request.headers.get("accept-language"),
        referer=request.headers.get("referer"),
        x_forwarded_for=request.headers.get("x-forwarded-for")
    )

    with open(ACCESS_LOG, "a", encoding="utf-8") as f:
        f.write(client_info.model_dump_json() + "\n")

    return record


@app.get('/supporters', response_model=list[Message])
def supporters():
    items = []
    try:
        with open(SUPPORT_FILE, "r", encoding="utf-8") as f:
            for line in f:
                items.append(Message.model_validate_json(line))
    except FileNotFoundError:
        pass
    return items


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8844)
