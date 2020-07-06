'''
  * @file picture.py
  * @brief draw charger cover sensor node.

  * method
     + draw

  * @author Shiang-Yu Hu 
  * @date 2019/07/05 
'''

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class Picture:
    
    def __init__( self, radius = 0, sensorNode = [], final = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.final = final
        
    def draw( self ):
        fig, ax = plt.subplots()
        for i in range(len( self.sensorNode )):
            plt.scatter( self.sensorNode[i][0], self.sensorNode[i][1], facecolors='none' ,edgecolors='k')
        for i in range(len( self.final )):
            circle = Circle(( self.final[i][0], self.final[i][1]), radius = self.radius, fc='none', ec='r')
            ax.add_artist(circle)
            #plt.scatter(candidate_set[i][0], candidate_set[i][1])
        plt.show()