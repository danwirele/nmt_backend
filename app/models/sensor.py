import uuid

from sqlalchemy import Column, String, Enum, ForeignKey, DateTime, Float
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base

from enum import Enum as PyEnum
from datetime import datetime


class SensorType(PyEnum):
    temperature = "temperature"
    humidity = "humidity"


class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    config_id = Column(UUID(as_uuid=True), ForeignKey('configs.id', ondelete='CASCADE'))
    title = Column(String, unique=True)
    details = Column(String)
    type = Column(Enum(SensorType))


class SensorHistory(Base):
    __tablename__ = 'sensor_history'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sensor_id = Column(UUID(as_uuid=True), ForeignKey('sensors.id', ondelete='CASCADE'))
    date = Column(DateTime, default=datetime.utcnow)
    value = Column(Float)
