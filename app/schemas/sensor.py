from app.models.sensor import SensorType

from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class SensorCreate(BaseModel):
    config_id: UUID
    title: str
    details: str
    type: SensorType
    alert_ids: list[UUID]


class SensorUpdate(BaseModel):
    title: str
    details: str
    alert_ids: list[UUID]


class SensorResponse(BaseModel):
    id: UUID
    title: str
    details: str
    type: SensorType

    class Config:
        from_attributes=True


class SensorHistoryCreate(BaseModel):
    sensor_id: UUID
    value: float


class SensorHistoryCreateDebug(BaseModel):
    value: float


class SensorHistoryResponse(BaseModel):
    id: UUID
    # sensor_id: UUID
    date: datetime
    value: float

    class Config:
        from_attributes=True
