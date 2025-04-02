from typing import List
from app.repositories.tab_repository import TabRepository

from app.schemas.sensor import *
from app.schemas.tab import *

from uuid import UUID


class TabService:
    def __init__(self):
        self.repository = TabRepository()


    async def create_tab(self, tab_data: TabCreate) -> TabResponse:
        tab = self.repository.create(tab_data)
        return TabResponse.from_orm(tab)


    async def get_tab_by_id(self, tab_id: UUID) -> TabResponse:
        tab = self.repository.get_by_id(tab_id)
        return TabResponse.from_orm(tab) if tab else None
    

    async def get_tabs_by_config_id(self, config_id: UUID) -> List[TabResponse]:
        tabs = self.repository.get_tabs_by_config_id(config_id)
        return [TabResponse.from_orm(tab) for tab in tabs] if tabs else []


    async def update_tab(self, tab_id: UUID, tab_data: TabUpdate) -> TabResponse:
        tab = self.repository.get_by_id(tab_id)
        if tab:
            tab.title = tab_data.title
            # for key, value in tab_data.dict().items():
            #     setattr(tab, key, value)
            self.repository.db.commit()
            return TabResponse.from_orm(tab)
        return None


    async def delete_tab(self, tab_id: UUID) -> bool:
        tab = self.repository.get_by_id(tab_id)
        if tab:
            self.repository.delete(tab)
            return True
        return False


    async def get_tab_by_id_with_sensors(self, tab_id: UUID) -> TSDebugResponse:
        tab = self.repository.get_by_id(tab_id)
        tab_sensors = self.repository.get_sensors_by_tab_id(tab_id)
        return TSDebugResponse(
            tab_id=tab.id, 
            config_id=tab.config_id, 
            title=tab.title, 
            sensors=[ts.sensor_id for ts in tab_sensors]
        ) if tab else None


    async def add_sensor_to_tab(self, tab_id: UUID, sensor_id: UUID) -> TabSensorResponse:
        tab_sensor = self.repository.add_sensor(tab_id, sensor_id)
        return TabSensorResponse(id=tab_sensor.id)


    async def remove_sensor_from_tab(self, tab_id: UUID, sensor_id: UUID) -> bool:
        success = self.repository.remove_sensor(tab_id, sensor_id)
        return success
