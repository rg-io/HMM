#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from math import log
def reestimate(obs, A, B, alpha_hat,beta_hat, scale):
    N = A.shape[0]
    T = obs.shape[0]
    M = 32
    #q = 4
    
    zeta = np.zeros((N, N, T), dtype = np.double)
    gamma= np.zeros((N,T), dtype = np.double)
   # A_new = np.zeros(np.size(A), dtype = np.double)
   # B_new = np.zeros(np.size(A), dtype = np.double)
   # P_new = np.zeros((N,1), dtype = np.double)
    
    denom_A = np.zeros((N,1), dtype = np.double)
    denom_B = np.zeros((N,1), dtype = np.double)
    numer_A = np.zeros((N,N), dtype = np.double)
    numer_B = np.zeros((N,M), dtype = np.double)
    
    for t in range(0, T-1):
        for i in range(0, N):
            for j in range(0, N):
                if (j%N == 0):
                    zeta[i,j,t] = alpha_hat[i,t]*A[i,j]*beta_hat[j,t+1]/scale[t+1,t]
                else:
                    zeta[i,j,t] =  alpha_hat[i,t]*A[i,j]*B[j, obs[t+1, 0]]*beta_hat[j, t+1]/scale[t+1, t] 
                
    for t in range(0, T):
        for i in range(0, N):
            gamma[i,t] =alpha_hat[i,t]*beta_hat[i,t]
            
    gamma_1 = np.zeros(gamma.shape(0), dtye = np.double)
    for i in range(0, N):
        gamma_1[i] = gamma[i,0]
        
    for i in range(0, N):
        for t in range(0, T-1):
            denom_A[i,1] = denom_A[i,1] + gamma[i,t]
    for j in range(0, N):
        for t in range(0, T-1):
            numer_A[i,j] = numer_A[i,j]+zeta[i,j,t]
            
    for i in range(0, N):
        for t in range(0, T):
            denom_B[i,0] = denom_B[i,0] + gamma[i,t]
    
    for j in range(0, M):
        for t in range(0, T):
            if(obs[t,0] == j):
                numer_B[i,j] = numer_B[i,j] + gamma[i,t]
    log_prob = -(sum(log(scale)))
    
    return(denom_A, numer_A, denom_B, numer_B, gamma_1, log_prob)
    