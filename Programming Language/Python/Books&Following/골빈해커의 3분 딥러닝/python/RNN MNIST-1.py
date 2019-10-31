import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

learning_rate = 0.001
training_epoch = 30
batch_size = 128
n_hidden = 128
n_input = 28
n_step = 28
n_class = 10

X = tf.placeholder(tf.float32, [None, n_step, n_input])
Y = tf.placeholder(tf.float32, [None, n_class])

W = tf.Variable(tf.random_normal([n_hidden, n_class]))
b = tf.Variable(tf.random_normal([n_class]))

cell = tf.nn.rnn_cell.BasicRNNCell(n_hidden)
outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)

outputs = tf.transpose(outputs, [1, 0, 2])
outputs = outputs[-1]
model = tf.matmul(outputs, W) + b

cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())
total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(training_epoch):
    total_cost = 0
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape((batch_size, n_step, n_input))
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys})
        total_cost += cost_val
    print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost =', '{:.3f}'.format(
        total_cost / total_batch))

print('최적화 완료!')

is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
test_batch_size = len(mnist.test.images)
test_xs = mnist.test.images.reshape(test_batch_size, n_step, n_input)
test_ys = mnist.test.labels

print('정확도:', sess.run(accuracy,
                        feed_dict={X: test_xs, Y: test_ys}))

'''result
Epoch: 0001 Avg. cost = 0.529
Epoch: 0002 Avg. cost = 0.231
Epoch: 0003 Avg. cost = 0.186
Epoch: 0004 Avg. cost = 0.150
Epoch: 0005 Avg. cost = 0.141
Epoch: 0006 Avg. cost = 0.125
Epoch: 0007 Avg. cost = 0.120
Epoch: 0008 Avg. cost = 0.116
Epoch: 0009 Avg. cost = 0.103
Epoch: 0010 Avg. cost = 0.105
Epoch: 0011 Avg. cost = 0.100
Epoch: 0012 Avg. cost = 0.092
Epoch: 0013 Avg. cost = 0.097
Epoch: 0014 Avg. cost = 0.085
Epoch: 0015 Avg. cost = 0.086
Epoch: 0016 Avg. cost = 0.082
Epoch: 0017 Avg. cost = 0.083
Epoch: 0018 Avg. cost = 0.080
Epoch: 0019 Avg. cost = 0.076
Epoch: 0020 Avg. cost = 0.074
Epoch: 0021 Avg. cost = 0.073
Epoch: 0022 Avg. cost = 0.076
Epoch: 0023 Avg. cost = 0.067
Epoch: 0024 Avg. cost = 0.073
Epoch: 0025 Avg. cost = 0.067
Epoch: 0026 Avg. cost = 0.073
Epoch: 0027 Avg. cost = 0.066
Epoch: 0028 Avg. cost = 0.065
Epoch: 0029 Avg. cost = 0.066
Epoch: 0030 Avg. cost = 0.055
최적화 완료!
정확도: 0.9769
'''