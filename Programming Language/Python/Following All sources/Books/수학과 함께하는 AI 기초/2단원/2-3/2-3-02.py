# 소리 데이터에 필요한 외부 모듈과 환경 변수 설정하기

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import os

Fs = 44100.0

tlen = 1
Ts = 1/Fs
t = np.arange(0, tlen, Ts)

sin_freq = 440
src = 2*np.pi*sin_freq*t
signal = np.sin(src)

x_range = 200
plt.plot(t[0:x_range], signal[0:x_range], color = 'blue')

plt.show()

freq = np.fft.fftfreq(len(t), Ts)
signal_f = np.fft.fft(signal)

plt.plot(freq[0:x_range], 20*np.log10(np.abs(signal_f[0:x_range])), color='blue')

plt.show()

#scaled = np.int16(signal/np.max(np.abs(signal)) * 32767)
#write('snd_signal.wav', 44100, scaled)
