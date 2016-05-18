import numpy as np

def sort_vertices(v, d):
    if d[0] * d[1] < 0 and d[0] * d[2] < 0:
        return v, d
    if d[1] * d[0] < 0 and d[1] * d[2] < 0:
        return [v[1], v[0], v[2]], [d[1], d[0], d[2]]
    return [v[2], v[0], v[1]], [d[2], d[0], d[1]]

def collision_line(u0, u1, v0, v1):
    mu = (u1[1] - u0[1]) / (u1[0] - u0[0])
    iu = u0[1] - mu * u0[0]
    mv = (v1[1] - v0[1]) / (v1[0] - v0[0])
    iv = v0[1] - mv * v0[0]
    if abs(mu - mv) < 1.0e-6:
        return abs(iu - iv) < 1.0e-6
    x = (iu - iv) / (mv - mu)
    if (x > min(u0[0], u1[0]) and 
        x < max(u0[0], u1[0]) and 
        x > min(v0[0], v1[0]) and 
        x < max(v0[0], v1[0]) ):
        return True
    return False

def collision_face_coplanar(u, v):
    for i,j in [(0,1), (0,2), (1,2)]:
        for k,l in [(0,1), (0,2), (1,2)]:
            if collision_line(u[i], u[j], v[k], v[l]):
                return True
    return False

def collision_face(u, v):    
    Nv = np.cross(v[1] - v[0], v[2]-v[0])
    d2 = - np.dot(Nv, v[0])
    du = np.array([np.dot(Nv, x) + d2 for x in u])
    if np.all(du > 0) or np.all(du < 0):
        return False
    
    Nu = np.cross(u[1] - u[0], u[2]-u[0])
    d1 = - np.dot(Nu, u[0])
    dv = np.array([np.dot(Nu, x) + d1 for x in v])
    if np.all(dv > 0) or np.all(dv < 0):
        return False
    
    if np.all(du == 0):
        return collision_coplanar()
    
    D = np.cross(Nu, Nv)
    u, du = sort_vertices(u, du)
    v, dv = sort_vertices(v, dv)
    
    pu = [np.dot(D, x) for x in u]
    pv = [np.dot(D, x) for x in v]
    tu = [pu[i] + (pu[0] - pu[i])*du[i]/(du[i] - du[0]) for i in (1,2)]
    tv = [pv[i] + (pv[0] - pv[i])*dv[i]/(dv[i] - dv[0]) for i in (1,2)]
    
    if (tu[1] - tv[0]) * (tu[1] - tv[1]) < 0:
        return True
    if (tu[0] - tv[0]) * (tu[0] - tv[1]) < 0:
        return True
    if (tv[1] - tu[0]) * (tv[1] - tu[1]) < 0:
        return True
    if (tv[0] - tu[0]) * (tv[0] - tu[1]) < 0:
        return True
    return False
