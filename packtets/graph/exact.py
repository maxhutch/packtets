from random import randrange

def exact_igraph(g):
  sets = g.largest_independent_vertex_sets()
  print("There are {} largest independent vertex sets".format(len(sets)))
  assert isinstance(sets[0], tuple)
  index = randrange(len(sets))

  return sets[index]
