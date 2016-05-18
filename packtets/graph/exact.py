from random import randrange

def exact_igraph(g):
  sets = g.largest_independent_vertex_sets()
  index = randrange(len(sets))

  return sets[index]
