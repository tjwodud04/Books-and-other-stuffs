import tensorflow as tf
import numpy as np

tf.set_random_seed(777)

xy = np.loadtxt('data-01-test-score.csv', delimiter=',', dtype=np.float32)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print(x_data, "\nx_data shape:", x_data.shape)
print(y_data, "\nx_data shape:", y_data.shape)

