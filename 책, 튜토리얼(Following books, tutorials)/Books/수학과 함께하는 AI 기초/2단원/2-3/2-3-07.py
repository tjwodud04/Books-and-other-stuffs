# 나만의 소리 파일의 데이터와 샘플링 주기 확인하기

import numpy as np
import scipy.io as sio                                   
from scipy.io.wavfile import write
import os

v_samplerate, v_data = sio.wavfile.read("thank_you.wav")
b_samplerate, b_data = sio.wavfile.read("Invisible_Beauty.wav")

v_times = np.arange(len(v_data))/float(v_samplerate)
b_times = np.arange(len(b_data))/float(b_samplerate)

print('sampling rate: ', v_samplerate, b_samplerate)
print('time : ', v_times[-1], b_times[-1])
print('len : ', len(v_data), len(b_data))
'''
sampling rate:  22050 44100
time :  0.7813605442176871 187.1887074829932
len :  17230 8255023
'''

print(v_data.shape)
print(b_data.shape)
'''
(17230,)
(8255023, 2)
'''