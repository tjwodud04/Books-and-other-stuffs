import librosa
import librosa.display
import numpy as np

from sklearn.linear_model import LogisticRegression

X_train = np.zeros((40, 20))
y_train = np.zeros(40)

# 인덱스번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징추출
for i in range(20):
    audio_path = './hungry/hungry_' + str(i + 1) + '.wav'
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    temp = mfcc.mean(axis=1)
    X_train[i] = temp

# laugh_특징추출
for i in range(20):
    audio_path = './laugh/laugh_' + str(i + 1) + '.wav'
    y, sr = librosa.load(audio_path)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    temp = mfcc.mean(axis=1)
    X_train[i + 20] = temp

# 추출한 특성 값들을 데이터 셋으로 묶기
# 데이터 셋
data_sets = np.zeros((40, 21))
data_sets[:, 0:20] = X_train
data_sets[:, 20] = y_train

# csv 모듈을 이용하여 파일로 추출하기
# 로지스틱 회귀로 접근 가능한지 확인하는 중
# 시도2_기울기의 변화량 만을 수집
def AccumAscentCurv(A):
    accVal = 0
    for i in range(len(A) - 1):
        accVal = accVal + abs(A[i + 1] - A[i])
    return accVal

X = [AccumAscentCurv(X_train[i]) for i in range(40)]
y = y_train

X = np.array(X).reshape(40, 1)
y = y.reshape(40, 1)

clf = LogisticRegression(random_state=0).fit(X, y)
# --------------------------
audio_path = 'test01.wav'
y, sr = librosa.load(audio_path)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
X_test = mfcc.mean(axis=1)

# 로지스틱회귀로 접근 가능한지 확인하는 중
# 시도2_기울기의 변화량 만을 수집
X_test = np.array(AccumAscentCurv(X_test).reshape(1,1))

print(clf.predict(X_test))

'''
[1.]
'''