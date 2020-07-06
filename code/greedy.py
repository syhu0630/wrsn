'''
  * @file greedy.py
  * @brief use greedy method to find final charger placement.

  * method
     + renewStatus
     + renewSensornumber
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/07/05 
'''

import math

class Greedy:
    
    def __init__( self, radius = 0, sensorNode = [], candidate = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.candidate = candidate
        self.sensorNodeBool = []           #sensor node be covered or not
        self.candidateStatus = []          #candidate cover sensor node 
        self.candidateSensornumber = []    #candidate cover sensor node number
        
    def renewStatus( self ):
        candidate_temp = []
        for i in range(len( self.candidate )):
            temp = []
            for j in range(len( self.sensorNode )):
                d = round(math.sqrt((self.candidate[i][0] - self.sensorNode[j][0]) * (self.candidate[i][0] - self.sensorNode[j][0])
                + (self.candidate[i][1] - self.sensorNode[j][1]) * (self.candidate[i][1] - self.sensorNode[j][1])), 2 )
                if d < self.radius and self.sensorNodeBool[j] == 1:
                    temp.append(j)
            candidate_temp.append(temp)
            #print(len(candidate_temp))
        return candidate_temp
        
    def renewSensornumber( self ):
        candidatenum_temp = []
        for i in range(len( self.candidate )):
            candidatenum_temp.append(len( self.candidateStatus[i] ))
        #print(candidatenum_temp)
        return candidatenum_temp
        
    def run( self ):
        final = []
        for i in range(len( self.sensorNode )):
            self.sensorNodeBool.append( 1 )
        self.candidateStatus = self.renewStatus()
        self.candidateSensornumber = self.renewSensornumber()
        while any( self.candidateSensornumber ):
            for i in range(len( self.candidateSensornumber )):
                if self.candidateSensornumber[i] == max( self.candidateSensornumber ) and self.candidateSensornumber[i] != 0:
                    for j in range(len( self.candidateStatus[i] )):
                        #print(candidate_status[i][j])
                        self.sensorNodeBool[ self.candidateStatus[i][j] ] = 0
                    final.append(self.candidate[i])
                    #print(candidate_set[i])
                    break
            #print(node_bool)
            self.candidateStatus = self.renewStatus()
            self.candidateSensornumber = self.renewSensornumber()
        
        return final