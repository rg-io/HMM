#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 19:01:52 2020

@author: ataraxis
"""

import numpy as np


def fwdfun(obs, A, B, Pt):
    N = len(A) #here A will be a dictionary with transition probabilities
    T = len(obs) #here T is the time 
    alpha = np.zeros((N,T), dtype = np.double)
    alpha_hat = alpha
    scale = np.zeros((T,1), dtype = np.double)
    
    for i in range(0, N):
        alpha[i, 0] = Pt[i] * B[i, obs]
