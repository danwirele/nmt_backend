from app.database.database import SessionLocal

from app.models.tab import *
from app.models.config import *
from app.schemas.config import *
from app.models.alert import AlertSensor
from app.models.sensor import Sensor

from uuid import UUID
from sqlalchemy.orm import Session


class ConfigRepository:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db


    def create(self, config_data: ConfigCreate) -> Config:   
        try:
            config = Config(title=config_data.title)
            self.db.add(config)
            self.db.flush()

            tab = Tab(id=config.id, config_id=config.id, title="Вкладка")

            self.db.add(tab)

            sensor_ids = []

            for sensor_data in config_data.sensors:
                sensor = Sensor(
                    config_id=config.id,
                    title=sensor_data.title,
                    details=sensor_data.details,
                    type=sensor_data.type
                )
                self.db.add(sensor)
                self.db.flush()

                sensor_ids.append(sensor.id)
                self.db.add_all([AlertSensor(alert_id=alert_id, sensor_id=sensor.id) for alert_id in sensor_data.alert_ids])

            self.db.add_all([TabSensor(tab_id=tab.id, sensor_id=sensor_id) for sensor_id in sensor_ids])

            self.db.commit()
            self.db.refresh(config)
            return config
        except Exception as e:
            self.db.rollback()
            raise e


    def get_by_id(self, config_id: UUID) -> Config:
        return self.db.query(Config).filter(Config.id == config_id).first()


    def get_all(self) -> list[Config]:
        return self.db.query(Config).all()


    def delete(self, config: Config):       
        try:
            self.db.delete(config)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def get_tabs_by_config_id(self, config_id: UUID) -> list[Tab]:
        return self.db.query(Tab).filter(Tab.config_id == config_id).all()
