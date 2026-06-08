import asyncio

from fastapi import FastAPI
from fastapi import HTTPException

from registry.models import (
    RegisterRequest,
    HeartbeatRequest
)

from registry.service_registry import (
    ServiceRegistry
)

app = FastAPI()

registry = ServiceRegistry()


@app.on_event("startup")
async def startup():

    async def cleanup_loop():

        while True:
            registry.remove_dead_services()
            await asyncio.sleep(5)

    asyncio.create_task(
        cleanup_loop()
    )


@app.get("/")
async def root():

    return {
        "service": "registry",
        "status": "running"
    }


@app.post("/register")
async def register(
    request: RegisterRequest
):

    registry.register(
        request.service_id,
        str(request.url)
    )

    return {
        "message": "registered"
    }


@app.post("/heartbeat")
async def heartbeat(
    request: HeartbeatRequest
):

    success = registry.heartbeat(
        request.service_id
    )

    if not success:

        raise HTTPException(
            status_code=404,
            detail="service not found"
        )

    return {
        "message": "heartbeat received"
    }


@app.get("/services")
async def services():

    return registry.get_healthy_services()