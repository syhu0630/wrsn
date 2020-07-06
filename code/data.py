'''
  * @file data.py
  * @brief create and read sensor node.

  * method
     + createSensor
     + readSensor

  * @author Shiang-Yu Hu 
  * @date 2019/07/05 
'''

import random

class Data:

    def __init__( self, sensorNumber = 0 ):
        self.sensorNumber = sensorNumber
        self.sensorNode = []

    def createSensor( self ):
        f = open( "data/node.txt", "w" )
        for i in range( self.sensorNumber ):
            f.write( str( i ) + " " +str( random.randint( 0, 2000) ) + " " + str(random.randint( 0, 1500) ) + "\n" )
        f.close()

    def readSensor( self ):
        f = open( "data/node.txt", "r" )
        for x in f:
            self.sensorNode.append([ int(x.split(" ")[1] ), int(x.split(" ")[2]) ] )
        f.close()
        return self.sensorNode