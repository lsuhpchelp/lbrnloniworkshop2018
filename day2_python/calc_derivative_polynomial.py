from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title

# calculate the x^2 function on evenly spaced data.
x = linspace(0,2.0,101)
y = x**2

dy=y[1:]-y[:-1]
dx=x[1:]-x[:-1]

dy_dx = dy/dx
cx = 0.5*(x[1:]+x[:-1])

dy_by_2=0.5*(y[1:]+y[:-1])

area = cumsum(dx*dy_by_2)
analytical = x**3/3.0

# print "area=", area

subplot(1,2,1)
plot(x,y)
plot(cx,dy_dx,'xr')
plot(x,2*x,'og')
subplot(1,2,2)
plot(cx,area,'xr')
plot(x,analytical)
show()
