#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:02:49 2020

@author: ataraxis
"""
import numpy as np

#q = 4
#phn_sgmt_mat = np.zeros((10,q), dtype = object)
phn_O = np.zeros((10), dtype = object)


def phn_o_const(phn_sgmt_mat, k):
    for i in range(10):
        phn_O[i] =  np.array(phn_sgmt_mat[i,k], dtype = object)
        
    return(phn_O)
            
    