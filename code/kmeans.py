'''
  * @file kmeans.py
  * @brief use K-means method to find final charger placement.

  * method
     + cluster
     + newKernel
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/07/09 
'''

import math

class Kmeans():
    
    def __init__( self, radius = 0, sensorNode = [], candidate = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.candidate = candidate
        self.center = self.sensorNode.copy()
        self.charger = []
        for i in range( len( self.sensorNode ) ):
            temp = []
            self.charger.append( temp )            
        
    def cluster( self ):
        for i in range( len( self.center ) ):
            temp = []
            for j in range( len( self.sensorNode ) ):
                d = round(math.sqrt((self.sensorNode[j][0] - self.center[i][0]) * (self.sensorNode[j][0] - self.center[i][0]) 
                    + (self.sensorNode[j][1] - self.center[i][1]) * (self.sensorNode[j][1] - self.center[i][1])),2)
                if d < self.radius:
                    temp.append( j )
            self.charger[i] = temp
            
    def newKernel( self ):
        for i in range( len( self.charger ) ):
            x = 0
            y = 0
            for j in self.charger[i]:
                #print( j )
                x = x + self.sensorNode[j][0]
                y = y + self.sensorNode[j][1]
            self.center[i] = [ x / len( self.charger[i] ), y / len( self.charger[i] ) ]
            
    def run( self, itera ):
        i = itera
        tempRadius = self.radius
        while i != 0:
            if i == itera:
                self.radius = tempRadius
            else:
                self.radius = tempRadius
            self.cluster()
            self.newKernel()
            i = i - 1

        return self.center
        