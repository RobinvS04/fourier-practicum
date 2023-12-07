from data_analyse import data
import numpy as np
class experiment:
    def __init__(self):
        self.function = data.make_data()
        self.dt = data.delta_time()
        self.t = np.arange(0, 1, self.dt)
        self.n = len(self.t)

    def fft_function(self):
        # fourier transform including complex values
        fhat = np.fft.fft(self.function,self.n)

        # complex conjugate of the fft, gets complex and real values in one real variable: PSD
        PSD = fhat * np.conj(fhat) / self.n

        # define frequency, 1/(dt*n) is the stepsize in frequency
        

        # L is used to get the real values when plotting
        self.L = np.arange(1, np.floor(self.n/2), dtype='int')
        PSD= PSD[self.L]
        return PSD[L]
    def fft_freq(self):
        freq = (1/(self.dt*self.n)) * np.arange(self.n)
        return freq[self.L]

