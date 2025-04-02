import random
import asyncio

from app.models.sensor import Sensor, SensorType

from math import exp


class SensorTwins:
    MAX_TEMP = 40  # Max temperature
    MIN_TEMP = -40  # Min temperature
    DELAYED_DURATION = 2  # Delay in seconds


    def __init__(self, sensor: Sensor):
        self.random = random.Random()
        self.sensor = sensor
        self.curr_temp = 0.0
        self.curr_humid = 0.0
        self.steps = 0
        self.current_range = {'max': 0, 'min': 0}


    def init_start_temp(self):
        self.curr_temp = self.random.uniform(self.MIN_TEMP, self.MAX_TEMP)


    def gen_steps(self):
        self.steps = 1 + self.random.randint(0, 9)


    def gen_range(self):
        delta = 1 + self.random.randint(0, 2)
        next_max_temp = round(self.curr_temp + delta)
        self.current_range['max'] = min(next_max_temp, self.MAX_TEMP)
        next_min_temp = round(self.curr_temp - delta)
        self.current_range['min'] = max(next_min_temp, self.MIN_TEMP)


    def gen_curr_temp(self):
        min_range = self.current_range['min']
        a = self.current_range['max'] - min_range
        self.curr_temp = min_range + abs(self.random.randint(0, a) - self.random.random())
        self.steps -= 1
        return self.curr_temp


    def gen_curr_humidity(self):
        curr_e = 6.11 * exp((17.67 * self.curr_temp) / (self.curr_temp + 243.5))
        dew_point = self.curr_temp / 1.5
        curr_es = 6.11 * exp((17.67 * dew_point) / (dew_point + 243.5))
        self.curr_humid = 100 * curr_e / curr_es
        return self.curr_humid / 2.15 - 5


    async def change_curr_temp(self):
        chance = self.random.random()
        max_change_chance = 0.05
        if chance <= max_change_chance:
            self.steps = 2 + self.random.randint(0, 3)
            sign = 1 if self.random.random() <= 0.55 else -1
            while self.steps > 0:
                change_temp = self.curr_temp + sign * (3 + self.random.randint(0, 5))
                self.curr_temp = min(max(change_temp, self.MIN_TEMP), self.MAX_TEMP)
                self.gen_curr_temp()
                self.gen_curr_humidity()
                self.steps -= 1
                await asyncio.sleep(self.DELAYED_DURATION)
            return True
        return False


    async def activity_twin(self):
        self.init_start_temp()
        while True:
            await asyncio.sleep(self.DELAYED_DURATION)
            if self.steps == 0:
                if await self.change_curr_temp():
                    continue
                self.gen_steps()
                self.gen_range()
            yield { 
                "temperature": self.gen_curr_temp(), 
                "humidity": self.gen_curr_humidity() 
            }

