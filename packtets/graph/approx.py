import numpy as np

def greedy_max(g):
    adj = np.array(g.get_adjacency()._get_data())
    while np.sum(adj) > 0:
        max_row = np.argmax(np.sum(adj, axis=1))
        adj = np.delete(adj, max_row, 0)
        adj = np.delete(adj, max_row, 1)
    return adj.shape[0]

def greedy_min(g):
    adj = np.array(g.get_adjacency()._get_data())
    while np.sum(adj) > 0:
        min_row = np.argmin(np.sum(adj, axis=1))
        to_remove = np.nonzero(adj[min_row,:])
        adj = np.delete(adj, to_remove, 0)
        adj = np.delete(adj, to_remove, 1)
    return adj.shape[0]
