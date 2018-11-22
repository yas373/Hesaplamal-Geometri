
# coding: utf-8

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

point1=np.array([0,0,0])
normal1=np.array([1,-2,1])

point2=np.array([0,-4,0])
normal2=np.array([0,2,-8])

point3=np.array([0,0,1])
normal3=np.array([-4,5,9])

point_test = np.array([1,-1,1])   
normal_test = np.array([1,-2,1])
np.sum(point_test*normal_test)

d1 = -np.sum(point1*normal1)
d2 = -np.sum(point2*normal2)
d3 = -np.sum(point3*normal3) 
d1,d2,d3


xx,yy=np.meshgrid(range(5),range(5))

xx 
yy

z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='red') 


point_test = np.array([1,-1,1])  
normal_test = np.array([1,-2,1])
np.sum(point_test*normal_test)


d1 = -np.sum(point1*normal1)
d2 = -np.sum(point2*normal2) 
d3 = -np.sum(point3*normal3) 


xx,yy=np.meshgrid(range(5),range(5))


z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]
get_ipython().magic('matplotlib inline')
plt3d = plt.figure().gca(projection='3d')
plt3d.plot_surface(xx,yy,z1,color='blue') 

#<sint,cost,t> 
n = 1000
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot a helix along the x-axis
theta_max = 8 * np.pi
theta = np.linspace(0, theta_max, n)
x = theta
z =  np.sin(theta)
y =  np.cos(theta)
ax.plot(x, y, z, 'b', lw=2)

ax.plot((-theta_max*0.2, theta_max * 1.2), (0,0), (0,0), color='k', lw=2)
ax.plot(x, y, 0, color='r', lw=1, alpha=0.5)
ax.plot(x, [0]*n, z, color='m', lw=1, alpha=0.5)

ax.set_axis_off()
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

n=1000
thete_max=0*np.pi
theta=np.linspace(0,theta_max,n)
x=np.sin(theta) 
y=np.cos(theta)
z=theta
ax.plot(x,y,z,'b',lw=2)

