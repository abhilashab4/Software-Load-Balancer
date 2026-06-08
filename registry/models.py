from pydantic import BaseModel, HttpUrl


class RegisterRequest(BaseModel):
    service_id: str
    url: HttpUrl


class HeartbeatRequest(BaseModel):
    service_id: str


class ServiceResponse(BaseModel):
    service_id: str
    url: str