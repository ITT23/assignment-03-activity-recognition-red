# this program gathers sensor data
import time
from DIPPID import SensorUDP
import csv
import helpers
from helpers.arg_parser import get_parsed_arguments
#from helpers import arg_parser

# use UPD (via WiFi) for communication
PORT = 5700
sensor = SensorUDP(PORT)

capture_data = False
start_time = 0
args  = helpers.arg_parser.get_parsed_arguments()
label = args.activity#"standing"
number = args.number #0

headers= ['timestamp', 'accelerometer_x', 'accelerometer_y', 'accelerometer_z', 'gyroscope_x', 'gyroscope_y', 'gyroscope_z', 'gravity_x', 'gravity_y', 'gravity_z', 'activity']
data =[]


def save_data():

    with open('./data/data_' + label + '_' + str(number) + '.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)
        writer.writerows(data)
        

while (True):
    if sensor.has_capability('button_1'):
        button_1 = sensor.get_value('button_1')
        if int(button_1) == 1 and not capture_data:
            print("started")
            capture_data = True
            start_time = time.time()

        if capture_data:
            duration = round(time.time() - start_time, 2)

            acc_x = float(sensor.get_value('accelerometer')['x'])
            acc_y = float(sensor.get_value('accelerometer')['y'])
            acc_z = float(sensor.get_value('accelerometer')['z'])

            gyr_x = float(sensor.get_value('gyroscope')['x'])
            gyr_y = float(sensor.get_value('gyroscope')['y'])
            gyr_z = float(sensor.get_value('gyroscope')['z'])

            grav_x = float(sensor.get_value('gravity')['x'])
            grav_y = float(sensor.get_value('gravity')['y'])
            grav_z = float(sensor.get_value('gravity')['z'])

            data.append([duration, acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, grav_x, grav_y, grav_z, label])

            if duration > 10:
                save_data()
                print("end")
                break
    
    time.sleep(0.01)


            
