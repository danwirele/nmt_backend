from app.database.database import SessionLocal

from app.models.alert import *
from app.schemas.alert import *

from uuid import UUID
from sqlalchemy.orm import Session, joinedload


class AlertRepository:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db

    def get_by_id(self, alert_id: UUID) -> Alert:
        return self.db.query(Alert).options(joinedload(Alert.rules)).filter(Alert.id == alert_id).first()
    
    
    def get_all(self) -> list[Alert]:
        return self.db.query(Alert).all()
    
    def get_alerts_by_sensor_id(self, sensor_id: UUID) -> list[Alert]:
            return self.db.query(Alert).join(AlertSensor, Alert.id == AlertSensor.alert_id).filter(AlertSensor.sensor_id == sensor_id).all()
        # alert_ids = self.db.query(AlertSensor).filter(AlertSensor.sensor_id == sensor_id).all()
        # return self.db.query(Alert).filter(alert_ids.__contains__(Alert.id)).all()

    def create(self, alert_data: AlertCreate) -> Alert:
        try:
            alert_rules = [AlertRule(type=rule.type, value=rule.value) for rule in alert_data.rules]
            alert = Alert(title=alert_data.title, message=alert_data.message, description=alert_data.description, type=alert_data.type, rules=alert_rules)
            self.db.add(alert)
            self.db.commit()
            self.db.refresh(alert)
            return alert
        except Exception as e:
            self.db.rollback()
            raise e
    
    def update_alert(self, alert_id: UUID, alert_data: AlertUpdate) -> Alert:
        alert = self.get_by_id(alert_id)
        if alert:
            alert.title = alert_data.title
            alert.message = alert_data.message
            alert.description = alert_data.description
            alert.type = alert_data.type
            alert.rules = [AlertRule(alert_id=alert.id, type=rule.type, value=rule.value) for rule in alert_data.rules]

            self.db.commit()
            self.db.refresh(alert)
            return AlertResponse.from_orm(alert)
        return None
        
    def delete(self, alert: Alert):
        try:
            self.db.delete(alert)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e

    def add_sensor(self, alert_id: UUID, sensor_id: UUID) -> AlertSensor:
        existing_sensor = self.db.query(AlertSensor).filter(
            AlertSensor.alert_id == alert_id,
            AlertSensor.sensor_id == sensor_id
        ).first()
        
        if existing_sensor:
            return existing_sensor
        
        try:
            alert_sensor = AlertSensor(alert_id=alert_id, sensor_id=sensor_id)
            self.db.add(alert_sensor)
            self.db.commit()
            self.db.refresh(alert_sensor)
            return alert_sensor
        except Exception as e:
            self.db.rollback()
            raise e

    def remove_sensor(self, alert_id: UUID, sensor_id: UUID):
        alert_sensor = self.db.query(AlertSensor).filter(
            AlertSensor.alert_id == alert_id,
            AlertSensor.sensor_id == sensor_id
        ).first()

        if alert_sensor:    
            try:
                self.db.delete(alert_sensor)
                self.db.commit()
                return True
            except Exception as e:
                self.db.rollback()
                raise e
        return False
