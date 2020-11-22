# 나만의 소리 파일의 데이터와 샘플링 주기를 그래프로 출력하기

import numpy as np
import scipy.io as sio
from scipy.io.wavfile import write
import os

v_samplerate, v_data = sio.wavfile.read("thank_you.wav")
b_samplerate, b_data = sio.wavfile.read("Invisible_Beauty.wav")

v_times = np.arange(len(v_data))/float(v_samplerate)
b_times = np.arange(len(b_data))/float(b_samplerate)

# ------------------------------------------------------------------------
import matplotlib.pyplot as plt

plt.plot(v_times, v_data)
plt.xlim(v_times[0], v_times[-1])
plt.xlabel('voice time (s)')
plt.ylabel('amplitude')
plt.show()

plt.plot(b_times, b_data)
plt.xlabel('bg time (s)')
plt.ylabel('amplitude')
plt.show()

