import tensorflow as tf
import numpy as np

char_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

num_dic = {n: i for i, n in enumerate(char_arr)}
dic_len = len(num_dic)

seq_data = ['word', 'wood', 'deep', 'dive', 'cold', 'cool', 'load', 'love', 'kiss', 'kind']

def make_batch(seq_data):
    input_batch = []
    target_batch = []

    for seq in seq_data:
        input = [num_dic[n] for n in seq[:-1]]
        target = num_dic[seq[-1]]
        input_batch.append(np.eye(dic_len)[input])
        target_batch.append(target)
    return input_batch, target_batch

learning_rate = 0.01
n_hidden = 128
total_epoch = 30
n_step = 3
n_input = n_class = dic_len

X = tf.placeholder(tf.float32, [None, n_step, n_input])
Y = tf.placeholder(tf.int32, [None])

W = tf.Variable(tf.random_normal([n_hidden, n_class]))
b = tf.Variable(tf.random_normal([n_class]))

cell1 = tf.nn.rnn_cell.BasicLSTMCell(n_hidden)
cell1 = tf.nn.rnn_cell.DropoutWrapper(cell1, output_keep_prob=0.5)
cell2 = tf.nn.rnn_cell.BasicLSTMCell(n_hidden)
multi_cell =  tf.nn.rnn_cell.MultiRNNCell([cell1, cell2])

outputs, states = tf.nn.dynamic_rnn(multi_cell, X, dtype=tf.float32)

outputs = tf.transpose(outputs, [1, 0, 2])
outputs = outputs[-1]
model = tf.matmul(outputs, W) + b

cost = tf.reduce_mean(
    tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

input_batch, target_batch = make_batch(seq_data)

for epoch in range(total_epoch):
    _, loss = sess.run([optimizer, cost], feed_dict={X: input_batch, Y: target_batch})
    print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost =', '{:.6f}'.format(loss))

print('최적화 완료!')

prediction = tf.cast(tf.argmax(model, 1), tf.int32)
prediction_check = tf.equal(prediction, Y)
accuracy = tf.reduce_mean(tf.cast(prediction_check, tf.float32))
input_batch, target_batch = make_batch(seq_data)
predict, accuracy_val = sess.run([prediction, accuracy], feed_dict={X:input_batch, Y:target_batch})

predict_words = []
for idx, val in enumerate(seq_data):
    last_char = char_arr[predict[idx]]
    predict_words.append(val[:3] + last_char)

print('\n=== 예측 결과 ===')
print('입력값:', [w[:3] + ' ' for w in seq_data])
print('예측값:', predict_words)
print('정확도:', accuracy_val)

'''result
Epoch: 0001 Avg. cost = 3.305068
Epoch: 0002 Avg. cost = 2.482345
Epoch: 0003 Avg. cost = 1.624286
Epoch: 0004 Avg. cost = 0.946380
Epoch: 0005 Avg. cost = 0.841605
Epoch: 0006 Avg. cost = 0.603073
Epoch: 0007 Avg. cost = 0.618644
Epoch: 0008 Avg. cost = 0.426482
Epoch: 0009 Avg. cost = 0.152803
Epoch: 0010 Avg. cost = 0.415074
Epoch: 0011 Avg. cost = 0.210360
Epoch: 0012 Avg. cost = 0.135979
Epoch: 0013 Avg. cost = 0.166849
Epoch: 0014 Avg. cost = 0.188329
Epoch: 0015 Avg. cost = 0.235793
Epoch: 0016 Avg. cost = 0.202626
Epoch: 0017 Avg. cost = 0.352821
Epoch: 0018 Avg. cost = 0.288223
Epoch: 0019 Avg. cost = 0.089981
Epoch: 0020 Avg. cost = 0.495442
Epoch: 0021 Avg. cost = 0.415876
Epoch: 0022 Avg. cost = 0.057750
Epoch: 0023 Avg. cost = 0.146925
Epoch: 0024 Avg. cost = 0.056294
Epoch: 0025 Avg. cost = 0.046548
Epoch: 0026 Avg. cost = 0.084488
Epoch: 0027 Avg. cost = 0.034583
Epoch: 0028 Avg. cost = 0.067940
Epoch: 0029 Avg. cost = 0.075463
Epoch: 0030 Avg. cost = 0.011219
최적화 완료!

=== 예측 결과 ===
입력값: ['wor ', 'woo ', 'dee ', 'div ', 'col ', 'coo ', 'loa ', 'lov ', 'kis ', 'kin ']
예측값: ['word', 'wood', 'deep', 'dive', 'cold', 'cool', 'load', 'love', 'kiss', 'kind']
정확도: 1.0
'''