import asyncio

from app.algo.sensor_twins import SensorTwins
from app.database.database import repool_database

from app.schemas.sensor import *
from app.schemas.config import *
from app.schemas.tab import *
from app.schemas.alert import *

from app.services.sensor_service import SensorService
from app.services.config_service import ConfigService
from app.services.tab_service import TabService
from app.services.alert_service import AlertService

from asyncio import Queue
from typing import List, Dict
from uuid import UUID

from fastapi import (
    FastAPI, Depends, 
    HTTPException, status, 
    WebSocket, WebSocketDisconnect
)


app = FastAPI()


def get_sensor_service() -> SensorService:
    return SensorService()


def get_config_service() -> ConfigService:
    return ConfigService()


def get_tab_service() -> TabService:
    return TabService()

def get_alert_service() -> AlertService:
    return AlertService()


###################### Sensor Routes ######################


@app.post("/sensors/", response_model=SensorResponse)
async def create_sensor(sensor: SensorCreate, sensor_service: SensorService = Depends(get_sensor_service)):
    sensor = await sensor_service.create_sensor(sensor)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return sensor


@app.get("/sensors/{sensor_id}", response_model=SensorResponse)
async def get_sensor(sensor_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    sensor = await sensor_service.get_sensor_by_id(sensor_id)
    if not sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return sensor

@app.get("/sensors/by_tab_id/{tab_id}", response_model=list[SensorResponse])
async def get_sensors_by_tab_id(tab_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    sensors = await sensor_service.get_sensors_by_tab_id(tab_id)
    if not sensors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensors not found")
    return sensors


@app.put("/sensors/{sensor_id}", response_model=SensorResponse)
async def update_sensor(sensor_id: UUID, sensor: SensorUpdate, sensor_service: SensorService = Depends(get_sensor_service)):
    updated_sensor = await sensor_service.update_sensor(sensor_id, sensor)
    if not updated_sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return updated_sensor


@app.delete("/sensors/{sensor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sensor(sensor_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    success = await sensor_service.delete_sensor(sensor_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return {"message": "Sensor deleted"}


###################### Sensor History Routes ######################


@app.post("/sensors/{sensor_id}/history", response_model=SensorHistoryResponse)
async def add_to_history(sensor_id: UUID, history: SensorHistoryCreateDebug, sensor_service: SensorService = Depends(get_sensor_service)):
    history = await sensor_service.create_sensor_history_entry(SensorHistoryCreate(sensor_id=sensor_id, value=history.value))
    if not history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return history


@app.get("/sensors/{sensor_id}/history/{history_id}", response_model=SensorHistoryResponse)
async def get_sensor_history_entry(history_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    history = await sensor_service.get_sensor_history_by_id(history_id)
    if not history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History entry not found")
    return history


@app.get("/sensors/{sensor_id}/history", response_model=list[SensorHistoryResponse])
async def get_sensor_history(sensor_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    history = await sensor_service.get_sensor_history_by_sensor_id(sensor_id)
    if not history:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History not found for this sensor")
    return history


@app.delete("/sensors/{sensor_id}/history/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sensor_history(history_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    success = await sensor_service.delete_sensor_history(history_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="History entry not found")
    return {"message": "Sensor history deleted"}


###################### Config Routes ######################


@app.post("/configs/", response_model=ConfigResponse)
async def create_config(config: ConfigCreate, config_service: ConfigService = Depends(get_config_service)):
    config = await config_service.create_config(config)
    if not config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
    return config

@app.get("/configs", response_model=List[ConfigResponse])
async def get_all_configs(config_service: ConfigService = Depends(get_config_service)):
    configs = await config_service.get_all_configs()
    if configs is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Configs not found")
    
    return configs

    # if not configs:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
    # return configs


@app.get("/configs/{config_id}", response_model=CFDebugResponse)
async def get_config(config_id: UUID, config_service: ConfigService = Depends(get_config_service)):
    config = await config_service.get_config_by_id_with_tabs(config_id)
    if not config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
    return config


@app.put("/configs/{config_id}", response_model=ConfigResponse)
async def update_config(config_id: UUID, config: ConfigCreate, config_service: ConfigService = Depends(get_config_service)):
    updated_config = await config_service.update_config(config_id, config)
    if not updated_config:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
    return updated_config


@app.delete("/configs/{config_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_config(config_id: UUID, config_service: ConfigService = Depends(get_config_service)):
    success = await config_service.delete_config(config_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Config not found")
    return {"message": "Config deleted"}


###################### Tab Routes ######################


@app.post("/tabs/", response_model=TabResponse)
async def create_tab(tab: TabCreate, tab_service: TabService = Depends(get_tab_service)):
    tab = await tab_service.create_tab(tab)
    if not tab:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tab not found")
    return tab


@app.get("/tabs/{tab_id}", response_model=TSDebugResponse)
async def get_tab(tab_id: UUID, tab_service: TabService = Depends(get_tab_service)):
    sensors = await tab_service.get_tab_by_id_with_sensors(tab_id)
    if not sensors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tab not found")
    return sensors

@app.get("/tabs/by_config_id/{config_id}", response_model=List[TabResponse])
async def get_tabs_by_config_id(config_id: UUID, tab_service: TabService = Depends(get_tab_service)):
    tabs = await tab_service.get_tabs_by_config_id(config_id)
    if tabs is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tabs not found")
    return tabs


@app.put("/tabs/{tab_id}", response_model=TabResponse)
async def update_tab(tab_id: UUID, tab: TabUpdate, tab_service: TabService = Depends(get_tab_service)):
    updated_tab = await tab_service.update_tab(tab_id, tab)
    if not updated_tab:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tab not found")
    return updated_tab


@app.delete("/tabs/{tab_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tab(tab_id: UUID, tab_service: TabService = Depends(get_tab_service)):
    success = await tab_service.delete_tab(tab_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tab not found")
    return {"message": "Tab deleted"}


@app.put("/tabs/{tab_id}/{sensor_id}", response_model=TabSensorResponse)
async def put_sensor_to_tab(tab_id: UUID, sensor_id: UUID, tab_service: TabService = Depends(get_tab_service)):
    tab_sensor = await tab_service.add_sensor_to_tab(tab_id, sensor_id)
    if not tab_sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return TabSensorResponse(id=tab_sensor.id)


@app.delete("/tabs/{tab_id}/{sensor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sensor_from_tab(tab_id: UUID, sensor_id: UUID, tab_service: TabService = Depends(get_tab_service)):
    success = await tab_service.remove_sensor_from_tab(tab_id, sensor_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found in this tab")
    return {"message": "Sensor deleted from this tab"}


###################### Alert Routes ######################


@app.post("/alerts/", response_model=AlertResponse)
async def create_alert(alert: AlertCreate, alert_service: AlertService = Depends(get_alert_service)):
    alert = await alert_service.create_alert(alert)
    if not alert:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Incorrect params")
    return alert


@app.get("/alerts/by_id/{alert_id}", response_model=AlertResponse)
async def get_alert(alert_id: UUID, alert_service: AlertService = Depends(get_alert_service)):
    alert = await alert_service.get_alert_by_id(alert_id)
    if not alert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alert not found")
    return alert


@app.get("/alerts/all", response_model=List[AlertResponse])
async def get_all_alerts(alert_service: AlertService = Depends(get_alert_service)):
    alerts = await alert_service.get_all_alerts()
    if alerts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alerts not found")
    return alerts


@app.get("/alerts/by_sensor_id/{sensor_id}", response_model=List[AlertResponse])
async def get_alerts_by_sensor_id(sensor_id: UUID, alert_service: AlertService = Depends(get_alert_service)):
    alerts = await alert_service.get_alerts_by_sensor_id(sensor_id)
    if alerts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alerts not found")
    return alerts


@app.put("/alerts/{alert_id}", response_model=AlertResponse)
async def update_alert(alert_id: UUID, alert: AlertUpdate, alert_service: AlertService = Depends(get_alert_service)):
    updated_alert = await alert_service.update_alert(alert_id, alert)
    if not updated_alert:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alert not found")
    return updated_alert


@app.delete("/alerts/{alert_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_alert(alert_id: UUID, alert_service: AlertService = Depends(get_alert_service)):
    success = await alert_service.delete_alert(alert_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Alert not found")
    return {"message": "Alert deleted"}


@app.put("/alerts/{alert_id}/{sensor_id}", response_model=AlertSensorResponse)
async def put_sensor_to_alert(alert_id: UUID, sensor_id: UUID, alert_service: AlertService = Depends(get_alert_service)):
    alert_sensor = await alert_service.add_sensor_to_alert(alert_id, sensor_id)
    if not alert_sensor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found")
    return TabSensorResponse(id=alert_sensor.id)


@app.delete("/alerts/{alert_id}/{sensor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_sensor_from_alert(alert_id: UUID, sensor_id: UUID, alert_service: AlertService = Depends(get_alert_service)):
    success = await alert_service.remove_sensor_from_alert(alert_id, sensor_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found in this alert")
    return {"message": "Sensor deleted from this alert"}


###################### Sensor Twins Streaming ######################


active_connections: Dict[UUID, List[WebSocket]] = {}
sensor_twins_dict: Dict[UUID, SensorTwins] = {}
sensor_data_queue: Dict[UUID, Queue] = {}


async def sensor_producer(sensor_id: UUID, sensor_twins: SensorTwins):
    async for data in sensor_twins.activity_twin():
        if sensor_id in sensor_data_queue:
            await sensor_data_queue[sensor_id].put(data)


async def sensor_consumer(sensor_id: UUID, websocket: WebSocket):
    while True:
        data = await sensor_data_queue[sensor_id].get()
        await websocket.send_json(data)


@app.websocket("/sensors/{sensor_id}")
async def ws_sensors(websocket: WebSocket, sensor_id: UUID, sensor_service: SensorService = Depends(get_sensor_service)):
    await websocket.accept()
    sensor = await sensor_service.get_sensor_by_id(sensor_id)
    if not sensor:
        await websocket.send_json({"message": "Sensor not found"})
        await websocket.close()
        return
    if sensor_id not in active_connections:
        active_connections[sensor_id] = []
    active_connections[sensor_id].append(websocket)
    if sensor_id not in sensor_data_queue:
        sensor_data_queue[sensor_id] = Queue()
    if sensor_id not in sensor_twins_dict:
        sensor_twins_dict[sensor_id] = SensorTwins(sensor)
        producer_task = asyncio.create_task(sensor_producer(sensor_id, sensor_twins_dict[sensor_id]))
    consumer_task = asyncio.create_task(sensor_consumer(sensor_id, websocket))
    try:
        while True:
            await websocket.receive_text()
            ##### DEBUG #####
            # if not active_connections[sensor_id]:
            #     await websocket.send_json({"message": True})
            # await websocket.send_json({"message": False})
            ##### ##### #####
    except WebSocketDisconnect:
        active_connections[sensor_id].remove(websocket)
        if not active_connections[sensor_id]:
            del active_connections[sensor_id]
            del sensor_twins_dict[sensor_id]
            del sensor_data_queue[sensor_id]
        # TODO: Temporary cancel tasks instead of clearing 
        # TODO: connection cause of memory leaks
        # active_connections.clear()
        # sensor_twins_dict.clear()
        # sensor_data_queue.clear()
        producer_task.cancel()
        consumer_task.cancel()


###################### Notifications Streaming ######################


notification_data = Queue()


async def debug_fill_notifications():
    # Same logic can be placed where you want to add notifications; 
    # If there is no connected clients, messages 'll be stored
    # inside `notification_data` and sended on next connection
    await notification_data.put({"message": "Notification Test"})


async def notification_consumer(websocket: WebSocket):
    while True:
        data = await notification_data.get()
        await websocket.send_json(data)


@app.websocket("/notifications")
async def ws_notifications(websocket: WebSocket):
    await websocket.accept()
    consumer_task = asyncio.create_task(notification_consumer(websocket))
    try:
        while True:
            await websocket.receive_text()
            await debug_fill_notifications()
    except WebSocketDisconnect:
        consumer_task.cancel()


###################### Utility Routes (Dev) ######################


@app.get("/dev/repool")
async def repool():
    try:
        await repool_database()
    except:
        raise HTTPException(status_code=403, detail="Should be dropped by hand")
    return {"message": "Success"}
