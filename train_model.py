#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:28:28 2020

@author: ataraxis
"""
from forward import fwdfun
#from backward import backfun
import numpy as np

def train_model(O, A, B, Pt):
    E = len(O) #10 #O is phn_O an array 
    N = len (A)
    alpha_hat = np.zeros((E, N), dtype = np.double)
    scale_new = np.zeros((E,1), dtype = np.double)
    M = 32
    denom_A_arr = np.zeros((N,1), dtype = np.double)
    numer_A_arr = np.zeros((N,N), dtype = np.double)
    denom_B_arr = np.zeros((N,1), dtype = np.double)
    numer_B_arr = np.zeros((N,M), dtype = np.double)
    gamma_1_arr = np.zeros((N,1), dtype = np.double)
    log_lh = 0
    
    A_new = np.zeros((N,N), dtype = np.double)
    B_new = np.zeros((N,M), dtype = np.double)
    
    for i in range(0, E):
        obs = O[i]
        alpha_hat, scale_new = fwdfun(obs, A, B, Pt)
        
        
    