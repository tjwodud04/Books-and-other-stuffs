import tensorflow as tf
import numpy as np
import  matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

learning_rate = 0.01
training_epoch = 20
batch_size = 100
n_hidden = 256
n_input = 28 * 28

X = tf.placeholder(tf.float32, [None, n_input])

W_encode = tf.Variable(tf.random_normal([n_input, n_hidden]))
b_encode = tf.Variable(tf.random_normal([n_hidden]))
encoder = tf.nn.sigmoid(tf.add(tf.matmul(X, W_encode), b_encode))

W_decode = tf.Variable(tf.random_normal([n_hidden, n_input]))
b_decode = tf.Variable(tf.random_normal([n_input]))
decoder = tf.nn.sigmoid(tf.add(tf.matmul(encoder, W_decode), b_decode))

cost = tf.reduce_mean(tf.pow(X - decoder, 2))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(training_epoch):
    total_cost = 0
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs})
        total_cost += cost_val
    print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost =', '{:.4f}'.format(
        total_cost / total_batch))

print('최적화 완료!')

sample_size = 10

samples = sess.run(decoder, feed_dict={X: mnist.test.images[:sample_size]})

fig, ax = plt.subplots(2, sample_size, figsize=(sample_size, 2))

for i in range(sample_size):
    ax[0][i].set_axis_off()
    ax[1][i].set_axis_off()
    ax[0][i].imshow(np.reshape(mnist.test.images[i],(28,28)))
    ax[1][i].imshow(np.reshape(samples[i], (28,28)))

plt.show()

'''result
Epoch: 0001 Avg. cost = 0.2035
Epoch: 0002 Avg. cost = 0.0645
Epoch: 0003 Avg. cost = 0.0501
Epoch: 0004 Avg. cost = 0.0427
Epoch: 0005 Avg. cost = 0.0371
Epoch: 0006 Avg. cost = 0.0335
Epoch: 0007 Avg. cost = 0.0295
Epoch: 0008 Avg. cost = 0.0273
Epoch: 0009 Avg. cost = 0.0266
Epoch: 0010 Avg. cost = 0.0261
Epoch: 0011 Avg. cost = 0.0256
Epoch: 0012 Avg. cost = 0.0251
Epoch: 0013 Avg. cost = 0.0247
Epoch: 0014 Avg. cost = 0.0245
Epoch: 0015 Avg. cost = 0.0241
Epoch: 0016 Avg. cost = 0.0239
Epoch: 0017 Avg. cost = 0.0235
Epoch: 0018 Avg. cost = 0.0231
Epoch: 0019 Avg. cost = 0.0223
Epoch: 0020 Avg. cost = 0.0216
최적화 완료!
'''