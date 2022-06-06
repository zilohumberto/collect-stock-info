import logging
from fastapi import FastAPI, status, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from collect_service import CollectService

app = FastAPI()
log = logging.getLogger(__name__)


collect_service = CollectService()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["*",])


@app.exception_handler(Exception)
async def un_handle_exception(request: Request, exception: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": f"Server unavailable"},
    )


@app.get("/")
async def collect(member_id: str, strategy: str = None):
    return await collect_service.collect(member_id=member_id, strategy=strategy,)
