import uuid

from sqlalchemy import Column, String, ForeignKey, Enum, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.database.database import Base
from enum import Enum as PyEnum


class AlertType(PyEnum):
    info = "info"
    warning = "warning"
    error = "error"
    fatal = "fatal"


class Alert(Base):
    __tablename__ = 'alerts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)
    message = Column(String)
    description = Column(String)
    type = Column(Enum(AlertType))

    rules = relationship('AlertRule', backref='alert', cascade="all, delete-orphan")


class AlertSensor(Base):
    __tablename__ = 'alertsensors'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    alert_id = Column(UUID(as_uuid=True), ForeignKey('alerts.id', ondelete='CASCADE'))
    sensor_id = Column(UUID(as_uuid=True), ForeignKey('sensors.id', ondelete='CASCADE'))


class RuleType(PyEnum):
  less_than = "lessThan"
  greater_than = "greaterThan"


class AlertRule(Base):
    __tablename__ = 'alertrules'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    alert_id = Column(UUID(as_uuid=True), ForeignKey('alerts.id', ondelete='CASCADE'))
    type = Column(Enum(RuleType))
    value = Column(Float)

    # alert = relationship('Alert', back_populates='rules')

   