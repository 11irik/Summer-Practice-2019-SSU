from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt




x = np.linspace(-3, 3)
y = np.linspace(-3, 3)
x, y = np.meshgrid(x, y)
z = x + np.cos(x * y)

plt.contourf(x, y, z)
plt.savefig('contour.png')
plt.show()

fig = plt.figure()
ax = fig.gca(projection="3d")
surf = ax.plot_surface(x, y, z)

plt.savefig('graph.png')
plt.show()
