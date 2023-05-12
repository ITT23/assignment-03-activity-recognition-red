# this program recognizes activities
import pandas as pd
from sklearn.preprocessing import scale, MinMaxScaler
from sklearn import svm, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from DIPPID import SensorUDP
import time

# use UPD (via WiFi) for communication
PORT = 5701
sensor = SensorUDP(PORT)


data = pd.DataFrame()
activities=["waving", "standing", "punching"]

for i in range(0, 9):
    for act in activities:
        new_data = pd.read_csv(f'./data/data_{act}_{i}.csv')
        frames = [data, new_data]
        data = pd.concat(frames)

sensor_data = pd.DataFrame(data.drop(['activity','timestamp'],axis=1))
labels = data.activity.values.astype(object)

# transform into numerical labels
encoder = preprocessing.LabelEncoder()
encoder.fit(data['activity'])
y = encoder.transform(data['activity'])

# mean removal: center values around mean
scaled_samples = scale(sensor_data)

data_mean = sensor_data.copy()

data_mean = scaled_samples

print(data_mean[:5])

# normalization: map all values to a certain range
s = MinMaxScaler()
s.fit(data_mean)
scaled_samples = s.transform(data_mean)

data_normalized = data_mean.copy()

data_normalized = scaled_samples

print(data_normalized[:5])

X_train, X_test, y_train, y_test = train_test_split(data_normalized, y, test_size=0.2,random_state=109) # 80% training and 20% test

classifier = svm.SVC(kernel='linear')
#classifier = svm.SVC(kernel='rbf') # non-linear classifier

classifier.fit(X_train, y_train)

#y_pred_train = classifier.predict(X_train)
y_pred_test=classifier.predict(X_test)

print('Model accuracy score with linear kernel and C=1000.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred_test)))

while(True):

    if sensor.has_capability('accelerometer'):
        acc_x = float(sensor.get_value('accelerometer')['x'])
        acc_y = float(sensor.get_value('accelerometer')['y'])
        acc_z = float(sensor.get_value('accelerometer')['z'])

    if sensor.has_capability('gyroscope'):
        gyr_x = float(sensor.get_value('gyroscope')['x'])
        gyr_y = float(sensor.get_value('gyroscope')['y'])
        gyr_z = float(sensor.get_value('gyroscope')['z'])

    if sensor.has_capability('gravity'):
        grav_x = float(sensor.get_value('gravity')['x'])
        grav_y = float(sensor.get_value('gravity')['y'])
        grav_z = float(sensor.get_value('gravity')['z'])


    pred = classifier.predict([[acc_x, acc_y, acc_z, gyr_x, gyr_y, gyr_z, grav_x, grav_y, grav_z]])
    print(encoder.classes_[pred])
    time.sleep(0.1)


