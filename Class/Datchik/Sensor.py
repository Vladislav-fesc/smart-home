class Sensor:

  def __init__(self, sensor_id, name, measurement_type, floor_number):
    self.sensor_id = sensor_id
    self.name = name
    self.measurement_type = measurement_type
    self.floor_number = floor_number

  def measure(self):
    pass