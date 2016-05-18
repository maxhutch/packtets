import numpy as np

class Cell:
    
    def __init__(self, vx, vy, vz):
        self.vx = np.array(vx)
        self.vy = np.array(vy)
        self.vz = np.array(vz)
        self.trans = np.stack((self.vx, self.vy, self.vz), axis=-1)
        self.volume = np.abs(np.dot(self.vx, np.cross(self.vy, self.vz)))
        return

