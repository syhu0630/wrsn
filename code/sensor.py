'''
  * @file sensor.py
  * @brief find charger candidate node.

  * method
     + twoInsec
     + threeInsec
     + distance
     + findNeighbor
     + findCandidate
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/07/05 
'''

import math
import numpy as np

class Sensor:
    
    def __init__( self, radius = 0, sensorNode = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.dist = []
        self.neighbor = []
        self.candidate = []
        self.finalcandidate = []
        
    def twoInsec( self, p1 ,r1 ,p2 ,r2 ):
        x = p1[0]
        y = p1[1]
        R = r1
        a = p2[0]
        b = p2[1]
        S = r2
        d = math.sqrt((abs(a-x))**2 + (abs(b-y))**2)
        if d > (R+S) or d < (abs(R-S)):
            print ("Two circles have no intersection")
            return 
        elif d == 0 and R==S :
            print ("Two circles have same center!")
            return
        else:
            A = (R**2 - S**2 + d**2) / (2 * d)
            h = math.sqrt(R**2 - A**2)
            x2 = x + A * (a-x)/d
            y2 = y + A * (b-y)/d
            x3 = round(x2 - h * (b - y) / d,2)
            y3 = round(y2 + h * (a - x) / d,2)
            x4 = round(x2 + h * (b - y) / d,2)
            y4 = round(y2 - h * (a - x) / d,2)
            #print (x3, y3)
            #print (x4, y4)
            c1 = np.array([x3, y3])
            c2 = np.array([x4, y4])
            return c1,c2
        
    def threeInsec( self, p1, r1 ,p2 ,r2 ,p3 ,r3 ):
        x = p2[0]
        y = p2[1]
        a = p3[0]
        b = p3[1]
        d = math.sqrt((abs(a-x))**2 + (abs(b-y))**2)
        if d < r3*2:
            C = self.twoInsec(p1,r1,p2,r2)
            D = self.twoInsec(p1,r1,p3,r3)
            E = self.twoInsec(p2,r2,p3,r3)
            if((C[0][0]-p3[0])**2 + (C[0][1]-p3[1])**2 < 25):
                A = C[0]
            else:
                A = C[1]
    
            if((D[0][0]-p2[0])**2 + (D[0][1]-p2[1])**2 < 25):
                B = D[0]
            else:
                B = D[1]
    
            if((E[0][0]-p1[0])**2 + (E[0][1]-p1[1])**2 < 25):
                J = E[0]
            else:
                J = E[1]
            CR = [round((A[0]+B[0]+J[0])/3,2),round((A[1]+B[1]+J[1])/3,2)] 
            return CR
        
    def distance( self ):
        for i in range(len( self.sensorNode )):
            temp = []
            for j in range(len( self.sensorNode )):
                if i == j:
                    temp.append(0)
                else:
                    temp.append(round(math.sqrt((self.sensorNode[j][0] - self.sensorNode[i][0]) * (self.sensorNode[j][0] - self.sensorNode[i][0]) 
                    + (self.sensorNode[j][1] - self.sensorNode[i][1]) * (self.sensorNode[j][1] - self.sensorNode[i][1])),2))
            self.dist.append(temp)
    
    def findNeighbor( self ):
        for i in range(len( self.sensorNode )):
            temp = []
            for j in range(len( self.sensorNode )):
                if self.dist[i][j] < self.radius*2 and self.dist[i][j] != 0:
                    temp.append(j)
            self.neighbor.append(temp)     
    
    def findCandidate( self ):            
        for i in range(len( self.sensorNode )):
            if len( self.neighbor[i] ) == 0:
                self.candidate.append(self.sensorNode[i])
            for j in range(len( self.neighbor[i]) ):
                p = self.twoInsec( self.sensorNode[i], self.radius, self.sensorNode[self.neighbor[i][j]], self.radius )
                centroid = [round((p[0][0]+p[1][0])/2,2), round((p[0][1]+p[1][1])/2,2)]
                self.candidate.append(centroid)
           
        for i in range(len( self.sensorNode )):
            for j in range(len( self.neighbor[i] ) - 1 ):
                p = self.threeInsec( self.sensorNode[i], self.radius, self.sensorNode[self.neighbor[i][j]], self.radius, self.sensorNode[self.neighbor[i][j+1]], self.radius )
                if p:
                    self.candidate.append(p)
    
    def run( self ):
        self.distance()
        self.findNeighbor()
        self.findCandidate()
        self.finalcandidate = list(set(map( tuple, self.candidate )))
        
        return self.finalcandidate
    
