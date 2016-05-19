#!/usr/bin/env python3

from sys import argv
from os.path import exists
from packtets import pack_tets, concentrated_sample
from packtets.geometry import Cell, Tet
from packtets.utils import read_packing, write_packing, write_verts
import numpy as np

# Just take the 1st arg, instead of a proper argument parser
solution_file = argv[1]

# If there is already a file there, load it; otherwise pick default values
if exists(solution_file):
    packing, box = read_packing(solution_file)
    packing_ratio = len(packing) / (6*np.sqrt(2)) / box.volume
    print("Loaded packing ratio of {} ({} tets)".format(packing_ratio, len(packing)))
else:
    # default box is unit FCC
    box = Cell([1., 1., 0.], [0., 1., 1.], [1., 0., 1.])
    packing = []

# Call the packing method, running for 60 seconds
packing = pack_tets(box, 
    input_packing=packing, 
    sample=concentrated_sample,
    time_budget=60, 
    verbose=True, 
    N_start = 40)

# How'd we do?
packing_ratio = len(packing) / (6*np.sqrt(2)) / box.volume
print("Achieved packing ratio of {}".format(packing_ratio))

# Write checkpoint file and vertex-format file
write_packing(solution_file, packing, box)
write_verts(solution_file+".vert", packing, box)
