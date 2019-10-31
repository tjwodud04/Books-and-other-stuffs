import tensorflow as tf
import numpy as np
tf.set_random_seed(777)

xy = np.loadtxt('data-04-zoo.csv', delimiter=',', dtype=np.float32)
X_data = xy[:, 0:-1]
N = X_data.shape[0]
y_data = xy[:, [-1]]

print("y has one of the following values")
print(np.unique(y_data))
print("Shape of X data: ", X_data.shape)
print("Shape of y data: ", y_data.shape)

nb_classes = 7
X = tf.placeholder(tf.float32, [None, 16])
y = tf.placeholder(tf.int32, [None, 1])

target = tf.one_hot(y, nb_classes)
target = tf.reshape(target, [-1, nb_classes])
target = tf.cast(target, tf.float32)

W = tf.Variable(tf.random_normal([16, nb_classes]), name='weight')
b = tf.Variable(tf.random_normal([nb_classes]), name='bias')

def sigma(x):
    return 1. / (1. + tf.exp(-x))

def sigma_prime(x):
    return sigma(x) * (1. - sigma(x))

layer_1 = tf.matmul(X, W) + b
y_pred = sigma(layer_1)

loss_i = - target * tf.log(y_pred) - (1. - target) * tf.log(1. - y_pred)
loss = tf.reduce_sum(loss_i)

assert y_pred.shape.as_list() == target.shape.as_list()

d_loss = (y_pred - target) / (y_pred * (1. - y_pred) + 1e-7)
d_sigma = sigma_prime(layer_1)
d_layer = d_loss * d_sigma
d_b = d_layer
d_W = tf.matmul(tf.transpose(X), d_layer)

learning_rate = 0.01
train_step = [
    tf.assign(W, W - learning_rate * d_W),
    tf.assign(b, b - learning_rate * tf.reduce_sum(d_b)),
]

prediction = tf.argmax(y_pred, 1)
acct_mat = tf.equal(tf.argmax(y_pred, 1), tf.argmax(target, 1))
acct_res = tf.reduce_mean(tf.cast(acct_mat, tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(500):
        sess.run(train_step, feed_dict={X: X_data, y: y_data})

        if step % 10 == 0:
            step_loss, acc = sess.run([loss, acct_res], feed_dict={
                                      X: X_data, y: y_data})
            print("Step: {:5}\t Loss: {:10.5f}\t Acc: {:.2%}" .format(
                step, step_loss, acc))

    pred = sess.run(prediction, feed_dict={X: X_data})
    for p, y in zip(pred, y_data):
        msg = "[{}]\t Prediction: {:d}\t True y: {:d}"
        print(msg.format(p == int(y[0]), p, int(y[0])))

'''result

y has one of the following values
[0. 1. 2. 3. 4. 5. 6.]
Shape of X data:  (101, 16)
Shape of y data:  (101, 1)

Step:     0	 Loss:  453.74808	 Acc: 38.61%
Step:    10	 Loss:  135.79250	 Acc: 83.17%
Step:    20	 Loss:   95.05664	 Acc: 88.12%
Step:    30	 Loss:   77.29308	 Acc: 91.09%
Step:    40	 Loss:   66.43569	 Acc: 93.07%
Step:    50	 Loss:   58.81989	 Acc: 94.06%
Step:    60	 Loss:   53.09288	 Acc: 94.06%
Step:    70	 Loss:   48.58739	 Acc: 96.04%
Step:    80	 Loss:   44.92377	 Acc: 96.04%
Step:    90	 Loss:   41.86682	 Acc: 97.03%
Step:   100	 Loss:   39.26265	 Acc: 97.03%
Step:   110	 Loss:   37.00650	 Acc: 97.03%
Step:   120	 Loss:   35.02472	 Acc: 97.03%
Step:   130	 Loss:   33.26402	 Acc: 97.03%
Step:   140	 Loss:   31.68491	 Acc: 97.03%
Step:   150	 Loss:   30.25749	 Acc: 97.03%
Step:   160	 Loss:   28.95874	 Acc: 97.03%
Step:   170	 Loss:   27.77063	 Acc: 97.03%
Step:   180	 Loss:   26.67880	 Acc: 97.03%
Step:   190	 Loss:   25.67166	 Acc: 97.03%
Step:   200	 Loss:   24.73972	 Acc: 98.02%
Step:   210	 Loss:   23.87506	 Acc: 98.02%
Step:   220	 Loss:   23.07096	 Acc: 98.02%
Step:   230	 Loss:   22.32165	 Acc: 98.02%
Step:   240	 Loss:   21.62208	 Acc: 100.00%
Step:   250	 Loss:   20.96780	 Acc: 100.00%
Step:   260	 Loss:   20.35483	 Acc: 100.00%
Step:   270	 Loss:   19.77959	 Acc: 100.00%
Step:   280	 Loss:   19.23886	 Acc: 100.00%
Step:   290	 Loss:   18.72972	 Acc: 100.00%
Step:   300	 Loss:   18.24953	 Acc: 100.00%
Step:   310	 Loss:   17.79592	 Acc: 100.00%
Step:   320	 Loss:   17.36671	 Acc: 100.00%
Step:   330	 Loss:   16.95997	 Acc: 100.00%
Step:   340	 Loss:   16.57392	 Acc: 100.00%
Step:   350	 Loss:   16.20698	 Acc: 100.00%
Step:   360	 Loss:   15.85770	 Acc: 100.00%
Step:   370	 Loss:   15.52480	 Acc: 100.00%
Step:   380	 Loss:   15.20708	 Acc: 100.00%
Step:   390	 Loss:   14.90350	 Acc: 100.00%
Step:   400	 Loss:   14.61307	 Acc: 100.00%
Step:   410	 Loss:   14.33491	 Acc: 100.00%
Step:   420	 Loss:   14.06823	 Acc: 100.00%
Step:   430	 Loss:   13.81229	 Acc: 100.00%
Step:   440	 Loss:   13.56643	 Acc: 100.00%
Step:   450	 Loss:   13.33002	 Acc: 100.00%
Step:   460	 Loss:   13.10251	 Acc: 100.00%
Step:   470	 Loss:   12.88337	 Acc: 100.00%
Step:   480	 Loss:   12.67214	 Acc: 100.00%
Step:   490	 Loss:   12.46836	 Acc: 100.00%
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 4	 True y: 4
[True]	 Prediction: 4	 True y: 4
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 4	 True y: 4
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 2	 True y: 2
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 2	 True y: 2
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 2	 True y: 2
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 4	 True y: 4
[True]	 Prediction: 2	 True y: 2
[True]	 Prediction: 2	 True y: 2
[True]	 Prediction: 3	 True y: 3
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 1	 True y: 1
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 5	 True y: 5
[True]	 Prediction: 0	 True y: 0
[True]	 Prediction: 6	 True y: 6
[True]	 Prediction: 1	 True y: 1
'''