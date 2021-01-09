import librosa
import librosa.display
import numpy as np

# 입력 변수와 출력 변수 생성하기
 
X_train=np.zeros((40,20))
y_train=np.zeros(40)

#인덱스 번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징 추출  
for i in range(20):
  audio_path = 'hungry/hungry_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1)
  X_train[i]=temp

# laugh_특징 추출  
for i in range(20):
  audio_path = 'laugh/laugh_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc= librosa.feature.mfcc(y=y, sr=sr)
  temp=mfcc.mean(axis=1) 
  X_train[i+20]=temp

# 추출한 특성 값들을 데이터 셋으로 묶기
#데이터 셋
data_sets=np.zeros((40,21))
data_sets[:,0:20] = X_train
data_sets[:,20] = y_train

# 데이터 준비하기 ----------------------------
#X=np.array(X).reshape(40,1)
#y=y.reshape(40,1)

# 로지스틱 회귀로 접근 가능한지 확인하는 중
# 시도2_기울기의 변화량 만을 수집
def AccumAscentCurv(A):
  accVal=0
  for i in range(len(A)-1):
    accVal = accVal + abs(A[i+1]-A[i])
  return accVal

X = [AccumAscentCurv(X_train[i]) for i in range(40)]
y = y_train

def sigmoid(X):
    return 1 / (1+np.exp(-X))

def cost_func(X, a):
    delta = 1e-7
    temp = beta0 + np.dot(X,beta1)
    Y_pred = sigmoid(temp)
    
    # likelihood 
    return  -np.sum( a*np.log(Y_pred + delta) + (1-a)*np.log((1 - Y_pred)+delta ) )

# 에포크(Epoch) 마다 손실(비용)값을 계산하는 Error 함수 정의하기
def Error(X, a):
    delta = 1e-7
    temp = beta0 + np.dot(X,beta1)
    Y_pred = sigmoid(temp)
    
    # likelihood 
    return  -np.sum(a*np.log(Y_pred + delta) + (1-a)*np.log((1 - Y_pred)+delta ) ) 

# 학습을 마친후, 임의의 데이터에 대해 미래 값 예측 함수
def predict(X):
    temp = np.dot(X,beta1) + beta0
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
        grad[idx] = (fx1 - fx2) / (2*delta_x)
        
        x[idx] = tmp_val 
        it.iternext()   
        
    return grad

# 파라미터 업데이트하기

learning_rate = 1e-3 
beta1 = np.random.rand(1,1)  
beta0 = np.random.rand(1)

F = lambda X : cost_func(X,y) 

for step in  range(10000001):
    beta1 -= learning_rate * numerical_derivative(F, beta1)
    beta0 -= learning_rate * numerical_derivative(F, beta0)
    
#    if (step % 100000 == 0):
#        print("Epoch = ", step, "error value = ", Error(X,y) )

# 문제해결하기 -----------------------------

# test data 준비하기
audio_path = 'test01.wav'
y, sr = librosa.load(audio_path)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
X_test = mfcc.mean(axis=1)

X_test = np.array(AccumAscentCurv(X_test).reshape(1,1))

# 데이터 분류하기 ----------------------------------

(Y_pred, label) = predict(X_test)

print(Y_pred, label)

'''
[[0.81065545]] 1
'''