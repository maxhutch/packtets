from sys import argv
from os.path import exists
from packtets.geometry import Cell, Tet
from packtets.utils import read_packing, write_packing, write_verts
import numpy as np

solution_file = argv[1]
if exists(solution_file):
    packing, box = read_packing(solution_file)
    packing_ratio = len(packing) / (6*np.sqrt(2)) / box.volume
    print("Loaded packing ratio of {} ({} tets)".format(packing_ratio, len(packing)))
else:
    box = Cell([1., 1., 0.], [0., 1., 1.], [1., 0., 1.])
    packing = []

from packtets import pack_tets
packing = pack_tets(box, input_packing=packing, time_budget=60, verbose=True, N_start = 40)
packing_ratio = len(packing) / (6*np.sqrt(2)) / box.volume

print("Achieved packing ratio of {}".format(packing_ratio))

write_packing(solution_file, packing, box)
write_verts(solution_file+".vert", packing, box)

