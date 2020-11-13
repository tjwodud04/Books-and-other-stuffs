# 생활 속의 소리 합성하기

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from scipy.io.wavfile import write
import os

Fs = 44100.0

tlen = 1
Ts = 1 / Fs
t = np.arange(0, tlen, Ts)

sin_freq = 440
src = 2 * np.pi * sin_freq * t
signal = np.sin(src)

x_range = 200
noise = np.random.uniform(-1, 1, len(t))

# -----------------------------------------------------------------------------------------
signal_n = signal + noise

scaled_noise = noise * 0.3
signal_n = signal + scaled_noise
# save as wav file
scaled = np.int16(signal_n / np.max(np.abs(signal_n)) * 32767)
write('snd_noise.wav', 44100, scaled)

# show the raw signals
plt.plot(t[0:x_range], signal[0:x_range], color='blue')
plt.plot(t[0:x_range], scaled_noise[0:x_range], color='red')
plt.show()

plt.plot(t[0:x_range], signal_n[0:x_range], color='green')
plt.show()
