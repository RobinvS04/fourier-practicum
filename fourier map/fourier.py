import numpy as np
import matplotlib.pyplot as plt

# making of the data
dt = 0.001
t = np.arange(0, 1, dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t) #twee verschillende frequenties
f_clean = f
f = f + 2.5*np.random.randn(len(t))

plt.figure(1)
plt.plot(t,f,color='c', label='noisy')
plt.plot(t,f_clean,color='k', label='clean')
plt.xlabel("time")
plt.ylabel("function intensity")
plt.savefig('noisy and clean data')

plt.figure(2)

# fourier transformation
n = len(t)
# fourier transform including complex values
fhat = np.fft.fft(f,n)

# complex conjugate of the fft, gets complex and real values in one real variable: PSD
PSD = fhat * np.conj(fhat) / n

# define frequency, 1/(dt*n) is the stepsize in frequency
# freq = (1/(dt*n)) * np.arange(n)
freq=np.fft.fftfreq(n)
# L is used to get the real values when plotting
L = np.arange(1, np.floor(n/2), dtype='int')

PSD_max = max(PSD)
print(f'PSD_max = {PSD_max}')
PSD_limit = PSD_max / 2

closeby_1 = False
closeby_2 = False

for x in range(n):
    if PSD[x] > PSD_limit and closeby_1 == False:
        print(x)
        closeby_1 = True
    elif PSD[x] > PSD_limit and closeby_1 == True and closeby_2 == False:
        print(f'De tweede frequentie is {x}')
        closeby_2 = True

plt.plot(freq[L], PSD[L])
# plt.plot(freq,PSD)
plt.xlabel("Frequencies [Hz]")
plt.ylabel("Intsity")
plt.savefig('FFT')

