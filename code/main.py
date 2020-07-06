'''
  * @file main.py
  * @brief main function.
  * @author Shiang-Yu Hu 
  * @date 2019/09/26 
'''

from data import Data
from sensor import Sensor
from energy import Energy
from greedy import Greedy
from picture import Picture
from sa import Sa
from lsabc import Lsabc
from nsga import Nsga
from kmeans import Kmeans
from agglomerativeClustering import AgglomerativeCluster

#parameter setting
sensorNumber = 75
radius = 133.0
iteration = 1000
population = 10
crossRate = 1
mutatRate = 0.8
times = 1

#--------------------------------#
sensorNode = []                  #
candidate = []                   #
final = []                       #
finalset = []                    #
saList = []                      #
saCharger = []                   #
lsabcList = []                   #
lsabcCharger = []                #
nsgaList = []                    #
nsgaCharger = []                 #
#--------------------------------#

#algorithm select
greedyFlag = 0
saFlag = 1
lsabcFlag = 0
nsgaFlag = 0

data = Data( sensorNumber )
#data.createSensor()
sensorNode = data.readSensor()

sensor = Sensor( radius, sensorNode )
candidate = sensor.run()

if greedyFlag == 1:
    greedy = Greedy( radius, sensorNode, candidate )
    final = greedy.run()
    print( len( final ) )

for i in range(times):
    if saFlag == 1:
        sa = Sa(  radius, sensorNode, candidate )
        final = sa.run( iteration )
        saList.append( final )
        saCharger.append( len( final ) )
        print( len( final ) )
        
    if lsabcFlag == 1:
        lsabc = Lsabc(  radius, sensorNode, candidate )
        final = lsabc.run( iteration )
        lsabcList.append( final )
        lsabcCharger.append( len( final ) )
        print( len( final ) )
        
    if nsgaFlag == 1:
        nsga = Nsga(  radius, sensorNode, candidate )
        finalset = nsga.run( iteration, population, crossRate, mutatRate )
        
        for j in range( len( finalset ) ): 
            #picture = Picture( radius, sensorNode, finalset[j] )
            #picture.draw()
            energy = Energy( radius, sensorNode, finalset[j] )
            #print( len(finalset[j]) )
            totalEnergy = energy.run()
            #print(totalEnergy)
        
        nsgaList.append( finalset[0] )
        nsgaCharger.append( len( finalset[0] ) )
        #print( len( finalset[0] ) )

    #kmeans = Kmeans(  radius, sensorNode, candidate )
    #final = kmeans.run( iteration )

    #agglomerativeClustering = AgglomerativeCluster(  radius, sensorNode, candidate )
    #final = agglomerativeClustering.run( )
    
    i = i + 1
    
sasum = 0
lsabcsum = 0
nsgasum = 0

for i in range(times):
    if saFlag == 1:
        sasum = sasum + saCharger[i]
        
    if lsabcFlag == 1:
        lsabcsum = lsabcsum + lsabcCharger[i]
        
    if nsgaFlag == 1:
        nsgasum = nsgasum + nsgaCharger[i]

#print result
if saFlag == 1:    
    print( "Sa average: " , sasum / times)
    
if lsabcFlag == 1:
    print( "Lsabc average: " , lsabcsum / times)
    
if nsgaFlag == 1:
    print( "Nsga average: " , nsgasum / times)


picture = Picture( radius, sensorNode, final )
picture.draw()
energy = Energy( radius, sensorNode, final )
totalEnergy = energy.run()
print( totalEnergy )
print( len( final ) )
