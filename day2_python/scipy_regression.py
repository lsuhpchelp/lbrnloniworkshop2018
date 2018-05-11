#!/usr/bin/env python

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 5, 7, 10, 15])
y = np.array([2, 6, 7, 9, 14, 19])
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x,y,'or')
yh = x*slope + intercept
plt.plot(x, yh, '-b')
plt.show()