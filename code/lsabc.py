'''
  * @file lsabc.py
  * @brief use layoffs simulated annealing method to find final charger placement.

  * method
     + transition
     + evaluation
     + determination
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/07/09 
'''

import random
import math
from greedy import Greedy

class Lsabc(Greedy):
    
    def __init__( self, radius = 0, sensorNode = [], candidate = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.candidate = candidate
        self.sensorNodeBool = []                                 #sensor node be covered or not
        for i in range( len( self.sensorNode ) ):
            self.sensorNodeBool.append( 1 ) 
        self.candidateStatus = self.renewStatus()                #candidate cover sensor node 
        self.sensorbeCover = []                                  #sensor node be covered the number of charger 
        for i in range( len( self.sensorNode ) ):
            self.sensorbeCover.append( 0 )
        for i in self.candidateStatus:
            for j in i:
                self.sensorbeCover[j] = self.sensorbeCover[j] + 1
        #print( self.sensorbeCover )
        self.chargerList = []                                   #charger be place or not
        for i in range( len( self.candidate ) ):
            self.chargerList.append( 1 )
        
    def transition( self ):
        r = random.randint(0, len( self.chargerList ) - 1 )
        while self.chargerList[r] == 0:
            r = random.randint(0, len( self.chargerList ) - 1 )
        self.chargerList[r] = 0
        return r
        
    def evaluation( self, r ):
        overLapping = 0
        for i in self.candidateStatus[r]:
            self.sensorbeCover[i] = self.sensorbeCover[i] - 1
        #print( self.sensorbeCover )
        if 0 not in self.sensorbeCover:
            for j in self.sensorbeCover:
                if j > 1:
                    overLapping = overLapping + 1
        return overLapping
        
    def determination( self, overLapping ):
        fitness = 0
        if overLapping != 0:
            fitness = 1 / overLapping
        return fitness
        
    def run( self, itera ):
        best = 0
        temperature = 100
        i = itera
        answer = []
        while i != 0:
            pa = 0
            r = random.random()
            index = self.transition()
            overLapping = self.evaluation( index )
            #print( overLapping )
            fitness = self.determination( overLapping )
            #print( fitness )
            if fitness != 0:
                pa = math.exp( ( best - fitness ) / temperature )
            if fitness < best and pa < r:
                for j in self.candidateStatus[index]:
                    self.sensorbeCover[j] = self.sensorbeCover[j] + 1
                self.chargerList[index] = 1
            else:
                best = fitness               
                
            temperature = temperature * 0.99
            i = i - 1
        for j in range( len( self.chargerList ) ):
            if self.chargerList[j] == 1:
                answer.append( self.candidate[j] )                 
        return answer
