import numpy as np

thefile = open('kpoint.txt', 'r')
lines = thefile.readlines()

e = 2;
minValue = float('inf')
avg = 0
avgEnergy = []
for line in lines:
    line = str.strip(line)
    values = [float(x) - 2 for x in line.split('\t')[1:]]
    #print(minValue)
    minValue = min([minValue,float(min(values))])
    avgEnergy.append(np.mean(values));
print('MinValue is ',minValue)
print('Average value is ',np.mean(avgEnergy))
   
    