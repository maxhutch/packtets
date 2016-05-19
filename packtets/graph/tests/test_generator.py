from packtets.graph import packing_graph
from packtets.geometry import Tet

unit  = [[1.,0.,0.], [0.,1.,0.], [0.,0.,1.]]
big   = [[100.,0.,0.], [0.,100.,0.], [0.,0.,100.]]
small = [[0.01,0.,0.], [0.,0.01,0.], [0.,0.,0.01]]

def test_single():
    t1 = Tet([0.0,0.,0.], 0.0, 0.0, 0.0)
    g = packing_graph([t1], big[0], big[1], big[2])
    assert len(g.largest_independent_vertex_sets()) == 1
    assert len(g.largest_independent_vertex_sets()[0]) == 1

def test_periodic():
    t1 = Tet([0.,0.,0.], 0., 0., 0.)
    g = packing_graph([t1], small[0], small[1], small[2])
    assert len(g.largest_independent_vertex_sets()) == 1
    assert len(g.largest_independent_vertex_sets()[0]) == 0

def test_collision():
    t1 = Tet([0.0,0.,0.], 0.0, 0.0, 0.0)
    t2 = Tet([0.1,0.,0.], 0.0, 0.0, 0.0)
    g = packing_graph([t1, t2], big[0], big[1], big[2])
    assert len(g.largest_independent_vertex_sets()) == 2
    assert len(g.largest_independent_vertex_sets()[0]) == 1
    assert len(g.largest_independent_vertex_sets()[1]) == 1

def test_no_collision():
    t1 = Tet([0.0,0.,0.], 0.0, 0.0, 0.0)
    t2 = Tet([2.0,0.,0.], 0.0, 0.0, 0.0)
    g = packing_graph([t1, t2], big[0], big[1], big[2])
    assert len(g.largest_independent_vertex_sets()) == 1
    assert len(g.largest_independent_vertex_sets()[0]) == 2


