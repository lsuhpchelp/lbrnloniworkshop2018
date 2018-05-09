# find the k nearest neighbor

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

N=50
dim=2
# generate N random points in 2D
X = np.random.random((N,dim))
# find pairwise difference using broadcasting
diff = X.reshape(N,1,dim)-X
# Find pairwise differences using the aggregate function
D = (diff**2).sum(axis=2)
# set diagonal to infinity to skip self-neighbors
i = np.arange(N)
# using advanced (fancy) indexing
D[i,i]=np.inf
#print D
# this only get the nearest neighbor
nni = D.argmin(axis=1)
# this will return all the nearest neighbors matrix (nnm)
nnm = D.argsort(axis=1)

# plot all the random points
plt.plot(X[:,0],X[:,1],'ob')
# plot pth point in red
p = N/2
plt.plot(X[p,0],X[p,1],'or')
k = 5
#print nnm[p,:k]
# plot k neighbors in circles
plt.plot(X[nnm[p,:k],0],X[nnm[p,:k],1],'o',markerfacecolor='None',markersize=15,markeredgewidth=1)
# http://stackoverflow.com/questions/17990845/how-to-equalize-the-scales-of-x-axis-and-y-axis-in-python-matplotlib
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

# d, i = NearestNeighbors().fit(X).kneighbors(X,2)
# print(i[:10,1])

