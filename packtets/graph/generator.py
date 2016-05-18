import igraph

def packing_graph(tets, vx, vy, vz, independent = 0):
    N = len(tets)
    g = igraph.Graph()
    g.add_vertices(N)
    for i in range(N):
        for j in range(max(i, independent),N):
            for s in tets[j].get_symetry(vx, vy, vz, include_self=(i != j)):
                if tets[i].collision(s):
                    g.add_edge(i,j)
                    break
    edges = g.get_edgelist()
    for i in range(N, -1, -1):
        if (i,i) in edges:
            g.delete_vertices(g.vs[i])
            del tets[i]
    return g
