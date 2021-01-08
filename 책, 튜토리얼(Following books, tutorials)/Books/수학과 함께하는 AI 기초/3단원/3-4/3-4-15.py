import librosa
import librosa.display
import numpy as np

# 입력변수와 출력변수 생성하기
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

def sigmoid(X):
    return 1 / (1 + np.exp(-X))

def cost_func(X, a):
    delta = 1e-7
    temp = beta0 + np.dot(X, beta1)
    Y_pred = sigmoid(temp)

    # likelihood
    return -np.sum(a * np.log(Y_pred + delta) + (1 - a) * np.log((1 - Y_pred) + delta))

# 에포크(Epoch) 마다 손실(비용)값을 계산하는 Error 함수 정의하기
def Error(X, a):
    delta = 1e-7

    # temp = beta0 + X*beta1
    temp = beta0 + np.dot(X, beta1)
    Y_pred = sigmoid(temp)

    # likelihood
    return -np.sum(a * np.log(Y_pred + delta) + (1 - a) * np.log((1 - Y_pred) + delta))

# 학습을 마친 후, 임의의 데이터에 대해 미래 값 예측 함수
def predict(X):
    # temp = beta0 + beta1*X
    temp = np.dot(X, beta1) + beta0
    Y_pred = sigmoid(temp)

    if Y_pred >= 0.79:
        result = 1
    else:
        result = 0

    return Y_pred, result

def numerical_derivative(f, x):
    delta_x = 1e-4
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + delta_x
        fx1 = f(x)

        x[idx] = tmp_val - delta_x
        fx2 = f(x)
        grad[idx] = (fx1 - fx2) / (2 * delta_x)

        x[idx] = tmp_val
        it.iternext()

    return grad

# 파라미터 업데이트하기
learning_rate = 1e-3
beta1 = np.random.rand(1, 1)
beta0 = np.random.rand(1)

F = lambda X: cost_func(X, y)

for step in range(10000001):
    beta1 -= learning_rate * numerical_derivative(F, beta1)
    beta0 -= learning_rate * numerical_derivative(F, beta0)
            
# 5-5-2 평가하기
count = 0
for i in range(len(X)):
  (temp1, temp2) = predict(X[i])

  print(i+1, temp1,temp2,temp2 == y[i] )

  if (temp2==y[i]) :
    count += 1

print("정확도:{0}".format(count/len(X)))

'''
1 [0.84316295] 1 [ True]
2 [0.7889664] 0 [False]
3 [0.7990686] 1 [ True]
4 [0.81867226] 1 [ True]
5 [0.82099056] 1 [ True]
6 [0.83956306] 1 [ True]
7 [0.83106934] 1 [ True]
8 [0.84001245] 1 [ True]
9 [0.83210642] 1 [ True]
10 [0.82005556] 1 [ True]
11 [0.84331787] 1 [ True]
12 [0.82980906] 1 [ True]
13 [0.81766475] 1 [ True]
14 [0.90710362] 1 [ True]
15 [0.78132026] 0 [False]
16 [0.86149745] 1 [ True]
17 [0.82616955] 1 [ True]
18 [0.84228177] 1 [ True]
19 [0.78853452] 0 [False]
20 [0.79169069] 1 [ True]
21 [0.7133528] 0 [ True]
22 [0.71422731] 0 [ True]
23 [0.71180112] 0 [ True]
24 [0.71249233] 0 [ True]
25 [0.71138821] 0 [ True]
26 [0.71024184] 0 [ True]
27 [0.71178987] 0 [ True]
28 [0.7199339] 0 [ True]
29 [0.75396649] 0 [ True]
30 [0.75396878] 0 [ True]
31 [0.7531266] 0 [ True]
32 [0.74827449] 0 [ True]
33 [0.74949531] 0 [ True]
34 [0.72530898] 0 [ True]
35 [0.72766103] 0 [ True]
36 [0.72579582] 0 [ True]
37 [0.72809038] 0 [ True]
38 [0.72792987] 0 [ True]
39 [0.72218315] 0 [ True]
40 [0.72733665] 0 [ True]
정확도:0.925
'''