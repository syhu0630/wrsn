'''
  * @file sa.py
  * @brief use simulated annealing method to find final charger placement.

  * method
     + addTransition
     + replaceTransition
     + evaluation
     + determination
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/07/08 
'''

import random
from greedy import Greedy

class Sa(Greedy):
    
    def __init__( self, radius = 0, sensorNode = [], candidate = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.candidate = candidate
        self.sensorNodeBool = []                                 #sensor node be covered or not
        for i in range( len( self.sensorNode ) ):
            self.sensorNodeBool.append( 1 )                              
        self.candidateStatus = self.renewStatus()                #candidate cover sensor node 
        self.candidateSensornumber = self.renewSensornumber()    #candidate cover sensor node number
        self.initNumber = int( len( self.sensorNode ) / max( self.candidateSensornumber ) )
        #self.candidateList = greedyfinal
        self.candidateList = random.sample( self.candidate, self.initNumber )
        #print( self.candidateList )
        #print( self.initNumber )
        self.best = []
        self.bestSensor = 0
        self.sensorCover = []
        for i in range( len( self.sensorNode ) ):
            self.sensorCover.append( 0 )
    def addTransition( self, charger ):
        self.candidateList.append( charger )
    
    def replaceTransition( self, charger ):
        #print( len( self.candidateList ) )
        r = random.randint(0, len( self.candidateList ) - 1 )
        self.candidateList[r] = charger
    
    def evaluation( self ):
        for i in range( len( self.sensorNode ) ):
            self.sensorCover[i] =  0 
        #print( self.candidateStatus )
        for i in self.candidateList:
            #print( self.candidateStatus[ self.candidate.index( i ) ] )
            for j in self.candidateStatus[ self.candidate.index( i ) ]:
                self.sensorCover[j] = 1

    def determination( self, best, sensorCover ):
        flag = 0
        sensor = 0
        for i in sensorCover:
            if i == 1:
                sensor = sensor + 1
        if self.bestSensor < sensor :
            self.best = self.candidateList.copy()
            self.bestSensor = sensor
            flag = 1
            return self.candidateList, sensor, flag
            '''
            if len( best ) >= len( self.candidateList ):
                self.best = self.candidateList.copy()
                self.bestSensor = sensor
                flag = 1
                return self.candidateList, sensor, flag
            else:
                self.best = self.candidateList.copy()
                self.bestSensor = sensor
                flag = 1
                return self.candidateList, sensor, flag
            '''
        else:
            self.candidateList = self.best.copy()
            flag = 0
            return self.candidateList, self.bestSensor, flag

    
    def run( self, itera ):
        A = 0.01
        flag = 0
        i = itera
        self.evaluation()
        self.best = self.candidateList.copy()
        #print( self.best )
        for j in self.sensorCover:
            if j == 1:
                self.bestSensor = self.bestSensor + 1        
        while i != 0:
            T = random.random()                  
            charger = random.choice( self.candidate )
            while charger in self.candidateList:
                charger = random.choice( self.candidate )

            if A > T:
                self.addTransition( charger )
            else:
                self.replaceTransition( charger )
                
            self.evaluation()
            self.candidateList, sensor, flag = self.determination(  self.best, self.sensorCover )
            if flag == 0:
                A = A + ( 1 / i )
                #A = 0
            i = i - 1
        return self.best
