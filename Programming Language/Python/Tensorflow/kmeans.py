'''
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf
from tensorflow.contrib.factorization import KMeans
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
full_data_x = mnist.train.images

num_steps = 50
batch_size = 1024
k = 25
num_classes = 10
num_features = 784

X = tf.placeholder(tf.float32, shape=[None, num_features])
Y = tf.placeholder(tf.float32, shape=[None, num_classes])

kmeans = KMeans(inputs=X, num_clusters=k, distance_metric='cosine', use_mini_batch=True)
training_graph = kmeans.training_graph()

if len(training_graph) > 6:
    (all_scores, cluster_idx, scores, cluster_centers_initialized,
     cluster_centers_var, init_op, train_op) = training_graph
else:
    (all_scores, cluster_idx, scores, cluster_centers_initialized,
     init_op, train_op) = training_graph

cluster_idx = cluster_idx[0]
avg_distance = tf.reduce_mean(scores)
init_vars = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init_vars, feed_dict={X: full_data_x})
sess.run(init_op, feed_dict={X: full_data_x})

for i in range(1, num_steps + 1):
    _, d, idx = sess.run([train_op, avg_distance, cluster_idx], feed_dict={X: full_data_x})
    if i % 10 == 0 or i == 1:
        print("단계 %i, 평균 거리: %f" % (i, d))

counts = np.zeros(shape=(k, num_classes))
for i in range(len(idx)):
    counts[idx[i]] += mnist.train.labels[i]

labels_map = [np.argmax(c) for c in counts]
labels_map = tf.convert_to_tensor(labels_map)
cluster_label = tf.nn.embedding_lookup(labels_map, cluster_idx)
correct_prediction = tf.equal(cluster_label, tf.cast(tf.argmax(Y, 1), tf.int32))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
test_x, test_y = mnist.test.images, mnist.test.labels

print("Test Accuracy:", sess.run(accuracy_op, feed_dict={X: test_x, Y: test_y}))

'''result
단계 1, 평균 거리: 0.341471
단계 10, 평균 거리: 0.221609
단계 20, 평균 거리: 0.220328
단계 30, 평균 거리: 0.219776
단계 40, 평균 거리: 0.219419
단계 50, 평균 거리: 0.219154
Test Accuracy: 0.7127
'''