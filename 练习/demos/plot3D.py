import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

np.random.seed(1)
def circle(center, R):
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = R * np.outer(np.cos(u), np.sin(v)) + mean_x
    y = R * np.outer(np.sin(u), np.sin(v)) + mean_y
    z = R * np.outer(np.ones(np.size(u)), np.cos(v)) + mean_z
    return x, y, z

data = np.random.randn(100,3)
# print(data.shape)
x, y, z = data[:,0], data[:,1], data[:,2]
mean_x, mean_y, mean_z = np.mean(x), np.mean(y), np.mean(z)
center = [mean_x, mean_y, mean_z]
# print(y.shape)
fig = plt.figure()
ax = Axes3D(fig)
#画数据点
ax.scatter3D(x, y ,z, c = 'b', marker = '+')
ax.scatter3D(mean_x, mean_y, mean_z, c='r', marker = '+')
#画最小包围球
R = 3.5
xc, yc, zc = circle(center, R)
ax.plot_surface(xc, yc, zc,  rstride=4, cstride=4,alpha = 0.5)
#画R+epsilon
epsilon = 1.0
x_plus, y_plusm, z_plus = circle(center, R = R + epsilon)
ax.plot_surface(x_plus, y_plusm,z_plus,  rstride=4, cstride=4,alpha = 0.3)
#画R-epsilon
epsilon = 1.0
x_r, y_r, z_r = circle(center, R = R - epsilon)
ax.plot_surface(x_r, y_r,z_r,  rstride=4, cstride=4,alpha = 0.4)
#画采样数据点


plt.show()
