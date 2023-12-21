from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

A = np.arange(-1.5, 1.5, 0.01)
B = np.arange(-1.5, 1.5, 0.01)
A, B = np.meshgrid(A, B)
R = (A**2-B**2+1)**2 + (2*A*B)**2
Z = np.sqrt(R)

surf = ax.plot_surface(A, B, Z, cmap=cm.autumn,
                       linewidth=0, antialiased=False)

ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()