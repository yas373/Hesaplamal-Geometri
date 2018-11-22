
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt

def my_draw_a_vector_from_origin(v):
    plt.axes().set_aspect('equal')
    x=[0,v[0]]
    y=[0,v[1]]
    plt.xlim(-10,15) #sınır değerler
    plt.ylim(-10,15)
    plt.plot(x,y)


def my_draw_a_vector_from_v_to_w(v,w):
    x=[v[0],w[0]]
    y=[v[1],w[1]]
    plt.xlim(-10,15) 
    plt.ylim(-10,15) 
    plt.plot(x,y)

def my_scalar_product(a,b):
    return (a[0]*b[0]+a[1]*b[1])


def distance(v,w):
    return (((v[0]-w[0])**2) + ((v[1]-w[1])**2))**.5

def my_vector_add(v,w):
    return [v[0]+w[0],v[1]+w[1]]

def my_vector_substract(v,w):
    return [v[0]-w[0],v[1]-w[1]]

def my_vector_multiply_with_scalar(c,v):
    return [c*v[0],c*v[1]]

