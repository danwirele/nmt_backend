from app.database.database import SessionLocal

from app.models.tab import *
from app.schemas.tab import *

from uuid import UUID
from sqlalchemy.orm import Session


class TabRepository:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db


    def create(self, tab_data: TabCreate) -> Tab:
        try:
            tab = Tab(config_id=tab_data.config_id, title=tab_data.title)
            self.db.add(tab)
            self.db.flush()
            print(tab.id)
            tab_sensors = [TabSensor(tab_id= tab.id, sensor_id=id) for id in tab_data.sensor_ids]
            self.db.add_all(tab_sensors)
            self.db.commit()
            self.db.refresh(tab)
            return tab
        except Exception as e:
            self.db.rollback()
            raise e
        

    # def create(self, tab_data: TabCreate) -> Tab:
    #     try:
    #         tab = Tab(config_id=tab_data.config_id, title=tab_data.title)
    #         self.db.add(tab)
    #         self.db.commit()
    #         self.db.refresh(tab)
    #         return tab
    #     except Exception as e:
    #         self.db.rollback()
    #         raise e


    def get_by_id(self, tab_id: UUID) -> Tab:
        return self.db.query(Tab).filter(Tab.id == tab_id).first()
    

    def get_tabs_by_config_id(self, config_id: UUID) -> list[Tab]:
        return self.db.query(Tab).filter(Tab.config_id == config_id).all()


    def get_sensors_by_tab_id(self, tab_id: UUID) -> list[TabSensor]:
        return self.db.query(TabSensor).filter(TabSensor.tab_id == tab_id).all()


    def get_all(self) -> list[Tab]:
        return self.db.query(Tab).all()


    def delete(self, tab: Tab):
        try:
            self.db.delete(tab)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def add_sensor(self, tab_id: UUID, sensor_id: UUID) -> TabSensor:
        existing_sensor = self.db.query(TabSensor).filter(
            TabSensor.tab_id == tab_id,
            TabSensor.sensor_id == sensor_id
        ).first()
        
        if existing_sensor:
            return existing_sensor
        
        try:
            tab_sensor = TabSensor(tab_id=tab_id, sensor_id=sensor_id)
            self.db.add(tab_sensor)
            self.db.commit()
            self.db.refresh(tab_sensor)
            return tab_sensor
        except Exception as e:
            self.db.rollback()
            raise e

    def remove_sensor(self, tab_id: UUID, sensor_id: UUID):
        tab_sensor = self.db.query(TabSensor).filter(
            TabSensor.tab_id == tab_id,
            TabSensor.sensor_id == sensor_id
        ).first()

        if tab_sensor:    
            try:
                self.db.delete(tab_sensor)
                self.db.commit()
                return True
            except Exception as e:
                self.db.rollback()
                raise e
        return False
