'''
  * @file energy.py
  * @brief calculate sensor node energy.

  * method
     + friis
     + calcuDistance
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/08/27 
'''

import math

class Energy:
    
    def __init__( self, radius = 0, sensorNode = [], charger = []):
        self.radius = radius
        self.charger = charger
        self.sensorNode = sensorNode
        self.sensorEnergy = []
        self.chargerSet = []
        
    def friis( self, r = 0 ):
        l = 0.328
        ptgt = 3
        gr = 3.98
        pi = 3.14
        pr = round( ptgt * gr * ( l / ( 4 * pi * r ) ) * ( l / ( 4 * pi * r ) ) * 1000, 3 )
        return pr
    
    def calcuDistance( self ):
        for i in range( len( self.sensorNode ) ):
            self.sensorEnergy.append( 0 )
        for i in range( len( self.charger ) ):
            temp = []
            for j in range( len( self.sensorNode ) ):
                d = round( math.sqrt((self.charger[i][0] - self.sensorNode[j][0]) * (self.charger[i][0] - self.sensorNode[j][0]) 
                + (self.charger[i][1] - self.sensorNode[j][1]) * (self.charger[i][1] - self.sensorNode[j][1])), 2 )
                if d < self.radius:
                    d = round( d / 100, 2 )
                    r = round( math.sqrt( pow( 2.3, 2 ) + pow( d, 2 ) ), 2 )
                    temp.append([ j, r ])
            self.chargerSet.append( temp )
    
    def run( self ):
        totalEnergy = 0
        self.calcuDistance() 
        for i in range( len( self.chargerSet ) ):
            for j in range( len( self.chargerSet[i] ) ):
                if self.chargerSet[i][j][1] == 0:
                    self.sensorEnergy[self.chargerSet[i][j][0]] = self.sensorEnergy[self.chargerSet[i][j][0]] + self.friis( 2.3 )
                else:
                    self.sensorEnergy[self.chargerSet[i][j][0]] = self.sensorEnergy[self.chargerSet[i][j][0]] + self.friis( self.chargerSet[i][j][1] )
        for i in range( len( self.sensorEnergy ) ): 
            totalEnergy = totalEnergy + self.sensorEnergy[i]
        #print( self.sensorEnergy )
        return totalEnergy 