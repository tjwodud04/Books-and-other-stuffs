import librosa
import librosa.display

audio = 'discomfort/discomfort_1.wav'
y, sr = librosa.load(audio)

print(y)
print(sr)

'''
[-0.00059498 -0.00078233 -0.00097827 ...  0.07309957  0.05529897
  0.02827073]
22050
'''