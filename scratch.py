#Problem3

#Libraries (Random, Time)
import random as rand
from datetime import datetime

def checkError():
    if 'err' in sensorCluster:

        print 'error'

#Problem 1 (32 Sensors taking 16 floats each)
sensorCluster = []
readings = []

for i in range(1,33):
    for n in range(1,17):
        sensorDataNumber = rand.random()
        readings.append(sensorDataNumber)

#appends from readings array to sensor cluster array
    sensorCluster.append(readings)

#empty readings array
    readings=[]

sensorCluster.append("err")
checkError()

#Problem 2 (creates timestamp and writes data to file)
with open("test.txt", "a") as f:
     st_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
     f.write('\n')
     f.write(st_time)
     f.write('\n' + "{}".format(sensorCluster))
     #f.write('\n')



