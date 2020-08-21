#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:02:49 2020

@author: ataraxis
"""
import math

#flat_start(C0_obs, q)
def flat_start(temp, q): #temp is a 1 x 10 matrix
    phn_sgmt = {}
    E = len(temp[0]) # this is the number of columns in c0_obs
    #print(E)

    for i in range(0, E):
        obs = temp[0, i] #accessing each col of the temp matrix
        #print(len(obs))
        T = len(obs)
        
        K = math.floor(T/q)
        #print('T: {}, K: {}'.format(T, K))
        for j in range(0, q):
            strt = K * j + 1
            fin = strt + K - 1
            if j == q:
                if fin < T:
                    fin  = T
            #print("strt = {}, fin = {}".format(strt, fin))
            phn_sgmt[i,j] = obs[strt:(fin+1)]
    #print(obs[strt:fin, 0])
    #print(phn_sgmt)
    return(phn_sgmt)
            
                    
                
        
	
        
    
