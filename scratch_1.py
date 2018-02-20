import random as rand
from datetime import datetime

sensorCluster = []
readings = []

for i in range(1,33):
    for n in range(1,17):
        sensorDataNumber = rand.random()
        readings.append(sensorDataNumber)
#appends to array
    sensorCluster.append(readings)
    readings=[]


#creates timestamp and writes data to file
with open("test.txt", "a") as f:
     st_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
     f.write(st_time)
     f.write("{}".format(sensorCluster))
     f.write('\n')

