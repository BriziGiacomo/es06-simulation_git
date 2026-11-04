class Satellite:
    def __init__(self):
        
        self.sensors=[]
        self.measures=[]
    def add_sensor(self, sensor):
        for element in self.sensors:
            if sensor.code ==element.get("code"):
                return
            
        temp_dict={"code": sensor.code, "size": sensor.size, "unit"= sensor.unit, "max_teshold": sensor.max_teshold}
        self.sensors.append(temp_dict)
        
    def regist_value(self, code:str, value:float):
        cont=0
        for element in self.sensors:
            if code == element.get("code"):
                if value<=element.get("max_teshold"):
                    temp_dict={"code":code, "value"}
                    self.measures.append(temp_dict)
                    return (f"Value registed succesfully")
                else return(f"Value is over the max_teshold of the sensor")
        raise KeyError(f"Key searched "{code}" is not present")
            
        