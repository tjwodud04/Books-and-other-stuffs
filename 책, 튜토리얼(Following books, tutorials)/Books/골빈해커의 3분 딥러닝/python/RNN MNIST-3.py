import tensorflow as tf
import numpy as np

char_arr = [c for c in 'SEPabcdefghijklmnopqrstuvwxyz단어나무놀이소녀키스사랑']
num_dic = {n: i for i, n in enumerate(char_arr)}
dic_len = len(num_dic)

seq_data = [['word', '단어'], ['wood', '나무'],
            ['game', '놀이'], ['girl', '소녀'],
            ['kiss', '키스'], ['love', '사랑']]

def make_batch(seq_data):
    input_batch = []
    output_batch = []
    target_batch = []

    for seq in seq_data:
        input = [num_dic[n] for n in seq[0]]
        output = [num_dic[n] for n in ('S' + seq[1])]
        target = [num_dic[n] for n in (seq[-1] + 'E')]
        input_batch.append(np.eye(dic_len)[input])
        output_batch.append(np.eye(dic_len)[output])
        target_batch.append(target)
    return input_batch, output_batch, target_batch

learning_rate = 0.01
n_hidden = 128
total_epoch = 100
n_input = n_class = dic_len

enc_input = tf.placeholder(tf.float32, [None, None, n_input])
dec_input = tf.placeholder(tf.float32, [None, None, n_input])
targets = tf.placeholder(tf.int64, [None, None])

with tf.variable_scope('encode'):
    enc_cell = tf.nn.rnn_cell.BasicRNNCell(n_hidden)
    enc_cell = tf.nn.rnn_cell.DropoutWrapper(enc_cell, output_keep_prob=0.5)
    outputs, enc_states = tf.nn.dynamic_rnn(enc_cell, enc_input, dtype=tf.float32)

with tf.variable_scope('decode'):
    dec_cell = tf.nn.rnn_cell.BasicRNNCell(n_hidden)
    dec_cell = tf.nn.rnn_cell.DropoutWrapper(dec_cell, output_keep_prob=0.5)
    outputs, dec_states = tf.nn.dynamic_rnn(dec_cell, dec_input, initial_state = enc_states, dtype=tf.float32)

model = tf.layers.dense(outputs, n_class, activation=None)

cost = tf.reduce_mean(
    tf.nn.sparse_softmax_cross_entropy_with_logits(logits=model, labels=targets))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

input_batch, output_batch, target_batch = make_batch(seq_data)

for epoch in range(total_epoch):
    _, loss = sess.run([optimizer, cost], feed_dict={enc_input: input_batch, dec_input: output_batch, targets: target_batch})
    print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost =', '{:.6f}'.format(loss))

print('최적화 완료!')

def translate(word):
    seq_data = [word, 'P' * len(word)]
    input_batch, output_batch, target_batch = make_batch([seq_data])
    prediction = tf.argmax(model, 2)
    result = sess.run(prediction,
                      feed_dict={enc_input: input_batch,
                                 dec_input: output_batch,
                                 targets: target_batch})

    decoded = [char_arr[i] for i in result[0]]
    end = decoded.index('E')
    if end == ValueError:
        print('값 없음')
    translated = ''.join(decoded[:end])
    return translated

print('\n=== 번역 테스트 ===')

print('word ->', translate('word'))
print('wodr ->', translate('wodr'))
print('love ->', translate('love'))
print('loev ->', translate('loev'))
print('abcd ->', translate('abcd'))

'''sample result
Epoch: 0001 Avg. cost = 3.705459
Epoch: 0002 Avg. cost = 2.485652
Epoch: 0003 Avg. cost = 1.430552
Epoch: 0004 Avg. cost = 1.203161
Epoch: 0005 Avg. cost = 0.622997
Epoch: 0006 Avg. cost = 0.366225
Epoch: 0007 Avg. cost = 0.309696
Epoch: 0008 Avg. cost = 0.262931
Epoch: 0009 Avg. cost = 0.195124
Epoch: 0010 Avg. cost = 0.153737
Epoch: 0011 Avg. cost = 0.218627
Epoch: 0012 Avg. cost = 0.082242
Epoch: 0013 Avg. cost = 0.224050
Epoch: 0014 Avg. cost = 0.145582
Epoch: 0015 Avg. cost = 0.102590
Epoch: 0016 Avg. cost = 0.019825
Epoch: 0017 Avg. cost = 0.027220
Epoch: 0018 Avg. cost = 0.123697
Epoch: 0019 Avg. cost = 0.015365
Epoch: 0020 Avg. cost = 0.179937
Epoch: 0021 Avg. cost = 0.012064
Epoch: 0022 Avg. cost = 0.006196
Epoch: 0023 Avg. cost = 0.028981
Epoch: 0024 Avg. cost = 0.012066
Epoch: 0025 Avg. cost = 0.008870
Epoch: 0026 Avg. cost = 0.004607
Epoch: 0027 Avg. cost = 0.004673
Epoch: 0028 Avg. cost = 0.002304
Epoch: 0029 Avg. cost = 0.007183
Epoch: 0030 Avg. cost = 0.010702
Epoch: 0031 Avg. cost = 0.005830
Epoch: 0032 Avg. cost = 0.002692
Epoch: 0033 Avg. cost = 0.013798
Epoch: 0034 Avg. cost = 0.006528
Epoch: 0035 Avg. cost = 0.001210
Epoch: 0036 Avg. cost = 0.002508
Epoch: 0037 Avg. cost = 0.001162
Epoch: 0038 Avg. cost = 0.000815
Epoch: 0039 Avg. cost = 0.001838
Epoch: 0040 Avg. cost = 0.003285
Epoch: 0041 Avg. cost = 0.000425
Epoch: 0042 Avg. cost = 0.001260
Epoch: 0043 Avg. cost = 0.001258
Epoch: 0044 Avg. cost = 0.000990
Epoch: 0045 Avg. cost = 0.000739
Epoch: 0046 Avg. cost = 0.000924
Epoch: 0047 Avg. cost = 0.001286
Epoch: 0048 Avg. cost = 0.001617
Epoch: 0049 Avg. cost = 0.002014
Epoch: 0050 Avg. cost = 0.000543
Epoch: 0051 Avg. cost = 0.001445
Epoch: 0052 Avg. cost = 0.001521
Epoch: 0053 Avg. cost = 0.000745
Epoch: 0054 Avg. cost = 0.001644
Epoch: 0055 Avg. cost = 0.000894
Epoch: 0056 Avg. cost = 0.000634
Epoch: 0057 Avg. cost = 0.002078
Epoch: 0058 Avg. cost = 0.000546
Epoch: 0059 Avg. cost = 0.000261
Epoch: 0060 Avg. cost = 0.000541
Epoch: 0061 Avg. cost = 0.000560
Epoch: 0062 Avg. cost = 0.001703
Epoch: 0063 Avg. cost = 0.000687
Epoch: 0064 Avg. cost = 0.000704
Epoch: 0065 Avg. cost = 0.000813
Epoch: 0066 Avg. cost = 0.000755
Epoch: 0067 Avg. cost = 0.000248
Epoch: 0068 Avg. cost = 0.000959
Epoch: 0069 Avg. cost = 0.000355
Epoch: 0070 Avg. cost = 0.001381
Epoch: 0071 Avg. cost = 0.000435
Epoch: 0072 Avg. cost = 0.000887
Epoch: 0073 Avg. cost = 0.000216
Epoch: 0074 Avg. cost = 0.000913
Epoch: 0075 Avg. cost = 0.000589
Epoch: 0076 Avg. cost = 0.000800
Epoch: 0077 Avg. cost = 0.000890
Epoch: 0078 Avg. cost = 0.000905
Epoch: 0079 Avg. cost = 0.000356
Epoch: 0080 Avg. cost = 0.000424
Epoch: 0081 Avg. cost = 0.000220
Epoch: 0082 Avg. cost = 0.000954
Epoch: 0083 Avg. cost = 0.000332
Epoch: 0084 Avg. cost = 0.000292
Epoch: 0085 Avg. cost = 0.000165
Epoch: 0086 Avg. cost = 0.000160
Epoch: 0087 Avg. cost = 0.000175
Epoch: 0088 Avg. cost = 0.000587
Epoch: 0089 Avg. cost = 0.001260
Epoch: 0090 Avg. cost = 0.000571
Epoch: 0091 Avg. cost = 0.000497
Epoch: 0092 Avg. cost = 0.000276
Epoch: 0093 Avg. cost = 0.000666
Epoch: 0094 Avg. cost = 0.000616
Epoch: 0095 Avg. cost = 0.000483
Epoch: 0096 Avg. cost = 0.000291
Epoch: 0097 Avg. cost = 0.001141
Epoch: 0098 Avg. cost = 0.000539
Epoch: 0099 Avg. cost = 0.000499
Epoch: 0100 Avg. cost = 0.000721
최적화 완료!

=== 번역 테스트 ===
word -> 단어
wodr -> 사랑
love -> 사랑
loev -> 사랑
abcd -> 키스
'''