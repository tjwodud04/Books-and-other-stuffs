import tensorflow as tf
import random
import os
from tensorflow.examples.tutorials.mnist import input_data

tf.set_random_seed(777)

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

learning_rate = 0.001
training_epochs = 15
batch_size = 100

CHECK_POINT_DIR = TB_SUMMARY_DIR = './tb/mnist2'

X = tf.placeholder(tf.float32, [None, 784])
Y = tf.placeholder(tf.float32, [None, 10])

x_image = tf.reshape(X, [-1, 28, 28, 1])
tf.summary.image('input', x_image, 3)
keep_prob = tf.placeholder(tf.float32)

with tf.variable_scope('layer1'):
    W1 = tf.get_variable("W", shape=[784, 512], initializer=tf.contrib.layers.xavier_initializer())
    b1 = tf.Variable(tf.random_normal([512]))
    L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
    L1 = tf.nn.dropout(L1, keep_prob=keep_prob)

    tf.summary.histogram("X", X)
    tf.summary.histogram("weights", W1)
    tf.summary.histogram("bias", b1)
    tf.summary.histogram("layer", L1)

with tf.variable_scope('layer2'):
    W2 = tf.get_variable("W", shape=[512, 512], initializer=tf.contrib.layers.xavier_initializer())
    b2 = tf.Variable(tf.random_normal([512]))
    L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
    L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

    tf.summary.histogram("weights", W2)
    tf.summary.histogram("bias", b2)
    tf.summary.histogram("layer", L2)

with tf.variable_scope('layer3'):
    W3 = tf.get_variable("W", shape=[512, 512], initializer=tf.contrib.layers.xavier_initializer())
    b3 = tf.Variable(tf.random_normal([512]))
    L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
    L3 = tf.nn.dropout(L3, keep_prob=keep_prob)

    tf.summary.histogram("weights", W3)
    tf.summary.histogram("bias", b3)
    tf.summary.histogram("layer", L3)

with tf.variable_scope('layer4'):
    W4 = tf.get_variable("W", shape=[512, 512], initializer=tf.contrib.layers.xavier_initializer())
    b4 = tf.Variable(tf.random_normal([512]))
    L4 = tf.nn.relu(tf.matmul(L3, W4) + b4)
    L4 = tf.nn.dropout(L4, keep_prob=keep_prob)

    tf.summary.histogram("weights", W4)
    tf.summary.histogram("bias", b4)
    tf.summary.histogram("layer", L4)

with tf.variable_scope('layer5'):
    W5 = tf.get_variable("W", shape=[512, 10], initializer=tf.contrib.layers.xavier_initializer())
    b5 = tf.Variable(tf.random_normal([10]))
    hypothesis = tf.matmul(L4, W5) + b5

    tf.summary.histogram("weights", W5)
    tf.summary.histogram("bias", b5)
    tf.summary.histogram("hypothesis", hypothesis)

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

tf.summary.scalar("loss", cost)
last_epoch = tf.Variable(0, name='last_epoch')
summary = tf.summary.merge_all()

sess = tf.Session()
sess.run(tf.global_variables_initializer())

writer = tf.summary.FileWriter(TB_SUMMARY_DIR)
writer.add_graph(sess.graph)
global_step = 0

saver = tf.train.Saver()
checkpoint = tf.train.get_checkpoint_state(CHECK_POINT_DIR)

if checkpoint and checkpoint.model_checkpoint_path:
    try:
        saver.restore(sess, checkpoint.model_checkpoint_path)
        print("Successfully loaded:", checkpoint.model_checkpoint_path)
    except:
        print("Error on loading old network weights")
else:
    print("Could not find old network weights")

start_from = sess.run(last_epoch)

print('Start learning from:', start_from)

for epoch in range(start_from, training_epochs):
    print('Start Epoch:', epoch)

    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.7}
        s, _ = sess.run([summary, optimizer], feed_dict=feed_dict)
        writer.add_summary(s, global_step=global_step)
        global_step += 1

        avg_cost += sess.run(cost, feed_dict=feed_dict) / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

    print("Saving network...")
    sess.run(last_epoch.assign(epoch + 1))
    if not os.path.exists(CHECK_POINT_DIR):
        os.makedirs(CHECK_POINT_DIR)
    saver.save(sess, CHECK_POINT_DIR + "/model", global_step=i)

print('Learning Finished!')

correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print('Accuracy:', sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels, keep_prob: 1}))

r = random.randint(0, mnist.test.num_examples - 1)
print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print("Prediction: ", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1], keep_prob: 1}))

''' result
Could not find old network weights
Start learning from: 0
Start Epoch: 0
Epoch: 0001 cost = 0.436934359
Saving network...
Start Epoch: 1
Epoch: 0002 cost = 0.159913032
Saving network...
Start Epoch: 2
Epoch: 0003 cost = 0.116018058
Saving network...
Start Epoch: 3
Epoch: 0004 cost = 0.096681275
Saving network...
Start Epoch: 4
Epoch: 0005 cost = 0.084224471
Saving network...
Start Epoch: 5
Epoch: 0006 cost = 0.074105245
Saving network...
Start Epoch: 6
Epoch: 0007 cost = 0.066751829
Saving network...
Start Epoch: 7
Epoch: 0008 cost = 0.058470142
Saving network...
Start Epoch: 8
Epoch: 0009 cost = 0.053073334
Saving network...
Start Epoch: 9
Epoch: 0010 cost = 0.050898358
Saving network...
Start Epoch: 10
Epoch: 0011 cost = 0.048577384
Saving network...
Start Epoch: 11
Epoch: 0012 cost = 0.045724012
Saving network...
Start Epoch: 12
Epoch: 0013 cost = 0.042662907
Saving network...
Start Epoch: 13
Epoch: 0014 cost = 0.040346368
Saving network...
Start Epoch: 14
Epoch: 0015 cost = 0.039371884
Saving network...
Learning Finished!
Accuracy: 0.983
Label:  [0]
Prediction:  [0]
'''
