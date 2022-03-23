#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2022 Jongrae.K

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import numpy as np

Ns = 1000
eps = 1e-6

d_lb = 1e-3
d_ub = 10

d_ulb = d_ub - d_lb

omega = 0
Mjw = 1/(omega*1j + 2)

num_delta = 2

def A_delta(delta_1, delta_2):
    
    return -2+delta_1+np.sin(delta_1*delta_2)

while d_ulb > eps:
    
    d = (d_lb+d_ub)/2
    
    delta_1 = np.random.rand(Ns)*d-d/2
    delta_2 = np.random.rand(Ns)*d-d/2
    
    rand_face = np.random.randint(1,num_delta+1,Ns)
    delta_1[rand_face==0]=d/2
    delta_2[rand_face==1]=d/2
    
    Delta = A_delta(delta_1,delta_2)-A_delta(0,0)
    
    if np.unique(np.sign(np.real(1-Mjw*Delta))).size == 2:
        d_ub = d
    else:
        d_lb = d
        
    d_ulb = d_ub - d_lb
    

mu_lb = 2/d_ub
