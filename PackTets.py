
# coding: utf-8

# In[1]:

get_ipython().magic('matplotlib notebook')
import numpy as np
import mpl_toolkits.mplot3d as a3
import matplotlib.pyplot as plt


# In[2]:

from packtets import pack_tets
from packtets.geometry import Cell
L = .75; theta = np.pi/2
vx = L * np.array([1,0,0])
vy = L * np.array([np.cos(theta),np.sin(theta),0])
vz = L * np.array([np.cos(theta)*np.cos(theta),np.cos(theta)*np.sin(theta),np.sin(theta)])

#vx = L * np.array([1,1,0])
#vy = L * np.array([1,0,1])
#vz = L * np.array([0,1,1])
box = Cell(vx, vy, vz)
res = pack_tets(box, time_budget=60, verbose=True)


# In[3]:

import scipy as sp
ax = a3.Axes3D(plt.figure(10))

bounding = [box.vx, box.vy, box.vz]
for i,j in [(0,1), (0,2), (1,2)]:
    verts = [(0,0,0)]
    verts.append(bounding[i])
    verts.append(bounding[i]+bounding[j])
    verts.append(bounding[j])
    face = a3.art3d.Poly3DCollection([verts], alpha=0.1)
    face.set_facecolor('red')
    face.set_edgecolor('k')

    ax.add_collection3d(face)


for tet in res:
    syms = tet.get_symmetry(box.vx, box.vy, box.vz)
    for s in syms[0:1]:
        for x,y,z in [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]:
            verts = [tuple(s.verts[x]), tuple(s.verts[y]), tuple(s.verts[z])]
            tri = a3.art3d.Poly3DCollection([verts], alpha=0.2)
            tri.set_edgecolor('k')
            ax.add_collection3d(tri)
ax.set_xlim(0,L)
ax.set_ylim(0,L)
ax.set_zlim(0,L);

