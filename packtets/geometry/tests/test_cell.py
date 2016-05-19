from packtets.geometry import Cell
import numpy as np
from numpy.linalg import norm

def test_volume():
    box = Cell([1.,0.,0.], [0.,2.,0.], [0.,0.,3.])
    assert abs(box.volume - 6) < 1.0e-12

def test_trans():
    box = Cell([1.,1.,0.], [0.,2.,2.], [3.,0.,3.])
    assert norm(np.dot(box.trans, [3.,2.,1.]) - np.array([6., 7., 7.])) < 1.0e-12
