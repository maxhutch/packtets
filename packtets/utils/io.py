from ..geometry import Cell, Tet
import numpy as np

def read_packing(fname):
    """Read packing and cell from file"""
    with open(fname, 'r') as f:
        lines = f.readlines()
    v = []
    for i in range(3):
        toks = lines[i].split()
        v.append(np.array([float(x) for x in toks[0:3]]))
    box = Cell(v[0], v[1], v[2])

    packing = []
    for i in range(3,len(lines)):
        toks = lines[i].split()
        center = np.array([float(x) for x in toks[0:3]])
        theta = float(toks[3])
        phi   = float(toks[4])
        psi   = float(toks[5])
        packing.append(Tet(center, theta, phi, psi))

    return packing, box

def write_packing(fname, packing, box):
    """Write box and packing as list of basis vectors, tets"""
    with open(fname, 'w') as f:
        f.write("{} {} {}\n".format(box.vx[0], box.vx[1], box.vx[2]))
        f.write("{} {} {}\n".format(box.vy[0], box.vy[1], box.vy[2]))
        f.write("{} {} {}\n".format(box.vz[0], box.vz[1], box.vz[2]))

        for tet in packing:
            f.write("{} {} {} {} {} {}\n".format(
                tet.center[0], 
                tet.center[1], 
                tet.center[2],
                tet.theta, 
                tet.phi, 
                tet.psi))
    return

def write_verts(fname, packing, box):
    """Write box and packing, but as a list of tet vertices"""
    with open(fname, 'w') as f:
        f.write("{} {} {}\n".format(box.vx[0], box.vx[1], box.vx[2]))
        f.write("{} {} {}\n".format(box.vy[0], box.vy[1], box.vy[2]))
        f.write("{} {} {}\n".format(box.vz[0], box.vz[1], box.vz[2]))

        for tet in packing:
            for v in tet.verts:
                f.write("{} {} {} ".format(v[0], v[1], v[2]))
            f.write("\n") 

    return
