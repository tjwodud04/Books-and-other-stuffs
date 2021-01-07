import librosa
import librosa.display
import numpy as np

# 입력변수와 출력변수 생성하기
X_train=np.zeros((40,20))
y_train=np.zeros(40)

#인덱스번호 0~19번까지는 레이블 1(배고픔), 21~40번까지는 레이블 0(웃음)
y_train[0:20] = 1

# hungry_특징추출
for i in range(20):
  audio_path = './hungry/hungry_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc = librosa.feature.mfcc(y = y, sr = sr)
  temp = mfcc.mean(axis = 1)
  X_train[i] = temp

# laugh_특징추출  
for i in range(20):
  audio_path = './laugh/laugh_'+str(i+1)+'.wav'
  y, sr = librosa.load(audio_path)
  mfcc = librosa.feature.mfcc(y=y, sr=sr)
  temp = mfcc.mean(axis=1)
  X_train[i+20] = temp

# 추출한 특성 값들을 데이터 셋으로 묶기
# 데이터 셋
data_sets=np.zeros((40,21))
data_sets[:,0:20] = X_train
data_sets[:,20] = y_train

# csv 모듈을 이용하여 파일로 추출하기
# 로지스틱 회귀로 접근 가능한지 확인하는 중
# 시도2_기울기의 변화량 만을 수집
def AccumAscentCurv(A):
  accVal=0
  for i in range(len(A)-1):
    accVal = accVal + abs(A[i+1]-A[i])
  return accVal

X = [AccumAscentCurv(X_train[i]) for i in range(40)]
y = y_train

X = np.array(X).reshape(40,1)
y = y.reshape(40,1)

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
    
    #temp = beta0 + X*beta1
    temp = beta0 + np.dot(X,beta1)
    Y_pred = sigmoid(temp)
    
    # likelihood 
    return  -np.sum( a*np.log(Y_pred + delta) + (1-a)*np.log((1 - Y_pred)+delta ) ) 

# 학습을 마친 후, 임의의 데이터에 대해 미래 값 예측 함수
def predict(X):
    #temp = beta0 + beta1*X
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
    
    if (step % 100000 == 0):
        print("Epoch = ", step, "error value = ", Error(X,y) )

'''
Epoch =  0 error value =  322.3619110191665
Epoch =  100000 error value =  193.91479314477627
Epoch =  200000 error value =  138.22437482823452
Epoch =  300000 error value =  113.21280843909207
Epoch =  400000 error value =  98.27180729889263
Epoch =  500000 error value =  88.09784313309167
Epoch =  600000 error value =  80.62233495352692
Epoch =  700000 error value =  74.84838172308177
Epoch =  800000 error value =  70.22816500026754
Epoch =  900000 error value =  66.43224476376038
Epoch =  1000000 error value =  63.24899182737507
Epoch =  1100000 error value =  60.53541930970088
Epoch =  1200000 error value =  58.190985217533274
Epoch =  1300000 error value =  56.14266896330859
Epoch =  1400000 error value =  54.33599875979175
Epoch =  1500000 error value =  52.72941450917179
Epoch =  1600000 error value =  51.29059218978982
Epoch =  1700000 error value =  49.99397036616472
Epoch =  1800000 error value =  48.819041047785404
Epoch =  1900000 error value =  47.74913940588189
Epoch =  2000000 error value =  46.770570126853386
Epoch =  2100000 error value =  45.871963969044174
Epoch =  2200000 error value =  45.04379645672413
Epoch =  2300000 error value =  44.278023226141016
Epoch =  2400000 error value =  43.56779907271842
Epoch =  2500000 error value =  42.90725972328626
Epoch =  2600000 error value =  42.29134958117051
Epoch =  2700000 error value =  41.71568549436843
Epoch =  2800000 error value =  41.17644707205638
Epoch =  2900000 error value =  40.67028812405571
Epoch =  3000000 error value =  40.19426444864042
Epoch =  3100000 error value =  39.745774737480765
Epoch =  3200000 error value =  39.3225112634409
Epoch =  3300000 error value =  38.922419336642825
Epoch =  3400000 error value =  38.54366328384576
Epoch =  3500000 error value =  38.184597673638294
Epoch =  3600000 error value =  37.84374316099091
Epoch =  3700000 error value =  37.519765557773304
Epoch =  3800000 error value =  37.211458829187535
Epoch =  3900000 error value =  36.91772963865484
Epoch =  4000000 error value =  36.637584343674604
Epoch =  4100000 error value =  36.37011783398323
Epoch =  4200000 error value =  36.11450416062759
Epoch =  4300000 error value =  35.869987355803325
Epoch =  4400000 error value =  35.635874734961874
Epoch =  4500000 error value =  35.41153002310447
Epoch =  4600000 error value =  35.19636810878116
Epoch =  4700000 error value =  34.989849325473934
Epoch =  4800000 error value =  34.79147571535724
Epoch =  4900000 error value =  34.60078665748394
Epoch =  5000000 error value =  34.417355720943554
Epoch =  5100000 error value =  34.24078719081788
Epoch =  5200000 error value =  34.070713727400054
Epoch =  5300000 error value =  33.90679359585344
Epoch =  5400000 error value =  33.74870858142832
Epoch =  5500000 error value =  33.59616197471014
Epoch =  5600000 error value =  33.448876740272226
Epoch =  5700000 error value =  33.3065937994909
Epoch =  5800000 error value =  33.16907094131612
Epoch =  5900000 error value =  33.03608133877051
Epoch =  6000000 error value =  32.90741189981409
Epoch =  6100000 error value =  32.782862771335374
Epoch =  6200000 error value =  32.66224650398614
Epoch =  6300000 error value =  32.54538618141872
Epoch =  6400000 error value =  32.43211577481995
Epoch =  6500000 error value =  32.32227853523193
Epoch =  6600000 error value =  32.21572666095746
Epoch =  6700000 error value =  32.11232073635884
Epoch =  6800000 error value =  32.01192901639652
Epoch =  6900000 error value =  31.9144270305383
Epoch =  7000000 error value =  31.81969691788652
Epoch =  7100000 error value =  31.72762694380765
Epoch =  7200000 error value =  31.638111643749482
Epoch =  7300000 error value =  31.5510506613197
Epoch =  7400000 error value =  31.4663487564018
Epoch =  7500000 error value =  31.38391576836583
Epoch =  7600000 error value =  31.303666001699717
Epoch =  7700000 error value =  31.225517578244904
Epoch =  7800000 error value =  31.149392713098727
Epoch =  7900000 error value =  31.075218067512797
Epoch =  8000000 error value =  31.00292266589792
Epoch =  8100000 error value =  30.93243992872682
Epoch =  8200000 error value =  30.863705560748496
Epoch =  8300000 error value =  30.796658646662838
Epoch =  8400000 error value =  30.731241081959272
Epoch =  8500000 error value =  30.667397141487278
Epoch =  8600000 error value =  30.605073534435803
Epoch =  8700000 error value =  30.544219411545075
Epoch =  8800000 error value =  30.48478641670907
Epoch =  8900000 error value =  30.42672777005629
Epoch =  9000000 error value =  30.369998926035016
Epoch =  9100000 error value =  30.31455722411544
Epoch =  9200000 error value =  30.260361985211418
Epoch =  9300000 error value =  30.207373919278893
Epoch =  9400000 error value =  30.155555168655756
Epoch =  9500000 error value =  30.10486983768736
Epoch =  9600000 error value =  30.05528325304017
Epoch =  9700000 error value =  30.006761998939623
Epoch =  9800000 error value =  29.959274396797937
Epoch =  9900000 error value =  29.9127897604918
Epoch =  10000000 error value =  29.867278300367126
'''