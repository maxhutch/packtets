from copy import deepcopy
from time import time
from numpy.random import uniform, normal
from numpy import pi, sqrt, mod
from numpy import dot
from .geometry import Tet
from .graph import packing_graph
from .graph import exact_igraph

def uniform_sample(packing, cell, N_add):
    """Uniformally sample the cell volume and tet orientation and return packing"""
    for j in range(N_add):
        center = dot(cell.trans, uniform(0, 1, 3))
        theta = uniform(0, 2*pi)
        phi   = uniform(0, 2*pi)
        psi   = uniform(0, 2*pi)
        packing.append(Tet(center, theta, phi, psi)) 
    return packing

def concentrated_sample(packing, cell, N_add, width=0.5):
    """Uniformally sample a nexus, then place tets near that nexus"""

    # draw a uniform random nexus
    nexus = uniform(0,1,3)
    for j in range(N_add):
        # draw a normally distributed displacement
        disp = normal(scale=width, size=3)
        # Find periodic mirror in primitive cell
        center = dot(cell.trans, mod(disp + nexus, 1))
        theta = uniform(0, 2*pi)
        phi   = uniform(0, 2*pi)
        psi   = uniform(0, 2*pi)
        packing.append(Tet(center, theta, phi, psi)) 
    return packing

def no_relax(packing, cell):
    """Don't do any relaxation"""
    return packing

def no_resize(packing, cell):
    """Don't do any resizing"""
    return packing, cell

def pack_tets(cell, input_packing=[], time_budget=60, verbose=False, N_start=10, 
        sample=uniform_sample, relax=no_relax, resize=no_resize):
    """Packs tets into cell, returning packing"""

    # copy to stay pure
    packing = deepcopy(input_packing)

    # pre-loop initialization of time and packing info
    start_time = time()
    num_packed = len(packing)
    N_add = N_start

    # run until out of time
    while time() - start_time < time_budget:
        # Step 1: Sample new tets onto previous solution
        packing = sample(packing, cell, N_add)
              
        # Step 2: construct collision graph 
        t0 = time()
        g = packing_graph(packing, cell.vx, cell.vy, cell.vz, num_packed)
        t_make = time() - t0
    
        # Step 3: Solve max independent set problem
        t0 = time()
        max_ind_set = exact_igraph(g)
        t_solve = time() - t0
        num_packed = len(max_ind_set)
       
        # if the MIS was cheap, add more tets next time 
        if t_solve < t_make:
            N_add += 1
        else:
            N_add += -1

        # extract new max packing
        old_packing = packing
        packing = []
        for j in range(num_packed):
            packing.append(old_packing[max_ind_set[j]])                

        # Step 4: Relax the packing 
        packing = relax(packing, cell)
       
        # Step 5: Resize the cell  
        packing, cell = resize(packing, cell)
        
        # print packing density
        if verbose:
            packing_ratio = num_packed / (6*sqrt(2)) / cell.volume
            print(packing_ratio, num_packed, N_add)
    
    return packing
