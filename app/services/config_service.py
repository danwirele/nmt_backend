from typing import List
from app.repositories.config_repository import ConfigRepository

from app.schemas.config import *

from uuid import UUID


class ConfigService:
    def __init__(self):
        self.repository = ConfigRepository()


    async def create_config(self, config_data: ConfigCreate) -> ConfigResponse:
        config = self.repository.create(config_data)
        return ConfigResponse.from_orm(config)


    async def get_config_by_id(self, config_id: UUID) -> ConfigResponse:
        config = self.repository.get_by_id(config_id)
        return ConfigResponse.from_orm(config) if config else None
    

    async def get_all_configs(self) -> List[ConfigResponse]:
        configs = self.repository.get_all()
        if configs is None:
            return None
        return [ConfigResponse.from_orm(config) for config in configs]
        # return [ConfigResponse.from_orm(config) for config in configs] if configs else []


    async def get_config_by_id_with_tabs(self, config_id: UUID) -> CFDebugResponse:
        config = self.repository.get_by_id(config_id)
        tabs = self.repository.get_tabs_by_config_id(config_id)
        return CFDebugResponse(
            id=config.id, 
            title=config.title, 
            tabs=[t.id for t in tabs]
        ) if config else None
    

    async def update_config(self, config_id: UUID, config_data: ConfigCreate) -> ConfigResponse:
        config = self.repository.get_by_id(config_id)
        if config:
            for key, value in config_data.dict().items():
                setattr(config, key, value)
            self.repository.db.commit()
            return ConfigResponse.from_orm(config)
        return None


    async def delete_config(self, config_id: UUID) -> bool:
        config = self.repository.get_by_id(config_id)
        if config:
            self.repository.delete(config)
            return True
        return False
