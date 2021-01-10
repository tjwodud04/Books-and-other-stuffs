# 데이터 불러오기
import pandas as pd
import numpy as np

df_train = pd.read_csv('fashion-mnist_train.csv')
df_test = pd.read_csv('fashion-mnist_test.csv')

#데이터 프레임을 배열 형태로 저장하기
data_train = np.array(df_train,dtype=np.float32)
x_train = data_train[:, 1:]
y_train = data_train[:, 0]

data_test = np.array(df_test)
x_test = data_test[:, 1:]
y_test = data_test[:, 0]

print(df_test)
print(data_test)

'''
     label  pixel1  pixel2  pixel3  ...  pixel781  pixel782  pixel783  pixel784
0         0       0       0       0  ...         0         0         0         0
1         1       0       0       0  ...         0         0         0         0
2         2       0       0       0  ...        31         0         0         0
3         2       0       0       0  ...       222        56         0         0
4         3       0       0       0  ...         0         0         0         0
...     ...     ...     ...     ...  ...       ...       ...       ...       ...
9995      0       0       0       0  ...         1         0         0         0
9996      6       0       0       0  ...        28         0         0         0
9997      8       0       0       0  ...        42         0         1         0
9998      8       0       1       3  ...         0         0         0         0
9999      1       0       0       0  ...         0         0         0         0

[10000 rows x 785 columns]
[[0 0 0 ... 0 0 0]
 [1 0 0 ... 0 0 0]
 [2 0 0 ... 0 0 0]
 ...
 [8 0 0 ... 0 1 0]
 [8 0 1 ... 0 0 0]
 [1 0 0 ... 0 0 0]]
'''