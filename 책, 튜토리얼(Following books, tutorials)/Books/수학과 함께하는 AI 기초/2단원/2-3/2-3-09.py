# 나만의 소리 파일의 샘플링 주기와 채널 타입 바꾸기

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio            
from scipy.io.wavfile import write
import os

v_samplerate, v_data = sio.wavfile.read('thank_you.wav')
b_samplerate, b_data = sio.wavfile.read("Invisible_Beauty.wav")

v_times = np.arange(len(v_data))/float(v_samplerate)
b_times = np.arange(len(b_data))/float(b_samplerate)

# ------------------------------------------------------------------------

if (len(v_data.shape) > 1) : 
   v_data = np.array(v_data[:,0])

if (len(b_data.shape) > 1) :
   b_data = np.array(b_data[:,0])

if (v_samplerate > b_samplerate) :
   diffRate = v_samplerate / b_samplerate
   v_data = np.array(v_data[0:len(v_data):diffRate])
   sr = b_samplerate

elif (v_samplerate < b_samplerate) :
   diffRate = int(b_samplerate / v_samplerate)
   b_data = np.array(b_data[0:len(b_data):diffRate])
   sr = v_samplerate

else :
   sr = b_samplerate

mix_data = v_data + b_data[sr*10:len(v_data)+sr*10]

b_data[sr*10:len(v_data)+sr*10] = mix_data

scaled = np.int16(b_data/np.max(np.abs(b_data)) * 32767)
write('music_card.wav', sr, scaled)
os.system("start music_card.wav")
