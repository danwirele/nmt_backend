from app.repositories.sensor_repository import SensorRepository

from app.repositories.tab_repository import TabRepository
from app.schemas.sensor import *
from app.models.sensor import *

from uuid import UUID


class SensorService:
    def __init__(self):
        self.repository = SensorRepository()
        self.tab_repository = TabRepository()


    async def create_sensor(self, sensor_data: SensorCreate) -> SensorResponse:
        sensor = self.repository.create(sensor_data)
        initial_history_data = SensorHistoryCreate(
            sensor_id=sensor.id,
            value=0.0
        )
        self.repository.create_sensor_history(initial_history_data)
        return SensorResponse.from_orm(sensor) if sensor else None
    
    async def update_sensor(self, sensor_id: UUID, sensor_data: SensorUpdate) -> SensorResponse:
        updated_sensor = self.repository.update(sensor_id,sensor_data)
        return SensorResponse.from_orm(updated_sensor) if updated_sensor else None 


    async def create_sensor_history_entry(self, history_data: SensorHistoryCreate) -> SensorHistoryResponse:
        sensor = self.repository.get_by_id(history_data.sensor_id)
        if sensor:
            entry = self.repository.create_sensor_history(history_data)
            return SensorHistoryResponse.from_orm(entry) if entry else None
        return None


    async def get_sensor_by_id(self, sensor_id: UUID) -> SensorResponse:
        sensor = self.repository.get_by_id(sensor_id)
        return SensorResponse.from_orm(sensor) if sensor else None
    

    async def get_sensors_by_tab_id(self, tab_id: UUID) -> list[SensorResponse]:
        tab_sensors = self.tab_repository.get_sensors_by_tab_id(tab_id)

        if not tab_sensors:
            return None

        sensors = self.repository.get_sensors_by_ids([ts.sensor_id for ts in tab_sensors])
        return [SensorResponse.from_orm(sensor) for sensor in sensors] if sensors else []


    async def get_sensor_history_by_sensor_id(self, sensor_id: UUID) -> list[SensorHistoryResponse]:
        history = self.repository.get_history_by_sensor_id(sensor_id)
        return [SensorHistoryResponse.from_orm(h) for h in history]


    async def get_sensor_history_by_id(self, history_id: UUID) -> SensorHistoryResponse:
        history = self.repository.get_history_by_id(history_id)
        if history:
            return SensorHistoryResponse.from_orm(history)
        return None


    async def update_sensor_history(self, history_id: UUID, value: float) -> SensorHistoryResponse:
        history = self.repository.get_history_by_id(history_id)
        if history:
            history.value = value
            self.repository.db.commit()
            return SensorHistoryResponse.from_orm(history)
        return None


    async def delete_sensor_history(self, history_id: UUID) -> bool:
        history = self.repository.get_history_by_id(history_id)
        if history:
            self.repository.db.delete(history)
            self.repository.db.commit()
            return True
        return False


    async def delete_sensor_history_by_sensor(self, sensor_id: UUID) -> bool:
        history = self.repository.get_history_by_sensor_id(sensor_id)
        if history:
            for record in history:
                self.repository.db.delete(record)
            self.repository.db.commit()
            return True
        return False


    async def delete_sensor(self, sensor_id: UUID) -> bool:
        sensor = self.repository.get_by_id(sensor_id)
        if sensor:
            self.repository.db.delete(sensor)
            self.repository.db.commit()
            return True
        return False
