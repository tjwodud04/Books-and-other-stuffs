import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc, font_manager

N = 2
H = 3
T = 20

dh = np.ones((N,H))
np.random.seed(3)
#Wh = np.random.randn(H,H)
Wh = np.random.randn(H,H) * 0.5

norm_list = []
for t in range(T):
    dh = np.matmul(dh, Wh.T)
    norm = np.sqrt(np.sum(dh**2)) / N
    norm_list.append(norm)

path = 'C:/Windows/Fonts/malgun.ttf'
font = font_manager. FontProperties(fname=path).get_name()
rc('font', family=font)
plt.plot(np.arange(len(norm_list)), norm_list)
plt.xticks([0, 4, 9, 14, 19], [1, 5, 10, 15, 20])
plt.xlabel('시간 크기(time step)')
plt.ylabel('노름(norm)')
plt.show()