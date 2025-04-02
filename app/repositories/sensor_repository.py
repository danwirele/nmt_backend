from app.database.database import SessionLocal

from app.models.sensor import *
from app.models.alert import *
from app.schemas.sensor import *

from uuid import UUID
from sqlalchemy.orm import Session


class SensorRepository:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db


    def create(self, sensor_data: SensorCreate) -> Sensor:
        try:
            sensor = Sensor(
                config_id=sensor_data.config_id,
                title=sensor_data.title,
                details=sensor_data.details,
                type=sensor_data.type
            )
            
            self.db.add(sensor)
            self.db.flush()
            
            self.db.add_all([AlertSensor(alert_id=alert_id, sensor_id=sensor.id) for alert_id in sensor_data.alert_ids])
            self.db.commit()
            self.db.refresh(sensor)
            return sensor
        except Exception as e:
            self.db.rollback()
            raise e
        

    def update(self, sensor_id: UUID, sensor_data: SensorUpdate) -> Sensor:
        try:
            sensor = self.get_by_id(sensor_id)
            if sensor:
                sensor.title=sensor_data.title
                sensor.details=sensor_data.details            
                self.db.query(AlertSensor).filter(AlertSensor.sensor_id == sensor_id).delete()
                self.db.add_all([AlertSensor(alert_id=alert_id, sensor_id=sensor.id) for alert_id in sensor_data.alert_ids])
                self.db.commit()
                self.db.refresh(sensor)
                return sensor
            return None
        except Exception as e:
            self.db.rollback()
            raise e

    def create_sensor_history(self, history_data: SensorHistoryCreate) -> SensorHistory:
        try:
            entry = SensorHistory(
            sensor_id=history_data.sensor_id,
            value=history_data.value
            )
            self.db.add(entry)
            self.db.commit()
            self.db.refresh(entry)
            return entry
        except Exception as e:
            self.db.rollback()
            raise e


    def get_by_id(self, sensor_id: UUID) -> Sensor:
        return self.db.query(Sensor).filter(Sensor.id == sensor_id).first()
    

    def get_sensors_by_ids(self, sensor_ids: list[UUID]) -> list[Sensor]:
        return self.db.query(Sensor).filter(Sensor.id.in_(sensor_ids)).all()


    def get_history_by_sensor_id(self, sensor_id: UUID) -> list[SensorHistory]:
        return self.db.query(SensorHistory).filter(SensorHistory.sensor_id == sensor_id).order_by(SensorHistory.date).all()


    def get_history_by_id(self, history_id: UUID) -> SensorHistory:
        return self.db.query(SensorHistory).filter(SensorHistory.id == history_id).first()


    def delete(self, sensor: Sensor):
        try:
            self.db.delete(sensor)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def delete_history(self, history: SensorHistory):
        try:
            self.db.delete(history)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e