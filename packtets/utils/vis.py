try:
    import mpl_toolkits.mplot3d as a3
    import matplotlib.pyplot as plt
except ImportError:
    pass

def plot_packing(packing, box=None, use_symmetry=False):
    """Plot packing within box"""
    ax = a3.Axes3D(plt.figure(10))

    if box is not None:
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
 
        ax.set_xlim(0,max([v[0] for v in bounding]))
        ax.set_ylim(0,max([v[1] for v in bounding]))
        ax.set_zlim(0,max([v[2] for v in bounding]));


    for tet in packing:
        if box is not None and use_symmetry:
          syms = tet.get_symmetry(box.vx, box.vy, box.vz)
        else:
          syms = [tet]

        for s in syms:
            for x,y,z in [(0,1,2), (0,1,3), (0,2,3), (1,2,3)]:
                verts = [tuple(s.verts[x]), tuple(s.verts[y]), tuple(s.verts[z])]
                tri = a3.art3d.Poly3DCollection([verts], alpha=0.2)
                tri.set_edgecolor('k')
                ax.add_collection3d(tri)

    return
