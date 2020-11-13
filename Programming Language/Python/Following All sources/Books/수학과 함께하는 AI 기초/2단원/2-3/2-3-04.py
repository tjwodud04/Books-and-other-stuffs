import numpy as np
import matplotlib.pyplot as plt
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

# -------------------------------------------------------------------------------------

noise = np.random.uniform(-1, 1, len(t))
scaled_noise = noise * 0.3

print("noise[0:20] = ")
print(noise[0:20])
print("scaled_noise[0:20] = ")
print(scaled_noise[0:20])
'''
noise[0:20] = 
[-0.58787569 -0.95846502  0.78966961 -0.05532778 -0.78702631 -0.97261785
  0.62329781 -0.16669088 -0.10996928 -0.60168463  0.86086294  0.33176946
  0.18321136  0.81126817 -0.83014061  0.76996129  0.98229615 -0.41188348
 -0.01852613  0.03981503]
scaled_noise[0:20] = 
[-0.17636271 -0.2875395   0.23690088 -0.01659833 -0.23610789 -0.29178535
  0.18698934 -0.05000727 -0.03299078 -0.18050539  0.25825888  0.09953084
  0.05496341  0.24338045 -0.24904218  0.23098839  0.29468884 -0.12356504
 -0.00555784  0.01194451]
'''

plt.plot(t[0:x_range], noise[0:x_range], color='red')
plt.show()

plt.plot(t[0:x_range], scaled_noise[0:x_range], color='green')
plt.ylim(-1, 1)
plt.show()

scaled = np.int16(noise / np.max(np.abs(noise)) * 32767)
write('noise_signal.wav', 44100, scaled)