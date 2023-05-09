# this program gathers sensor data
import time
from DIPPID import SensorUDP

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

capture_data = False
start_time = 0

while (True):
    if sensor.has_capability('button_1'):
        button_1 = sensor.get_value('button_1')
        if int(button_1) == 1:
            capture_data = True
            start_time = time.time()

        if capture_data:
            print(time.time() - start_time)
