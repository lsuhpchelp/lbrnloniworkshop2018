"""
Calculate Derivative
--------------------
"""
import numpy as np
import matplotlib.pyplot as plt

# calculate the sin() function on evenly spaced data.
x = np.linspace(0,2*np.pi,101)
y = np.sin(x)

# use slicing to get dy and dx
dy=y[1:]-y[:-1]
dx=x[1:]-x[:-1]

dy_dx = dy/dx
cx = 0.5*(x[1:]+x[:-1])

dy_by_2=0.5*(y[1:]+y[:-1])

# note the trapezoid rule with cumsum
area = np.cumsum(dx*dy_by_2)
analytical = -np.cos(x) + np.cos(0)

# print "area=", area

plt.subplot(1,2,1)
plt.plot(x,y)
plt.plot(cx,dy_dx,'xr')
plt.plot(x,np.cos(x),'og')
plt.subplot(1,2,2)
plt.plot(cx,area,'xr')
plt.plot(x,analytical)
plt.show()
