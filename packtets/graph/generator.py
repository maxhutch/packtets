import igraph

def packing_graph(tets, vx, vy, vz, independent = 0):
    N = len(tets)
    for i in range(N-1, independent-1, -1):
      for s in tets[i].get_symetry(vx, vy, vz, include_self=False):
          if tets[i].collision(s):
              del tets[i] 
              break

    N = len(tets)
    g = igraph.Graph()
    g.add_vertices(N)
    for i in range(N):
        for j in range(max(i, independent),N):
            for s in tets[j].get_symetry(vx, vy, vz, include_self=(i != j)):
                if tets[i].collision(s):
                    g.add_edge(i,j)
                    break

    return g
