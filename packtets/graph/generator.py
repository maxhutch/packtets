import igraph

def packing_graph(tets, vx, vy, vz):
    N = len(tets)
    g = igraph.Graph()
    g.add_vertices(N)
    for i in range(N):
        for j in range(i+1,N):
            for s in tets[j].get_symetry(vx, vy, vz):
                if tets[i].collision(s):
                    g.add_edge(i,j)
                    continue
    return g
