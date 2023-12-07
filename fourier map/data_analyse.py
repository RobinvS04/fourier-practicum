import numpy as np
class data:
    def __init__(self):
        self.dt = 0.001
        self.t = np.arange(0, 1, self.dt)
    def delta_time(self):
        return self.dt
    def make_data(self):
        f = np.sin(2*np.pi*50*self.t) + np.sin(2*np.pi*120*self.t)+5*np.sin(2*np.pi*180*self.t) #twee verschillende frequenties
        f_clean = f
        self.f = f_clean + 2.5*np.random.randn(len(self.t))
        return self.f