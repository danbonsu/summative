#Problem3

#Libraries (Random, Time)
import random as rand
from datetime import datetime

#Problem 1 (32 Sensors taking 16 floats each)
sensorCluster = []
readings = []


def checkerror(x):
        if 'err' in sensorCluster[x]:
            return 'err'


for i in range(1,33):
    for n in range(1,17):
        sensorDataNumber = rand.random()
        readings.append(sensorDataNumber)

#appends from readings array to sensor cluster array
    sensorCluster.append(readings)
#empty readings array
    readings=[]

sensorCluster[3].append("err")
sensorCluster[4].append("err")
sensorCluster[6].append("err")

#print sensorCluster[31]

#Problem 2 (creates timestamp and writes data to file)
with open("test.txt", "a") as f:
     st_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
     f.write('\n')
     f.write(st_time)
     f.write('\n' + "{}".format(sensorCluster))
     #f.write('\n')


#Problem 3
for counter, value in enumerate(sensorCluster):
 if checkerror(counter):
    #print (counter,value)

    with open("log.txt", "a") as f:
        st_time = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')
        f.write('\n')
        f.write(st_time)
        f.write("Problem happened with sensor at location" + '%d' % counter)


