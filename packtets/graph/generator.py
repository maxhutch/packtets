import igraph

def tet_collision(t1, t2, vx, vy, vz):
    sym1 = t1.get_symmetry(vx, vy, vz)
    sym2 = t2.get_symmetry(vx, vy, vz)
    for s1 in sym1:
        for s2 in sym2:
            if s1.collision(s2):
                return True
    return False

def packing_graph(tets, vx, vy, vz, independent = 0):
    N = len(tets)
    for i in range(N-1, independent-1, -1):
      for s in tets[i].get_symmetry(vx, vy, vz, include_self=False):
          if tets[i].collision(s):
              del tets[i] 
              break

    N = len(tets)
    g = igraph.Graph()
    g.add_vertices(N)
    for i in range(N):
        for j in range(max(i+1, independent),N):
            if tet_collision(tets[i], tets[j], vx, vy, vz):
                g.add_edge(i,j)

    return g
