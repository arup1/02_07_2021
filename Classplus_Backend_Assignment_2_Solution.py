# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 20:32:46 2021

@author: arupb
"""
def count_of_epicentres(n,h,x,hotspots_list,roads):
    #Creating a level one hash_map of all interconnected-cities
    all_conn = {i+1:{1:set()} for i in range(n)}
    for u,v in roads:
        all_conn[u][1].add(v)
        all_conn[v][1].add(u)
    
    #Initially assuming all cities can be epicentres
    epicentres = set(range(1,n+1))
    
    #Expanding the interconnected-cities hash_map for all hotspots to level x
    for hotspot in hotspots_list:
        temp_set = all_conn[hotspot][1]
        
        for i in range(2, x+1):
            all_conn[hotspot].setdefault(i, set())
            for prev_root in all_conn[hotspot][i-1]:
                all_conn[hotspot][i].update(all_conn[prev_root][1]) 
            temp_set.update(all_conn[hotspot][i])
        
        #removing out of range cities by comparing with i'th hotspot's in-range cities
        epicentres = epicentres.intersection(temp_set)

    return len(epicentres)

if __name__=='__main__':
    #Reading Inputs
    parser = lambda x: list(map(int, x.split()))
    n, h, x = parser(input()) #5,2,2
    hotspots_list = parser(input()) #[2,5]
    roads = [parser(input()) for _ in range(n-1)] #[[1,2],[2,3],[2,4],[4,5]]
    
    print('No. of epicentre= ', count_of_epicentres(n,h,x,hotspots_list,roads))
