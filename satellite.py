from sensore import Sensore
from typing import List, Dict, Any

class Satellite:
    def __init__(self):
        self.name = name
        self.sensors: Dict[str, Sensore] = {}
        self.readings: List[Dict[str, Any]] = []
    def add_sensor(self, sensor):
       if sensor.code in self.sensors:
            raise ValueError(f"Sensor with code '{sensor.code}' is already registered.")
        self.sensors[sensor.code] = sensor
        
    def regist_value(self, code:str, value:float):
        if sensor_code not in self.sensors:
            raise KeyError(f"Sensor code '{sensor_code}' not found in the satellite.")
        
        sensor = self.sensors[sensor_code]
        # Il confronto è strettamente valore > soglia_massima
        alarm = value > sensor.max_threshold

        reading = {
            "sensor": sensor.code,
            "metric": sensor.size,
            "value": value,
            "unit": sensor.unit,
            "alarm": alarm
        }
        self.readings.append(reading)
    def telemetry_alarm(self):
        return [r for r in self.readings if r["alarm"]]
            
    def riepilogue(self)->None:
        print(f"=== Satellite Summary: {self.name} ===")
        print(f"Registered sensors: {list(self.sensors.keys())}")
        print("Readings list:")
        for r in self.readings:
            status = "ALARM" if r["alarm"] else "OK"
            print(f"- [{status}] Sensor {r['sensor']} ({r['metric']}): {r['value']} {r['unit']} (Threshold exceeded? {r['alarm']})")