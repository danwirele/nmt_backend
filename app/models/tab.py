import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database.database import Base


class Tab(Base):
    __tablename__ = 'tabs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    config_id = Column(UUID(as_uuid=True), ForeignKey('configs.id', ondelete='CASCADE'))
    title = Column(String)


class TabSensor(Base):
    __tablename__ = 'tabsensors'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tab_id = Column(UUID(as_uuid=True), ForeignKey('tabs.id', ondelete='CASCADE'))
    sensor_id = Column(UUID(as_uuid=True), ForeignKey('sensors.id', ondelete='CASCADE'))
