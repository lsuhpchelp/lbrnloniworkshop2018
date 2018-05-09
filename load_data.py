#!/usr/bin/env python
import numpy as np
#a= np.loadtxt('data.txt',skiprows=33,dtype=np.float64,comments = '#')
a= np.loadtxt('data.txt',skiprows=16,dtype=np.float64,usecols=(0,1,2),comments = '#')
print a
