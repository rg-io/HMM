#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 21:53:32 2020

@author: ataraxis
"""

import numpy as np

def backfun(obs, A, B, P, scale_new):
    N = len(A)
    T = len(obs)
    beta = np.zeros((N,T), dtype = np.double)
    beta_hat = beta
    beta[N-1,T-1] =1
    
    for i in range(0, N-1):
        beta[i, T-1] = A[i, N-1]
        
    for i in range(0, T):
        beta_hat[i, T-1] = beta[i, T-1]
        for t in range 