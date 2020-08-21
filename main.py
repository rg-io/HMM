#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:02:49 2020

@author: ataraxis
"""

from scipy.io import loadmat as load
import numpy as np
from flat_start import flat_start
from phn_o_const import phn_o_const
from train_model import train_model

c0 = load('c0_coded_sep_lrg_nrm.mat')
c0_obs = c0['c0_new'] #c0_obs is a 1 x 10 matrix

q = 4 #number of states
utter = 0

maxiter = 15
N = 4
M = 32
	
A = np.zeros((N,N), dtype = np.double)
B = np.zeros((N,M), dtype = np.double)
P = np.ones((N,1), dtype = np.double)	
	
P = P/sum(P)
log_lh_arr = []
A_big = {}
B_big = {}

for i in range(0, N-1):
	A[i,i] = 0.5
	A[i,i+1] =0.5
	
for i in range(0, q):
    A_big[i] = A
	
for i in range(0, N):
    for j in range(0, M):
        B[i,j] = 1/M

for i in range(0, M):
    B[N-1, i] = 0

for i in range(0, q):
        B_big[i] = B
    

phn_sgmt = flat_start(c0_obs, q) #function call


phn_sgmt_mat = np.zeros((10,q), dtype = object)
for i in range(0, 10):
     for j in range(0, q):
         phn_sgmt_mat[i,j] = phn_sgmt[i,j]
# Had to make phn_sgmt_mat to mimic the cells in matlab

    
#train

lh_arr = np.zeros((q, 1)) #4 X 1 matrix
lh_mat = np.zeros((maxiter, q)) #15 X 4 matrix
phn_O = np.zeros((1), dtype = object)
A_new = np.zeros((N,N), dtype = np.double)
B_new = np.zeros((N,M), dtype = np.double)
P_new = np.ones((N,1), dtype = np.double)
log_lh = 0

for i in range(0, maxiter):
    for j in range(0, q):
        phn_O = phn_o_const(phn_sgmt_mat, j)
        #print(30081995)
        A_new, B_new, P_new, log_lh = train_model(phn_O,A_big[j],B_big[j], P)
        A_new
