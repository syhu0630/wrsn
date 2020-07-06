'''
  * @file nsga.py
  * @brief use Non-dominated Sorting Genetic Algorithm-II method to find final charger placement.

  * method
     + initialize
     + crossover
     + mutation
     + index_of
     + sort_by_values
     + fast_non_dominated_sort
     + crowding_distance
     + fitnessCharger
     + fitnessCover
     + fitnessEnergy
     + evlaution
     + run

  * @author Shiang-Yu Hu 
  * @date 2019/09/24
'''

import random
import math
from greedy import Greedy
from energy import Energy

class Nsga(Greedy):
        
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
            
    def initialize( self, population, chromosome = [] ): 
        for i in range( population ):
            temp = []
            for j in range( len( self.candidate ) ):
                temp.append( random.randint( 0, 1 ) )
            chromosome.append( temp )
        return chromosome
        
    def crossover( self, a, b ):
        pointA =  random.randint( 0, len( self.candidate ) - 1 )
        pointB =  random.randint( 0, len( self.candidate ) - 1 )
        if pointA < pointB:
            c = a[ 0 : pointA ] + b[ pointA : pointB ] + a[ pointB : len( self.candidate ) ]
            d = b[ 0 : pointA ] + a[ pointA : pointB ] + b[ pointB : len( self.candidate ) ]
        else:
            c = a[ 0 : pointB ] + b[ pointB : pointA ] + a[ pointA : len( self.candidate ) ]
            d = b[ 0 : pointB ] + a[ pointB : pointA ] + b[ pointA : len( self.candidate ) ]
        return c, d
          
    def mutation( self, a, mutatRate ): 
        r = random.random()
        if r <= mutatRate:
            point =  random.randint( 0, len( self.candidate ) - 1 )
            if a[point] == 0:
                a[point] = 1
            else:
                a[point] = 0
        return a

    def index_of( self, a, list1 ):
        for i in range(0, len(list1)):
            if list1[i] == a:
                return i
        return -1

    def sort_by_values( self, list1, values ):
        sorted_list = []
        while(len(sorted_list)!=len(list1)):
            if self.index_of(min(values),values) in list1:
                sorted_list.append(self.index_of(min(values),values))
            values[self.index_of(min(values),values)] = math.inf
        return sorted_list

    def fast_non_dominated_sort( self, values1, values2, values3 ):
        S=[[] for i in range(0,len(values1))]
        front = [[]]
        n=[0 for i in range(0,len(values1))]
        rank = [0 for i in range(0, len(values1))]
    
        for p in range(0,len(values1)):
            S[p]=[]
            n[p]=0
            '''
            for q in range(0, len(values1)):
                if (values1[p] < values1[q] and values2[p] > values2[q] and values3[p] > values3[q]) or (values1[p] < values1[q] and values2[p] > values2[q] and values3[p] >= values3[q])\
                or (values1[p] < values1[q] and values2[p] >= values2[q] and values3[p] >= values3[q]) or (values1[p] < values1[q] and values2[p] >= values2[q] and values3[p] > values3[q])\
                or (values1[p] <= values1[q] and values2[p] >= values2[q] and values3[p] > values3[q]) or (values1[p] <= values1[q] and values2[p] > values2[q] and values3[p] >= values3[q])\
                or (values1[p] <= values1[q] and values2[p] > values2[q] and values3[p] > values3[q]):
                    if q not in S[p]:
                        S[p].append(q)
                elif (values1[q] < values1[p] and values2[q] > values2[p] and values3[q] > values3[p]) or (values1[q] < values1[p] and values2[q] > values2[p] and values3[q] >= values3[p])\
                or (values1[q] < values1[p] and values2[q] >= values2[p] and values3[q] >= values3[p]) or (values1[q] < values1[p] and values2[q] >= values2[p] and values3[q] > values3[p])\
                or (values1[q] <= values1[p] and values2[q] >= values2[p] and values3[q] > values3[p]) or (values1[q] <= values1[p] and values2[q] > values2[p] and values3[q] >= values3[p])\
                or (values1[q] <= values1[p] and values2[q] > values2[p] and values3[q] > values3[p]):
                    n[p] = n[p] + 1
            '''  
            '''
            for q in range(0, len(values1)):
                if (values1[p] < values1[q] and values2[p] > values2[q]) or (values1[p] <= values1[q] and values2[p] > values2[q]) or (values1[p] < values1[q] and values2[p] >= values2[q]):
                    if q not in S[p]:
                        S[p].append(q)
                elif (values1[q] < values1[p] and values2[q] > values2[p]) or (values1[q] <= values1[p] and values2[q] > values2[p]) or (values1[q] < values1[p] and values2[q] >= values2[p]):
                    n[p] = n[p] + 1
            if n[p]==0:
                rank[p] = 0
                if p not in front[0]:
                    front[0].append(p)
            '''
            for q in range(0, len(values1)):
                if values2[p] > values2[q]:
                    if q not in S[p]:
                        S[p].append(q)
                elif values2[p] == values2[q]:
                    if values1[p] < values1[q]:
                        if q not in S[p]:
                            S[p].append(q)
                    elif values1[p] == values1[q]:
                        if values3[p] > values3[q]:
                            if q not in S[p]:
                                S[p].append(q)
                    else:
                        n[p] = n[p] + 1
                        
                else:
                    n[p] = n[p] + 1
            if n[p]==0:
                rank[p] = 0
                if p not in front[0]:
                    front[0].append(p)
        i = 0
        while(front[i] != []):
            Q=[]
            for p in front[i]:
                for q in S[p]:
                    n[q] =n[q] - 1
                    if( n[q]==0):
                        rank[q]=i+1
                        if q not in Q:
                            Q.append(q)
            i = i+1
            front.append(Q)
    
        del front[len(front)-1]
        #print( front )
        return front

    def crowding_distance( self, values1, values2, values3, front ):
        distance = [0 for i in range(0,len(front))]
        sorted1 = self.sort_by_values(front, values1[:])
        sorted2 = self.sort_by_values(front, values2[:])
        sorted3 = self.sort_by_values(front, values3[:])
        distance[0] = 99999999999999
        distance[len(front) - 1] = 8888888888888
        for k in range(1,len(front)-1):
            if (max(values1)-min(values1)) != 0:
                distance[k] = distance[k] + (values1[sorted1[k+1]] - values2[sorted1[k-1]])/(max(values1)-min(values1))
        for k in range(1,len(front)-1):
            if (max(values2)-min(values2)) != 0:
                distance[k] = distance[k] + (values2[sorted2[k+1]] - values2[sorted2[k-1]])/(max(values2)-min(values2))
        for k in range(1,len(front)-1):
            if (max(values3)-min(values3)) != 0:
                distance[k] = distance[k] + (values3[sorted3[k+1]] - values3[sorted3[k-1]])/(max(values3)-min(values3))
        return distance   

    def selection( self ):   
        
        return 0 
    
    def fitnessCharger( self, a ):
        number = 0
        for i in range( len( a ) ):
            if a[i] == 1:
                number = number + 1  
        return number
    
    def fitnessCover( self, a ):
        sensorCover = 0
        temp = []
        for i in range( len( a ) ):
            if a[i] == 1:
                temp.append( self.candidate[i] ) 
        cover = []
        for i in range( len( self.sensorNode ) ):
            cover.append( 0 )
        for i in temp:
            #print( self.candidateStatus[ self.candidate.index( i ) ] )
            for j in self.candidateStatus[ self.candidate.index( i ) ]:
                cover[j] = 1
        for i in cover:
            if i == 1:
                sensorCover = sensorCover + 1
        return round( sensorCover / len( self.sensorNode ), 2 )
    
    def fitnessEnergy( self, a ):
        temp = []
        for i in range( len( a ) ):
            if a[i] == 1:
                temp.append( self.candidate[i] ) 
        energy = Energy( self.radius, self.sensorNode, temp )
        return energy.run()
    
    def evlaution( self, chromosome = [] ):
        chargertemp = []
        covertemp = []
        energytemp = []
        for i in range( len( chromosome ) ):
            chargertemp.append( self.fitnessCharger( chromosome[i] ) )
            covertemp.append( self.fitnessCover( chromosome[i] ) )
            energytemp.append( self.fitnessEnergy( chromosome[i] ) )            
        #print( min(chargertemp) )
        #print( covertemp )
        #print( energytemp )
        return chargertemp, covertemp, energytemp
    
    def run( self, iteration, population, crossRate, mutatRate ):
        chromosome = []
        chargerfit = []
        coverfit = []
        energyfit = []
        final = []
        chromosome = self.initialize( population, chromosome)
        it = 0
        while it != iteration:
            offspring = []
            for i in range( 0, len( chromosome ), 2):
                r = random.random()
                x = random.randint(0, len(chromosome) - 1)
                y = random.randint(0, len(chromosome) - 1)
                if r <= crossRate:
                    a, b = self.crossover( chromosome[x], chromosome[y] )
                    offspring.append( self.mutation( a, mutatRate ) )
                    offspring.append( self.mutation( b, mutatRate ) )
                else:
                    offspring.append( chromosome[x] )
                    offspring.append( chromosome[y] )
            family = []
            family = chromosome + offspring
            chargerfit, coverfit, energyfit = self.evlaution( family )
            if it % 20 == 0:
                print( min(chargerfit) )
            front = self.fast_non_dominated_sort( chargerfit, coverfit, energyfit )
            #print( front )
            tempchromosome = []
            for i in range( len( front ) ):
                if len( front[i] ) + len( tempchromosome ) < population:
                    tempchromosome = tempchromosome + front[i]
                else:
                    distance = self.crowding_distance( chargerfit, coverfit, energyfit, front[i] )
                    distancetmp =  distance.copy()
                    distancetmp.sort(reverse=True)
                    #print(distancetmp)
                    for j in range( len(distancetmp) ):
                        tempchromosome.append( front[i][self.index_of(distancetmp[j],distance)] )
                        if len(tempchromosome) >= population:
                            break
                if len(tempchromosome) >= population:
                    break
            #print(tempchromosome)
            nextchromosome = []
            for i in tempchromosome:
                nextchromosome.append( family[i] )
            #print(nextchromosome)
            chromosome = nextchromosome  
            #print( len( chromosome ) )
            it = it + 1
            
        for i in range( len( chromosome ) ):
            temp = []
            for j in range( len( chromosome[i] ) ):
                if chromosome[i][j] == 1:
                    temp.append( self.candidate[j] )
            final.append( temp )
        return final
            #print( chromosome )