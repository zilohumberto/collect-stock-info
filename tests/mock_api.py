import logging
from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from random import randrange

app = FastAPI()
log = logging.getLogger(__name__)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*", ]
)

members_values = {
    str(i): {
        "deductible": randrange(0, 9999), "stop_loss": randrange(0, 9999), "oop_max": randrange(0, 9999)
    } for i in range(10)
}


@app.exception_handler(Exception)
async def un_handle_exception(request: Request, exception: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": f"Server unavailable"}
    )


@app.get("/")
async def collect(member_id: str):
    if member_id in members_values:
        return members_values[member_id]
    raise ValueError("Member does not exists on testing DB!")
