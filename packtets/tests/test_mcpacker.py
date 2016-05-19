from packtets import pack_tets
from packtets.geometry import Cell

def test_too_small():
    box = Cell([0.1, 0., 0.], [0., 1., 0.], [0., 0., 1.])
    res = pack_tets(box)
    assert len(res) == 0

def test_one_tet():
    box = Cell([0.75, 0., 0.], [0., 0.75, 0.], [0., 0., 0.75])
    res = pack_tets(box)
    assert len(res) == 1

