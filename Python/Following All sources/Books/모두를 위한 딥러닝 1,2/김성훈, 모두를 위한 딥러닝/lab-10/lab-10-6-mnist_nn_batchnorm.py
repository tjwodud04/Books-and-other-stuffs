import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

print(mnist.train.images.shape)
'''result
(55000, 784)
'''

class Model:
    def __init__(self, name, input_dim, output_dim, hidden_dims=[32, 32], use_batchnorm=True, activation_fn=tf.nn.relu,
                 optimizer=tf.train.AdamOptimizer, lr=0.01):
        with tf.variable_scope(name):
            self.X = tf.placeholder(tf.float32, [None, input_dim], name='X')
            self.y = tf.placeholder(tf.float32, [None, output_dim], name='y')
            self.mode = tf.placeholder(tf.bool, name='train_mode')
            net = self.X

            for i, h_dim in enumerate(hidden_dims):
                with tf.variable_scope('layer{}'.format(i)):
                    net = tf.layers.dense(net, h_dim)

                    if use_batchnorm:
                        net = tf.layers.batch_normalization(net, training=self.mode)

                    net = activation_fn(net)

            net = tf.contrib.layers.flatten(net)
            net = tf.layers.dense(net, output_dim)

            self.loss = tf.nn.softmax_cross_entropy_with_logits(logits=net, labels=self.y)
            self.loss = tf.reduce_mean(self.loss, name='loss')

            update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS, scope=name)
            with tf.control_dependencies(update_ops):
                self.train_op = optimizer(lr).minimize(self.loss)

            softmax = tf.nn.softmax(net, name='softmax')
            self.accuracy = tf.equal(tf.argmax(softmax, 1), tf.argmax(self.y, 1))
            self.accuracy = tf.reduce_mean(tf.cast(self.accuracy, tf.float32))

class Solver:
    def __init__(self, sess, model):
        self.model = model
        self.sess = sess

    def train(self, X, y):
        feed = {
            self.model.X: X,
            self.model.y: y,
            self.model.mode: True
        }
        train_op = self.model.train_op
        loss = self.model.loss

        return self.sess.run([train_op, loss], feed_dict=feed)

    def evaluate(self, X, y, batch_size=None):
        if batch_size:
            N = X.shape[0]

            total_loss = 0
            total_acc = 0

            for i in range(0, N, batch_size):
                X_batch = X[i:i + batch_size]
                y_batch = y[i:i + batch_size]

                feed = {
                    self.model.X: X_batch,
                    self.model.y: y_batch,
                    self.model.mode: False
                }

                loss = self.model.loss
                accuracy = self.model.accuracy

                step_loss, step_acc = self.sess.run([loss, accuracy], feed_dict=feed)

                total_loss += step_loss * X_batch.shape[0]
                total_acc += step_acc * X_batch.shape[0]

            total_loss /= N
            total_acc /= N

            return total_loss, total_acc

        else:
            feed = {
                self.model.X: X,
                self.model.y: y,
                self.model.mode: False
            }

            loss = self.model.loss
            accuracy = self.model.accuracy

            return self.sess.run([loss, accuracy], feed_dict=feed)

input_dim = 784
output_dim = 10
N = 55000

tf.reset_default_graph()
sess = tf.InteractiveSession()

bn = Model('batchnorm', input_dim, output_dim, use_batchnorm=True)
nn = Model('no_norm', input_dim, output_dim, use_batchnorm=False)
bn_solver = Solver(sess, bn)
nn_solver = Solver(sess, nn)

epoch_n = 10
batch_size = 32

train_losses = []
train_accs = []

valid_losses = []
valid_accs = []

init = tf.global_variables_initializer()
sess.run(init)

for epoch in range(epoch_n):
    for _ in range(N // batch_size):
        X_batch, y_batch = mnist.train.next_batch(batch_size)

        _, bn_loss = bn_solver.train(X_batch, y_batch)
        _, nn_loss = nn_solver.train(X_batch, y_batch)

    b_loss, b_acc = bn_solver.evaluate(mnist.train.images, mnist.train.labels, batch_size)
    n_loss, n_acc = nn_solver.evaluate(mnist.train.images, mnist.train.labels, batch_size)

    train_losses.append([b_loss, n_loss])
    train_accs.append([b_acc, n_acc])
    print(
        f'[Epoch {epoch}-TRAIN] Batchnorm Loss(Acc): {b_loss:.5f}({b_acc:.2%}) vs No Batchnorm Loss(Acc): {n_loss:.5f}({n_acc:.2%})')

    b_loss, b_acc = bn_solver.evaluate(mnist.validation.images, mnist.validation.labels)
    n_loss, n_acc = nn_solver.evaluate(mnist.validation.images, mnist.validation.labels)

    valid_losses.append([b_loss, n_loss])
    valid_accs.append([b_acc, n_acc])
    print(
        f'[Epoch {epoch}-VALID] Batchnorm Loss(Acc): {b_loss:.5f}({b_acc:.2%}) vs No Batchnorm Loss(Acc): {n_loss:.5f}({n_acc:.2%})')
    print()

'''result
[Epoch 0-TRAIN] Batchnorm Loss(Acc): 0.13882(95.69%) vs No Batchnorm Loss(Acc): 0.23722(93.01%)
[Epoch 0-VALID] Batchnorm Loss(Acc): 0.15276(95.46%) vs No Batchnorm Loss(Acc): 0.25612(93.08%)

[Epoch 1-TRAIN] Batchnorm Loss(Acc): 0.10808(96.63%) vs No Batchnorm Loss(Acc): 0.17144(95.08%)
[Epoch 1-VALID] Batchnorm Loss(Acc): 0.12606(96.38%) vs No Batchnorm Loss(Acc): 0.18311(95.28%)

[Epoch 2-TRAIN] Batchnorm Loss(Acc): 0.10635(96.71%) vs No Batchnorm Loss(Acc): 0.16905(95.25%)
[Epoch 2-VALID] Batchnorm Loss(Acc): 0.12869(96.48%) vs No Batchnorm Loss(Acc): 0.19350(95.02%)

[Epoch 3-TRAIN] Batchnorm Loss(Acc): 0.08368(97.43%) vs No Batchnorm Loss(Acc): 0.16245(95.44%)
[Epoch 3-VALID] Batchnorm Loss(Acc): 0.11088(96.98%) vs No Batchnorm Loss(Acc): 0.18880(94.96%)

[Epoch 4-TRAIN] Batchnorm Loss(Acc): 0.06473(98.03%) vs No Batchnorm Loss(Acc): 0.14620(96.02%)
[Epoch 4-VALID] Batchnorm Loss(Acc): 0.09965(97.12%) vs No Batchnorm Loss(Acc): 0.18223(95.66%)

[Epoch 5-TRAIN] Batchnorm Loss(Acc): 0.06258(98.08%) vs No Batchnorm Loss(Acc): 0.12623(96.47%)
[Epoch 5-VALID] Batchnorm Loss(Acc): 0.09342(97.44%) vs No Batchnorm Loss(Acc): 0.16034(95.70%)

[Epoch 6-TRAIN] Batchnorm Loss(Acc): 0.05566(98.27%) vs No Batchnorm Loss(Acc): 0.12514(96.52%)
[Epoch 6-VALID] Batchnorm Loss(Acc): 0.09826(97.36%) vs No Batchnorm Loss(Acc): 0.16888(95.98%)

[Epoch 7-TRAIN] Batchnorm Loss(Acc): 0.06427(97.96%) vs No Batchnorm Loss(Acc): 0.14058(96.13%)
[Epoch 7-VALID] Batchnorm Loss(Acc): 0.10927(96.84%) vs No Batchnorm Loss(Acc): 0.19691(95.52%)

[Epoch 8-TRAIN] Batchnorm Loss(Acc): 0.04898(98.51%) vs No Batchnorm Loss(Acc): 0.11428(96.79%)
[Epoch 8-VALID] Batchnorm Loss(Acc): 0.08803(97.54%) vs No Batchnorm Loss(Acc): 0.17764(95.70%)

[Epoch 9-TRAIN] Batchnorm Loss(Acc): 0.05045(98.38%) vs No Batchnorm Loss(Acc): 0.11396(96.99%)
[Epoch 9-VALID] Batchnorm Loss(Acc): 0.09400(97.50%) vs No Batchnorm Loss(Acc): 0.18394(95.80%)
'''

print(bn_solver.evaluate(mnist.test.images, mnist.test.labels))
print(nn_solver.evaluate(mnist.test.images, mnist.test.labels))

'''result
[0.103145815, 0.9704]
[0.18223572, 0.9576]
'''

def plot_compare(loss_list: list, ylim=None, title=None) -> None:
    bn = [i[0] for i in loss_list]
    nn = [i[1] for i in loss_list]

    plt.figure(figsize=(15, 10))
    plt.plot(bn, label='With BN')
    plt.plot(nn, label='Without BN')
    if ylim:
        plt.ylim(ylim)

    if title:
        plt.title(title)
    plt.legend()
    plt.grid('on')
    plt.show()

plot_compare(train_losses, title='Training Loss at Epoch')
plot_compare(train_accs, [0, 1.0], title="Training Acc at Epoch")
plot_compare(valid_losses, title='Validation Loss at Epoch')
plot_compare(valid_accs, [0, 1.], title='Validation Acc at Epoch')
