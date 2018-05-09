# http://www.codehamster.com/2015/03/18/use-the-np-array-argsort-and-list-sort-to-get-the-rank-of-the-number/
# http://glowingpython.blogspot.com/2012/04/k-nearest-neighbor-search.html
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import NearestNeighbors

N=50
dim=3
X = np.random.random((N,dim))
diff = X.reshape(N,1,dim)-X
D = (diff**2).sum(axis=-1)
# print D.shape
i = np.arange(N)
D[i,i]=np.inf
# this only get the nearest neighbor
nni = D.argmin(axis=-1)
# this will return all the nearest neighbors matrix (nnm)
nnm = D.argsort(axis=-1)

p = N/2
k = 8
print nnm[p,:k]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xt = X[:,0]
yt = X[:,1]
zt = X[:,2]
ax.scatter(xt, yt, zt, c='b', marker='o')
xk = X[nnm[p,:k],0]
yk = X[nnm[p,:k],1]
zk = X[nnm[p,:k],2]
# https://www.getdatajoy.com/examples/python-plots/3d-scatter-plot
ax.scatter(xk, yk, zk, c='r', marker='o', s=60)
xp = X[p,0]
yp = X[p,1]
zp = X[p,2]
ax.scatter(xp, yp, zp, c='g', marker='8', s=90)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()

# d, i = NearestNeighbors().fit(X).kneighbors(X,2)
# print(i[:10,1])

