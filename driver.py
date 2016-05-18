from sys import argv
from os.path import exists
from packtets.geometry import Cell, Tet
import numpy as np

solution_file = argv[1]
if exists(solution_file):
    with open(solution_file, 'r') as f:
        lines = f.readlines()
    v = []
    for i in range(3):
        toks = lines[i].split()
        v.append(np.array([float(x) for x in toks[0:3]]))
    box = Cell(v[0], v[1], v[2])

    tets = []
    for i in range(3,len(lines)):
        toks = lines[i].split()
        center = np.array([float(x) for x in toks[0:3]])
        theta = float(toks[3])
        phi   = float(toks[4])
        psi   = float(toks[5])
        tets.append(Tet(center, theta, phi, psi))
    packing_ratio = len(tets) / (6*np.sqrt(2)) / box.volume
    print("Loaded packing ratio of {} ({} tets)".format(packing_ratio, len(tets)))
else:
    box = Cell([1., 0., 0.], [0., 1., 0.], [0., 0., 1.])
    tets = []

from packtets import pack_tets
res = pack_tets(box, starting_set=tets, time_budget=60, verbose=False)
packing_ratio = len(res) / (6*np.sqrt(2)) / box.volume

print("Achieved packing ratio of {}".format(packing_ratio))

with open(solution_file, 'w') as f:
    f.write("{} {} {}\n".format(box.vx[0], box.vx[1], box.vx[2]))
    f.write("{} {} {}\n".format(box.vy[0], box.vy[1], box.vy[2]))
    f.write("{} {} {}\n".format(box.vz[0], box.vz[1], box.vz[2]))

    for tet in res:
        f.write("{} {} {} {} {} {}\n".format(tet.center[0], tet.center[1], tet.center[2], 
                                           tet.theta, tet.phi, tet.psi))

