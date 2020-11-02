# 소리 데이터에 필요한 외부 모듈 설정하기

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile
import sounddevice as sd

v_samplerate, v_data = scipy.io.wavfile.read("thank_you.wav")
times = np.arange(len(v_data))/float(v_samplerate)

print('sampling rate: ', v_samplerate)
print('time : ', times[-1])
print('vData : ', v_data[5000:5100])
'''
sampling rate:  22050
time :  0.7813605442176871
vData :  [  2899   3912   4583   4520   3852   2744   1496    725    890   1968
   3470   4616   4867   4266   3267   2566   2671   3451   4471   5311
   5480   4789   3642   2628   2172   2296   2552   2587   2365   1788
    812   -417  -1848  -3250  -4074  -4209  -4236  -4794  -6158  -8135
 -10150 -11595 -12089 -11715 -11148 -11117 -11836 -13066 -14205 -14524
 -13937 -13173 -12830 -12816 -12661 -11620  -8703  -3632   2073   5600
   5077   1793   -231   2004   7297  11561  11937   9086   5769   3724
   2460   1004   -461  -1253  -1480  -2055  -3581  -5579  -7018  -7343
  -6614  -4950  -2371    628   2774   2899   1316     -9    945   4290
   8101  10304  10278   8894   7496   6716   6502   6936   7903   8664]
'''

sd.play(v_data, v_samplerate)

plt.plot(times, v_data)
plt.xlim(times[0], times[-1])
plt.xlabel('time (s)')
plt.ylabel('amplitude')

plt.show()

