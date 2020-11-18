import tensorflow as tf
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=False)

num_steps = 500
batch_size = 1024
num_classes = 10
num_features = 784
num_trees = 10
max_nodes = 1000

X = tf.placeholder(tf.float32, shape=[None, num_features])
Y = tf.placeholder(tf.int32, shape=[None])

hparams = tensor_forest.ForestHParams(num_classes=num_classes,
                                      num_features=num_features,
                                      num_trees=num_trees,
                                      max_nodes=max_nodes).fill()

forest_graph = tensor_forest.RandomForestGraphs(hparams)

train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

infer_op, _, _ = forest_graph.inference_graph(X)
correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64))
accuracy_op = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

init_vars = tf.group(tf.global_variables_initializer(),
    resources.initialize_resources(resources.shared_resources()))

sess = tf.Session()
sess.run(init_vars)

for i in range(1, num_steps + 1):
    batch_x, batch_y = mnist.train.next_batch(batch_size)
    _, l = sess.run([train_op, loss_op], feed_dict={X: batch_x, Y: batch_y})
    if i % 50 == 0 or i == 1:
        acc = sess.run(accuracy_op, feed_dict={X: batch_x, Y: batch_y})
        print('Step %i, Loss: %f, Acc: %f' % (i, l, acc))

test_x, test_y = mnist.test.images, mnist.test.labels

print("Test Accuracy:", sess.run(accuracy_op, feed_dict={X: test_x, Y: test_y}))

'''result
Step 1, Loss: -1.000000, Acc: 0.373047
Step 50, Loss: -255.600006, Acc: 0.893555
Step 100, Loss: -543.000000, Acc: 0.905273
Step 150, Loss: -828.000000, Acc: 0.924805
Step 200, Loss: -1001.000000, Acc: 0.936523
Step 250, Loss: -1001.000000, Acc: 0.926758
Step 300, Loss: -1001.000000, Acc: 0.926758
Step 350, Loss: -1001.000000, Acc: 0.930664
Step 400, Loss: -1001.000000, Acc: 0.921875
Step 450, Loss: -1001.000000, Acc: 0.914062
Step 500, Loss: -1001.000000, Acc: 0.927734
Test Accuracy: 0.9235
'''