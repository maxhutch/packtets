from packtets.geometry import Tet
import numpy as np
from numpy.linalg import norm

def test_center():
    center = np.array([1., 2., 3.])
    t1 = Tet(center, 3., 2., 1.)
    avg = np.zeros(3)
    for v in t1.verts:
        avg += v
    avg *= .25
    assert norm(avg - center) < 1.0e-12

def test_collision():
    center = np.array([1., 2., 3.])
    displacement = np.array([0.5, 0., 0.])
    t1 = Tet(center, 3., 2., 1.)
    t2 = Tet(center+displacement, 1., 2., 3.)
    assert t1.collision(t2)

def test_no_collision():
    center = np.array([1., 2., 3.])
    displacement = np.array([1.5, 0., 0.])
    t1 = Tet(center, 3., 2., 1.)
    t2 = Tet(center+displacement, 1., 2., 3.)
    assert not t1.collision(t2)

def test_symmetry():
    center = np.array([0., 0., 0.])
    t1 = Tet(center, 3., 2., 1.)
    syms = t1.get_symmetry([2., 0., 0.], [0., 2., 0.], [0., 0., 2.])
    assert len(syms) == 8
