from pydantic import BaseModel
from uuid import UUID

from app.schemas.sensor import SensorType

class ConfigSensor(BaseModel):
    title: str
    details: str
    type: SensorType
    alert_ids: list[UUID]


class ConfigCreate(BaseModel):
    title: str
    sensors: list[ConfigSensor]


class ConfigResponse(BaseModel):
    id: UUID
    title: str

    class Config:
        from_attributes = True


class CFDebugResponse(BaseModel):
    id: UUID
    title: str
    tabs: list[UUID]

    class Config:
        from_attributes = True
