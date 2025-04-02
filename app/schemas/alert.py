from app.models.alert import AlertType, RuleType

from pydantic import BaseModel, ConfigDict
from uuid import UUID


class AlertRuleModel(BaseModel):
    type: RuleType
    value: float
    
    model_config = ConfigDict(from_attributes=True)

class AlertResponse(BaseModel):
    id: UUID
    title: str
    message: str
    description: str
    type: AlertType
    rules: list[AlertRuleModel]
    
    model_config = ConfigDict(from_attributes=True)

class AlertCreate(BaseModel):
    title: str
    message: str
    description: str
    type: AlertType
    rules: list[AlertRuleModel]

class AlertUpdate(BaseModel):
    title: str
    message: str
    description: str
    type: AlertType
    rules: list[AlertRuleModel]


class AlertSensorResponse(BaseModel):
    id: UUID

    class Config:
        from_attributes=True

