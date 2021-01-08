import librosa
import numpy as np

# test data 준비하기
audio_path = 'test01.wav'
y, sr = librosa.load(audio_path)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
X_test = mfcc.mean(axis=1)

# 로지스틱회귀로 접근 가능한지 확인하는 중
# 시도2_기울기의 변화량 만을 수집
def AccumAscentCurv(A):
  accVal = 0
  for i in range(len(A)-1):
    accVal = accVal + abs(A[i+1]-A[i])
  return accVal

X_test = np.array(AccumAscentCurv(X_test).reshape(1,1))

print(X_test)

'''
[[920.70890832]]
'''