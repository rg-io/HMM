#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:01:52 2020

@author: ataraxis
"""

import numpy as np


def fwdfun(obs, A, B, Pt):
    N = len(A) #here A will be a dictionary with transition probabilities
    T = len(obs) #here T is the time #E 
    alpha = np.zeros((N,T), dtype = np.double)
    alpha_hat = alpha
    scale = np.zeros((T,1), dtype = np.double)
    
    for i in range(0, N):
        alpha[i, 0] = Pt[i] * B[i, obs[0,0]]
        
    val = 0
        
    for i in range(0, N):
        val += alpha[i,0]
    scale[0,0] = val
    
    if (scale[0,0] == 0):
        scale[0,0]  = 1

    for i in range(0, alpha.shape(0)):
        alpha_hat[i,0] =  alpha[i,0]/scale[0,0]
        
    for t in range(1, T):
        for j in range(0, N):
            temp = 0
            for i in range(0, N):
                if(j%4 ==0):
                    temp = temp + A[i,j]*alpha_hat[i,t]
                else:
                    temp = temp + A[i,j]*alpha_hat[i, t-i]*B[j, obs[t,0]]
            alpha[j,t] = temp
            alpha_hat[j,t] = temp
     
        scale[t, 0] = np.sum(alpha,0)[t]
        if (scale[t,0] == 0):
            scale[t,0] = 1
        for i in range(0, alpha.shape(0)):
            alpha_hat[i,t] =  alpha[i,t]/scale[t,0]
    lhood = np.sum(alpha, 0)[T-1]
    
    return (alpha_hat, scale, lhood)
        
        
    
    
    