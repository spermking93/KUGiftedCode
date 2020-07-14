import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import csv
import pandas as pd

def genRan(inN, inRmin, inRmax):
    outRanL = [random.randint(inRmin,inRmax) for i in range(inN)]
    return outRanL

testRan = genRan(10, 1,100)
print(testRan)

def calData(inData,w,b):
    outData = w * inData + b
    return outData

inCal = np.array(range(100))
print(inCal)
testCal = calData( inCal , 10. , 10. )
print(testCal)

def csvWr(i,inData):
    f = open('outTest.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([i,inData])
    f.close()

csvWr(0,testCal)

def csvR(inData):
    f = open(inData, 'r', encoding='utf-8')
    r = csv.reader(f)
    for line in r:
        print(line)
    f.close()
csvR("outTest.csv")


def plot2D(xData, yData):
    plt.figure(figsize=(5, 5))
    plt.scatter(xData, yData, c='blue', alpha=0.2)
    plt.show()

#plot(inCal, testCal)

def conDf(xData, yData, zData):
    dfOut = pd.DataFrame({"x":xData, "y":yData, "z":zData})
    return dfOut

xIn = inCal
yIn = calData( xIn , 10. , 10. )
zIn = calData( xIn, 20. ,30. )

dfTest = conDf(xIn, yIn, zIn)

print(dfTest)

def plot3D(xIn, yIn, zIn):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xIn,yIn,zIn )
    plt.show()
x3D = dfTest['x']
y3D = dfTest['y']
z3D = dfTest['z']
print(x3D)

plot3D(x3D, y3D, z3D)
