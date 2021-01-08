import librosa

# test data 준비하기
audio_path = 'test01.wav'
y, sr = librosa.load(audio_path)
mfcc= librosa.feature.mfcc(y=y, sr=sr)
X_test=mfcc.mean(axis=1)

print(X_test)

'''
[-297.9742     146.2829     -55.88721    -10.3654585   -0.5838854
  -46.56438     -8.005969     6.911135   -12.364082     2.9450808
   -2.4025762  -14.01791     -1.0353881   -4.696634    -2.4477494
    8.988057    -5.497288    -8.135314     1.6247091   -9.138424 ]
'''