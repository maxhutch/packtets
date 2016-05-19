from copy import deepcopy
from time import time
from numpy.random import uniform
from numpy import pi, sqrt
from numpy import dot
from .geometry import Tet
from .graph import packing_graph
from .graph import exact_igraph

def pack_tets(cell, starting_set = [], time_budget = 60, verbose=False, N_start = 10):
    tets = deepcopy(starting_set)
    num_packed = len(tets)
    start_time = time()
    N_add = N_start
    while time() - start_time < time_budget:
        for j in range(N_add):
            center = dot(cell.trans, uniform(0, 1, 3))
            theta = uniform(0, 2*pi)
            phi   = uniform(0, 2*pi)
            psi   = uniform(0, 2*pi)
            tets.append(Tet(center, theta, phi, psi)) 
        
        t0 = time()
        g = packing_graph(tets, cell.vx, cell.vy, cell.vz, num_packed)
        t_make = time() - t0
    
        t0 = time()
        max_ind_set = exact_igraph(g)
        t_solve = time() - t0
        num_packed = len(max_ind_set)
        
        if t_solve < t_make:
            N_add += 1
        else:
            N_add += -1

        old_tets = tets
        tets = []
        for j in range(num_packed):
            tets.append(old_tets[max_ind_set[j]])                
        
        packing_ratio = num_packed / (6*sqrt(2)) / cell.volume
        if verbose:
            print(packing_ratio, num_packed, N_add)
    
    return tets
