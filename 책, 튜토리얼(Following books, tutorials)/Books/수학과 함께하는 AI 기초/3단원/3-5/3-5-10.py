import numpy as np
import matplotlib.pyplot as plt

def Step(x):
  return np.array(x>0,dtype=np.int)

# 시그모이드 함수를 이용하여 곡선으로 출력하기
def Sigmoid(X):
    return 1 / (1+np.exp(-X))

x = np.arange(-10.0,10.0,0.1)
y1 = Step(x)
y2 = Sigmoid(x)

plt.plot(x,y1)
plt.plot(x,y2)
plt.grid()
plt.show()