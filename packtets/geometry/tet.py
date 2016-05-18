import numpy as np
from numpy.linalg import norm
from .collisions import *

class Tet():
    radius = np.sqrt(3./8.)
    inner_radius = np.sqrt(1./24.)
    center_verts = [
            np.array([ 1/2.,     0, -1./np.sqrt(8)]),
            np.array([-1/2.,     0, -1./np.sqrt(8)]),
            np.array([    0,  1/2.,  1./np.sqrt(8)]),
            np.array([    0, -1/2.,  1./np.sqrt(8)])]
    
    def __init__(self, center, theta, phi, psi):
        rotation = np.array([
            [np.cos(phi), -np.cos(psi)*np.sin(phi), np.sin(phi)*np.sin(psi)],
            [np.cos(theta)*np.sin(phi), 
             np.cos(theta)*np.cos(phi)*np.cos(psi) - np.sin(theta)*np.sin(psi), 
            -np.cos(psi)*np.sin(theta) - np.cos(theta)*np.cos(phi)*np.sin(psi)],
            [np.sin(theta)*np.sin(phi), 
             np.cos(theta)*np.sin(psi) + np.cos(phi)*np.cos(psi)*np.sin(theta), 
             np.cos(theta)*np.cos(psi)-np.cos(phi)*np.sin(theta)*np.sin(psi)]
            ])
        self.center = np.array(center)
        self.theta = theta
        self.phi = phi
        self.psi = psi
        self.verts = [np.dot(rotation, x) + self.center for x in self.center_verts]
        return

    def __repr__(self):
        return "Tet({}, {}, {}, {})".format(self.center, self.theta, self.phi, self.psi)
    
    def collision(self, other):
        dist = np.sum(np.square(self.center - other.center))
        if dist < np.square(2*self.inner_radius):
            return True
        if dist > np.square(2*self.radius):
            return False
        for i,j,k in [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]:
            for x,y,z in [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]:
                if collision_face([ self.verts[i],  self.verts[j],  self.verts[k]], 
                                  [other.verts[x], other.verts[y], other.verts[z]]):
                    return True
        return False
    
    def get_symetry_1d(self, v1):
        res = []
        if norm(v1) - np.dot(self.center, v1) / norm(v1) < 2*self.radius:
            res.append(Tet(self.center - v1, self.theta, self.phi, self.psi))
        if np.dot(self.center, v1) / norm(v1) < 2*self.radius:
            res.append(Tet(self.center + v1, self.theta, self.phi, self.psi))    
        return res
    
    def get_symetry(self, v1, v2, v3, include_self = True):
        syms = [self,] + self.get_symetry_1d(v1)
        for s in syms.copy():
            syms += s.get_symetry_1d(v2)
        for s in syms.copy():
            syms += s.get_symetry_1d(v3)
        if not include_self:
            syms = syms[1:]
        return syms
