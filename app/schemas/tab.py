from pydantic import BaseModel
from uuid import UUID


class TabCreate(BaseModel):
    config_id: UUID
    title: str
    sensor_ids: list[UUID]


class TabUpdate(BaseModel):
    title: str
    

class TabResponse(BaseModel):
    id: UUID
    title: str

    class Config:
        from_attributes=True


class TabSensorResponse(BaseModel):
    id: UUID

    class Config:
        from_attributes=True


class TSDebugResponse(BaseModel):
    tab_id: UUID
    config_id: UUID
    title: str
    sensors: list[UUID]

    class Config:
        from_attributes=True
