# 활성화 함수 g를 출력하기
import numpy as np
import matplotlib.pyplot as plt

def Step(x):
  return np.array(x>0,dtype=np.int)

x = np.arange(-10.0,10.0,0.1)
y = Step(x)

plt.plot(x,y)
plt.grid()
plt.show()
