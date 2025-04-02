from typing import List
from app.repositories.alert_repository import AlertRepository

from app.schemas.sensor import *
from app.schemas.alert import *
from app.models.alert import *

from uuid import UUID


class AlertService:
    def __init__(self):
        self.repository = AlertRepository()


    async def get_alert_by_id(self, alert_id: UUID) -> AlertResponse:
        alert = self.repository.get_by_id(alert_id)
        return AlertResponse.from_orm(alert) if alert else None
    

    async def get_all_alerts(self) -> List[AlertResponse]:
        alerts = self.repository.get_all()
        return [AlertResponse.from_orm(alert) for alert in alerts] if alerts else []
    

    async def get_alerts_by_sensor_id(self, sensor_id: UUID) -> List[AlertResponse]:
        alerts = self.repository.get_alerts_by_sensor_id(sensor_id)
        return [AlertResponse.from_orm(alert) for alert in alerts] if alerts else []
    

    async def create_alert(self, alert_data: AlertCreate) -> AlertResponse:
        alert = self.repository.create(alert_data)
        return AlertResponse.from_orm(alert)
    

    async def update_alert(self, alert_id: UUID, alert_data: AlertUpdate) -> AlertResponse:
        updated_alert = self.repository.update_alert(alert_id, alert_data)
        if updated_alert:
            return AlertResponse.from_orm(updated_alert)
        return None


    async def delete_alert(self, alert_id: UUID) -> bool:
        alert = self.repository.get_by_id(alert_id)
        if alert:
            self.repository.delete(alert)
            return True
        return False


    async def add_sensor_to_alert(self, alert_id: UUID, sensor_id: UUID) -> AlertSensorResponse:
        alert_sensor = self.repository.add_sensor(alert_id, sensor_id)
        return AlertSensorResponse(id=alert_sensor.id)


    async def remove_sensor_from_alert(self, alert_id: UUID, sensor_id: UUID) -> bool:
        success = self.repository.remove_sensor(alert_id, sensor_id)
        return success
