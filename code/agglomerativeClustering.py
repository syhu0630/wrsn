# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:59:51 2019

@author: Frank
"""

from sklearn.cluster import AgglomerativeClustering
import numpy as np
import math

class AgglomerativeCluster():
    
    def __init__( self, radius = 0, sensorNode = [], candidate = [] ):
        self.radius = radius
        self.sensorNode = sensorNode
        self.candidate = candidate
        self.center = self.sensorNode.copy()
        self.charger = []
        for i in range( len( self.sensorNode ) ):
            temp = []
            self.charger.append( temp )      
            
    def run( self ):
        X = np.array( self.sensorNode )
        clustering = AgglomerativeClustering(n_clusters = None, distance_threshold = self.radius, linkage='complete' ).fit( X )
        
        print(clustering.labels_)
        