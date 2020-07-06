# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 14:51:55 2019

@author: Frank
"""
import math

class test():
    def __init__(self):
        self.x = [0, 0, 1]
        self.z = [1, 2, 3]
        self.y = self.x.copy()
    def run(self):
        #self.x[1] = 5
        #print(self.y)
        l = 0.328
        ptgt = 3
        gr = 3.98
        pi = 3.14
        pr = round( ptgt * gr * ( l / ( 4 * pi * 4 ) ) * ( l / ( 4 * pi * 4 ) ) * 1000, 3 )
        r = round( math.sqrt( pow( 2.3, 2 ) + pow( 1.33, 2 ) ), 2 )
        #print( r )
        
        a = self.x[0:1]+self.z[1:1]+self.x[1:3]
        print(a)
test = test()
test.run()