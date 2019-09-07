import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

X = tf.placeholder(tf.float32, [None, 28,28,1])
Y = tf.placeholder(tf.float32, [None, 10])
is_training = tf.placeholder(tf.bool)

L1 = tf.layers.conv2d(X, 32, [3, 3], activation= tf.nn.relu,padding='SAME')
L1 = tf.layers.max_pooling2d(L1, [2, 2], [2, 2], padding='SAME')
L1 = tf.layers.dropout(L1, 0.7, is_training)

L2 = tf.layers.conv2d(L1, 64, [3, 3])
L2 = tf.layers.max_pooling2d(L1, [2, 2], [2, 2])
L2 = tf.layers.dropout(L2, 0.7, is_training)

L3 = tf.layers.flatten(L2)
L3 = tf.layers.dense(L3, 256, activation=tf.nn.relu)
L3 = tf.layers.dropout(L3, 0.5, is_training)

model = tf.layers.dense(L3, 10, activation=None)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(15):
    total_cost = 0
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        batch_xs = batch_xs.reshape(-1, 28, 28, 1)
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys, is_training: True})
        total_cost += cost_val
    print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost =', '{:.4f}'.format(
        total_cost / total_batch))

print('최적화 완료!')

is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도:', sess.run(accuracy,
                        feed_dict={X: mnist.test.images.reshape(-1,28,28,1), Y: mnist.test.labels, is_training: False}))

'''result
Epoch: 0001 Avg. cost = 0.2605
Epoch: 0002 Avg. cost = 0.0825
Epoch: 0003 Avg. cost = 0.0590
Epoch: 0004 Avg. cost = 0.0467
Epoch: 0005 Avg. cost = 0.0383
Epoch: 0006 Avg. cost = 0.0323
Epoch: 0007 Avg. cost = 0.0257
Epoch: 0008 Avg. cost = 0.0219
Epoch: 0009 Avg. cost = 0.0180
Epoch: 0010 Avg. cost = 0.0144
Epoch: 0011 Avg. cost = 0.0115
Epoch: 0012 Avg. cost = 0.0109
Epoch: 0013 Avg. cost = 0.0080
Epoch: 0014 Avg. cost = 0.0066
Epoch: 0015 Avg. cost = 0.0060
최적화 완료!
정확도: 0.9866
'''