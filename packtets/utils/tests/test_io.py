from packtets.utils import read_packing, write_packing
from packtets.geometry import Cell, Tet
from numpy.linalg import norm

def test_restore_cell():
    box1 = Cell([1.,0.,0.], [0.,1.,0.], [0.,0.,1.])
    packing1 = []
    write_packing("pack.tmp", packing1, box1)

    packing2, box2 = read_packing("pack.tmp")
    
    assert len(packing1) == len(packing2)
    assert norm(box1.trans - box2.trans) < 1.0e-12

def test_restore_tet():
    box1 = Cell([1.,0.,0.], [0.,1.,0.], [0.,0.,1.])
    tet1 = Tet([0.1, 0.2, 0.3], 0.2, 0.1, 0.0)
    packing1 = [tet1]
    write_packing("pack.tmp", packing1, box1)

    packing2, box2 = read_packing("pack.tmp")
    
    assert len(packing1) == len(packing2)
    assert norm(box1.trans - box2.trans) < 1.0e-12
    assert norm(packing1[0].center - packing2[0].center) < 1.0e-12
    assert norm(packing1[0].theta  - packing2[0].theta)  < 1.0e-12
    assert norm(packing1[0].phi    - packing2[0].phi)    < 1.0e-12
    assert norm(packing1[0].psi    - packing2[0].psi)    < 1.0e-12

