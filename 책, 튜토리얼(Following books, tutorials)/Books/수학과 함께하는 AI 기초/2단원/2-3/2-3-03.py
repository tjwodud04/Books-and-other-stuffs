# 생성한 소리 데이터를 wav 형식의 파일로 저장하기

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

# -------------------------------------------------------------------------------

scaled = np.int16(signal/np.max(np.abs(signal)) * 32767)
write('snd_signal.wav', 44100, scaled)

