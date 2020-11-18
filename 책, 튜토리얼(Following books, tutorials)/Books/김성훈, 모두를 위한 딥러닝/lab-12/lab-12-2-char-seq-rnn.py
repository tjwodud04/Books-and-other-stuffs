import tensorflow as tf
import numpy as np
tf.set_random_seed(777)

sample = " if you want you"
idx2char = list(set(sample))
char2idx = {c: i for i, c in enumerate(idx2char)}

dic_size = len(char2idx)
hidden_size = len(char2idx)
num_classes = len(char2idx)
batch_size = 1
sequence_length = len(sample) - 1
learning_rate = 0.1

sample_idx = [char2idx[c] for c in sample]
x_data = [sample_idx[:-1]]
y_data = [sample_idx[1:]]

X = tf.placeholder(tf.int32, [None, sequence_length])
Y = tf.placeholder(tf.int32, [None, sequence_length])

x_one_hot = tf.one_hot(X, num_classes)
cell = tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size, state_is_tuple=True)
initial_state = cell.zero_state(batch_size, tf.float32)
outputs, _states = tf.nn.dynamic_rnn(cell, x_one_hot, initial_state=initial_state, dtype=tf.float32)

X_for_fc = tf.reshape(outputs, [-1, hidden_size])
outputs = tf.contrib.layers.fully_connected(X_for_fc, num_classes, activation_fn=None)

outputs = tf.reshape(outputs, [batch_size, sequence_length, num_classes])

weights = tf.ones([batch_size, sequence_length])
sequence_loss = tf.contrib.seq2seq.sequence_loss(logits=outputs, targets=Y, weights=weights)
loss = tf.reduce_mean(sequence_loss)
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)

prediction = tf.argmax(outputs, axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(50):
        l, _ = sess.run([loss, train], feed_dict={X: x_data, Y: y_data})
        result = sess.run(prediction, feed_dict={X: x_data})
        result_str = [idx2char[c] for c in np.squeeze(result)]
        print(i, "loss:", l, "Prediction:", ''.join(result_str))

''' result
0 loss: 2.2666504 Prediction: y  yyuyyyyyyyyy
1 loss: 2.0822308 Prediction: y   ou   o   ou
2 loss: 1.8820318 Prediction: y   uu       uu
3 loss: 1.6487232 Prediction: y   ou  ay  yuu
4 loss: 1.3983546 Prediction: y  you wan  you
5 loss: 1.1119218 Prediction: y  you wan  you
6 loss: 0.84018695 Prediction: yf you wan  you
7 loss: 0.6318382 Prediction: yf you want you
8 loss: 0.45192415 Prediction: if you want you
9 loss: 0.32623404 Prediction: if you want you
10 loss: 0.23212156 Prediction: if you want you
11 loss: 0.16584498 Prediction: if you want you
12 loss: 0.11478365 Prediction: if you want you
13 loss: 0.07848178 Prediction: if you want you
14 loss: 0.053977422 Prediction: if you want you
15 loss: 0.037210505 Prediction: if you want you
16 loss: 0.02582115 Prediction: if you want you
17 loss: 0.01830291 Prediction: if you want you
18 loss: 0.013437038 Prediction: if you want you
19 loss: 0.01024137 Prediction: if you want you
20 loss: 0.008035907 Prediction: if you want you
21 loss: 0.0064241784 Prediction: if you want you
22 loss: 0.005197394 Prediction: if you want you
23 loss: 0.0042452863 Prediction: if you want you
24 loss: 0.0035021226 Prediction: if you want you
25 loss: 0.0029218355 Prediction: if you want you
26 loss: 0.0024685482 Prediction: if you want you
27 loss: 0.0021135323 Prediction: if you want you
28 loss: 0.0018340044 Prediction: if you want you
29 loss: 0.001612374 Prediction: if you want you
30 loss: 0.001434804 Prediction: if you want you
31 loss: 0.0012910267 Prediction: if you want you
32 loss: 0.0011729213 Prediction: if you want you
33 loss: 0.0010745148 Prediction: if you want you
34 loss: 0.0009911435 Prediction: if you want you
35 loss: 0.0009195056 Prediction: if you want you
36 loss: 0.00085701776 Prediction: if you want you
37 loss: 0.00080199266 Prediction: if you want you
38 loss: 0.00075313833 Prediction: if you want you
39 loss: 0.0007097338 Prediction: if you want you
40 loss: 0.00067095447 Prediction: if you want you
41 loss: 0.00063638843 Prediction: if you want you
42 loss: 0.0006056314 Prediction: if you want you
43 loss: 0.00057827093 Prediction: if you want you
44 loss: 0.0005539345 Prediction: if you want you
45 loss: 0.00053230475 Prediction: if you want you
46 loss: 0.0005130008 Prediction: if you want you
47 loss: 0.0004958087 Prediction: if you want you
48 loss: 0.0004804505 Prediction: if you want you
49 loss: 0.0004666087 Prediction: if you want you
'''
