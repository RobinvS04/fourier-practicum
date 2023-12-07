from experiment import experiment
import matplotlib.pyplot as plt
class view:
    def __init__(self):
        self.Power = experiment.fft_function()
        self.freq = experiment.fft_freq()
    def plot_signal(self):
        
        plt.figure(1)
        plt.plot(t,f,color='c', label='noisy')
        plt.plot(t,f_clean,color='k', label='clean')
        plt.xlabel("time")
        plt.ylabel("function intensity")
        plt.savefig('noisy and clean data')
    def plot_FFT(self):
        plt.plot(self.freq, self.Power)
        # plt.plot(freq,PSD)
        plt.xlabel("Frequencies [Hz]")
        plt.ylabel("Intsity")
        plt.savefig('FFT')