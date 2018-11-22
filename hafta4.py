
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


plt.plot(1,12,'*')
plt.show()


point1 = np.array([0,0,0])
normal1 = np.array([1,-2,1])


point2 = np.array([0,-4,0])
normal2 = np.array([0,2,-8])

point3 = np.array([0,0,1])
normal3 = np.array([-4,5,9])


d1 = -np.sum(point1*normal1) # buradaki d 4x+5y+6z+7 = 0 örneğindeki 7 sayısıdır.
d2 = -np.sum(point2*normal2)
d3 = -np.sum(point3*normal3)


xx, yy = np.meshgrid(range(30), range(30)) 
z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().run_line_magic('matplotlib', 'inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1, color = 'yellow')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 1000
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
x = np.sin(theta)
y = np.cos(theta)
z = theta
ax.plot(x, y, z, 'b', lw=2)

