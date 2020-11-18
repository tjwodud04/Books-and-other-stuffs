import tensorflow as tf
import numpy as np
import  matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

total_epoch = 100
batch_size = 100
n_hidden = 256
n_input = 28 * 28
n_noise = 128
n_class = 10

X = tf.placeholder(tf.float32, [None, n_input])
Y = tf.placeholder(tf.float32, [None, n_class])
Z = tf.placeholder(tf.float32, [None, n_noise])

def generator(noise, labels):
    with tf.variable_scope('generator'):
        inputs = tf.concat([noise, labels], 1)
        hidden = tf.layers.dense(inputs, n_hidden, activation=tf.nn.relu)
        output = tf.layers.dense(hidden, n_input, activation=tf.nn.relu)
    return output

def discriminator(inputs, labels, reuse=None):
    with tf.variable_scope('discriminator') as scope:
        if reuse:
            scope.reuse_variables()
        inputs = tf.concat([inputs, labels], 1)
        hidden = tf.layers.dense(inputs, n_hidden, activation=tf.nn.relu)
        output = tf.layers.dense(hidden, 1, activation=None)
    return output

def get_noise(batch_size, n_noise):
    return np.random.uniform(-1., 1., size=[batch_size, n_noise])

G = generator(Z, Y)
D_real = discriminator(X, Y)
D_gene = discriminator(G, Y, True)

loss_D_real = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=D_real, labels=tf.ones_like(D_real)))
loss_D_gene = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=D_gene, labels=tf.zeros_like(D_gene)))

loss_D = loss_D_real + loss_D_gene
loss_G = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=D_gene, labels=tf.ones_like(D_gene)))

vars_D = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='discriminator')
vars_G = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='generator')

train_D = tf.train.AdamOptimizer().minimize(loss_D, var_list=vars_D)
train_G = tf.train.AdamOptimizer().minimize(loss_G, var_list=vars_G)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

total_batch = int(mnist.train.num_examples / batch_size)
loss_val_D, loss_val_G = 0, 0

for epoch in range(total_epoch):
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        noise = get_noise(batch_size, n_noise)
        _, loss_val_D = sess.run([train_D, loss_D], feed_dict={X: batch_xs, Y: batch_ys, Z: noise})
        _, loss_val_G = sess.run([train_G, loss_G], feed_dict={Y: batch_ys, Z: noise})
    print('Epoch:', '%04d' % (epoch + 1), 'D loss: {:.4}'.format(
        loss_val_D), 'G loss: {:.4}'.format(
        loss_val_G))

if epoch == 0 or (epoch + 1) % 10 == 0:
    sample_size = 10
    noise = get_noise(sample_size, n_noise)
    samples = sess.run(G, feed_dict={Y: mnist.test.labels[:sample_size], Z: noise})

    fig, ax = plt.subplots(2, sample_size, figsize=(sample_size, 2))

    for i in range(sample_size):
        ax[0][i].set_axis_off()
        ax[1][i].set_axis_off()
        ax[0][i].imshow(np.reshape(mnist.test.images[i],(28,28)))
        ax[1][i].imshow(np.reshape(samples[i], (28,28)))
    plt.savefig('samples2/{}.png'.format(str(epoch).zfill(3)), bbox_inches='tight')
    plt.close(fig)

print('최적화 완료!')

'''result
Epoch: 0000 D loss: 0.01164 G loss: 7.482
Epoch: 0001 D loss: 0.003262 G loss: 9.411
Epoch: 0002 D loss: 0.005903 G loss: 7.406
Epoch: 0003 D loss: 0.003902 G loss: 8.641
Epoch: 0004 D loss: 0.0254 G loss: 9.228
Epoch: 0005 D loss: 0.006446 G loss: 7.748
Epoch: 0006 D loss: 0.01496 G loss: 7.095
Epoch: 0007 D loss: 0.05254 G loss: 6.747
Epoch: 0008 D loss: 0.08779 G loss: 7.017
Epoch: 0009 D loss: 0.1079 G loss: 6.719
Epoch: 0010 D loss: 0.09162 G loss: 6.497
Epoch: 0011 D loss: 0.1761 G loss: 5.903
Epoch: 0012 D loss: 0.2178 G loss: 4.3
Epoch: 0013 D loss: 0.2713 G loss: 4.867
Epoch: 0014 D loss: 0.3472 G loss: 4.482
Epoch: 0015 D loss: 0.5564 G loss: 3.617
Epoch: 0016 D loss: 0.4494 G loss: 3.403
Epoch: 0017 D loss: 0.4506 G loss: 3.177
Epoch: 0018 D loss: 0.5611 G loss: 3.616
Epoch: 0019 D loss: 0.3808 G loss: 3.623
Epoch: 0020 D loss: 0.4956 G loss: 3.039
Epoch: 0021 D loss: 0.5526 G loss: 2.657
Epoch: 0022 D loss: 0.6547 G loss: 3.457
Epoch: 0023 D loss: 0.4959 G loss: 3.273
Epoch: 0024 D loss: 0.7739 G loss: 2.663
Epoch: 0025 D loss: 0.7535 G loss: 2.26
Epoch: 0026 D loss: 0.6097 G loss: 2.265
Epoch: 0027 D loss: 0.5365 G loss: 2.729
Epoch: 0028 D loss: 0.7975 G loss: 2.292
Epoch: 0029 D loss: 0.4946 G loss: 2.956
Epoch: 0030 D loss: 0.7583 G loss: 2.646
Epoch: 0031 D loss: 0.7775 G loss: 2.601
Epoch: 0032 D loss: 0.7891 G loss: 2.059
Epoch: 0033 D loss: 0.6987 G loss: 2.197
Epoch: 0034 D loss: 0.6298 G loss: 2.407
Epoch: 0035 D loss: 0.7241 G loss: 2.149
Epoch: 0036 D loss: 0.6196 G loss: 2.126
Epoch: 0037 D loss: 0.6696 G loss: 2.476
Epoch: 0038 D loss: 0.5984 G loss: 1.949
Epoch: 0039 D loss: 0.8417 G loss: 1.878
Epoch: 0040 D loss: 0.7528 G loss: 2.354
Epoch: 0041 D loss: 0.72 G loss: 1.932
Epoch: 0042 D loss: 0.6186 G loss: 2.924
Epoch: 0043 D loss: 0.7211 G loss: 1.946
Epoch: 0044 D loss: 0.7471 G loss: 2.018
Epoch: 0045 D loss: 0.6432 G loss: 2.463
Epoch: 0046 D loss: 0.8119 G loss: 1.962
Epoch: 0047 D loss: 0.6828 G loss: 2.24
Epoch: 0048 D loss: 0.7224 G loss: 2.43
Epoch: 0049 D loss: 0.8788 G loss: 1.971
Epoch: 0050 D loss: 0.7301 G loss: 1.961
Epoch: 0051 D loss: 0.6708 G loss: 2.474
Epoch: 0052 D loss: 0.8342 G loss: 1.921
Epoch: 0053 D loss: 0.7991 G loss: 2.119
Epoch: 0054 D loss: 0.6846 G loss: 2.19
Epoch: 0055 D loss: 0.7266 G loss: 2.028
Epoch: 0056 D loss: 0.7785 G loss: 2.397
Epoch: 0057 D loss: 0.7179 G loss: 2.03
Epoch: 0058 D loss: 0.7363 G loss: 2.049
Epoch: 0059 D loss: 0.5349 G loss: 2.356
Epoch: 0060 D loss: 0.6587 G loss: 2.298
Epoch: 0061 D loss: 0.6622 G loss: 2.173
Epoch: 0062 D loss: 0.8151 G loss: 2.119
Epoch: 0063 D loss: 0.6871 G loss: 2.328
Epoch: 0064 D loss: 0.7468 G loss: 2.337
Epoch: 0065 D loss: 0.7685 G loss: 1.987
Epoch: 0066 D loss: 0.8185 G loss: 2.422
Epoch: 0067 D loss: 0.74 G loss: 2.097
Epoch: 0068 D loss: 0.7151 G loss: 1.955
Epoch: 0069 D loss: 0.6125 G loss: 2.466
Epoch: 0070 D loss: 0.6583 G loss: 1.901
Epoch: 0071 D loss: 0.9263 G loss: 1.83
Epoch: 0072 D loss: 0.7153 G loss: 1.928
Epoch: 0073 D loss: 0.6379 G loss: 2.195
Epoch: 0074 D loss: 0.7931 G loss: 1.853
Epoch: 0075 D loss: 0.7471 G loss: 2.409
Epoch: 0076 D loss: 0.6825 G loss: 1.789
Epoch: 0077 D loss: 0.6244 G loss: 2.343
Epoch: 0078 D loss: 0.6793 G loss: 1.843
Epoch: 0079 D loss: 0.8095 G loss: 2.277
Epoch: 0080 D loss: 0.8414 G loss: 2.076
Epoch: 0081 D loss: 0.7936 G loss: 1.713
Epoch: 0082 D loss: 0.686 G loss: 2.036
Epoch: 0083 D loss: 0.6561 G loss: 2.339
Epoch: 0084 D loss: 0.7981 G loss: 2.142
Epoch: 0085 D loss: 0.6705 G loss: 2.004
Epoch: 0086 D loss: 0.8394 G loss: 2.072
Epoch: 0087 D loss: 0.8997 G loss: 1.597
Epoch: 0088 D loss: 0.7285 G loss: 2.076
Epoch: 0089 D loss: 0.6244 G loss: 2.429
Epoch: 0090 D loss: 0.7533 G loss: 1.808
Epoch: 0091 D loss: 0.7328 G loss: 2.151
Epoch: 0092 D loss: 0.6712 G loss: 2.203
Epoch: 0093 D loss: 0.7264 G loss: 1.847
Epoch: 0094 D loss: 0.7146 G loss: 1.979
Epoch: 0095 D loss: 0.7361 G loss: 2.153
Epoch: 0096 D loss: 0.7096 G loss: 1.925
Epoch: 0097 D loss: 0.5528 G loss: 2.362
Epoch: 0098 D loss: 0.7797 G loss: 1.978
Epoch: 0099 D loss: 0.6278 G loss: 2.138
최적화 완료!
'''