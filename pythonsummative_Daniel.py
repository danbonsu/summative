#Imported Libraries (Random, Time)
import random as rand
from datetime import datetime

#Created sensorCluster array to hold 32 sensors and readings array to hold 16 floats
sensorCluster = []
readings = []

#Created function which checks for error. Takes param as array number and returns err
def checkerror(x):
        if 'err' in sensorCluster[x]:
            return 'err'

#Loop which begins populating sensor clusters with data
for i in range(1,33):
    for n in range(1,17):
        sensorDataNumber = rand.random()
        readings.append(sensorDataNumber)

#appends from readings array to sensor cluster array
    sensorCluster.append(readings)
#empty readings array and begins loop with new set of 16 floats
    readings=[]

#Created corrupted data at the following indexes
sensorCluster[3].append("err")
sensorCluster[4].append("err")
sensorCluster[6].append("err")

#Creates timestamp and writes sensor data to file
with open("test.txt", "a") as f:
     st_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
     f.write('\n')
     f.write(st_time)
     f.write('\n' + "{}".format(sensorCluster))

#Check sensorCluster array and calls check error function, if there is error write to error log file
for counter, value in enumerate(sensorCluster):
 if checkerror(counter):
    #print (counter,value)

    with open("log.txt", "a") as f:
        st_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
        f.write('\n')
        f.write(st_time)
        f.write("Problem happened with sensor at location " + '%d' % counter)


