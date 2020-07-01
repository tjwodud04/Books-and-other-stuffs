import matplotlib.pyplot as plt
import numpy as np
from DefinitionOfAll.SGD import SGD
from dataset import ptb
from DefinitionOfAll.SimpleRnnlm import SimpleRnnlm

batch_size = 10
wordvec_size = 100
hidden_size = 100
time_size = 5
lr = 0.1
max_epoch = 100

corpus, word_to_id, id_to_word = ptb.load_data('train')
corpus_size = 1000
corpus = corpus[:corpus_size]
vocab_size = int(max(corpus) + 1)

xs = corpus[:-1]
ts = corpus[1:]
data_size = len(xs)
print('말뭉치 크기: %d, 어휘 수: %d' % (corpus_size, vocab_size))

max_iters = data_size // (batch_size * time_size)
time_idx = 0
total_loss = 0
loss_count = 0
ppl_list = []

model = SimpleRnnlm(vocab_size, wordvec_size, hidden_size)
optimizer = SGD(lr)

jump = (corpus_size - 1) // batch_size
offsets = [i * jump for i in range(batch_size)]

for epoch in range(max_epoch):
    for iter in range(max_iters):
        batch_x = np.empty((batch_size, time_size), dtype='i')
        batch_t = np.empty((batch_size, time_size), dtype='i')
        for t in range(time_size):
            for i, offset in enumerate(offsets):
                batch_x[i, t] = xs[(offset + time_idx) % data_size]
                batch_t[i, t] = ts[(offset + time_idx) % data_size]
            time_idx += 1

        loss = model.forward(batch_x, batch_t)
        model.backward()
        optimizer.update(model.params, model.grads)
        total_loss += loss
        loss_count += 1

    ppl = np.exp(total_loss / loss_count)
    print('| 에폭 %d | 퍼플렉서티 %.2f'
          % (epoch+1, ppl))
    ppl_list.append(float(ppl))
    total_loss, loss_count = 0, 0

x = np.arange(len(ppl_list))
plt.plot(x, ppl_list, label='train')
plt.xlabel('epochs')
plt.ylabel('perplexity')
plt.show()

'''
실행결과

말뭉치 크기: 1000, 어휘 수: 418
| 에폭 1 | 퍼플렉서티 400.48
| 에폭 2 | 퍼플렉서티 288.06
| 에폭 3 | 퍼플렉서티 232.09
| 에폭 4 | 퍼플렉서티 220.21
| 에폭 5 | 퍼플렉서티 209.03
| 에폭 6 | 퍼플렉서티 204.58
| 에폭 7 | 퍼플렉서티 200.39
| 에폭 8 | 퍼플렉서티 197.84
| 에폭 9 | 퍼플렉서티 192.50
| 에폭 10 | 퍼플렉서티 193.51
| 에폭 11 | 퍼플렉서티 188.98
| 에폭 12 | 퍼플렉서티 191.83
| 에폭 13 | 퍼플렉서티 190.83
| 에폭 14 | 퍼플렉서티 191.11
| 에폭 15 | 퍼플렉서티 189.94
| 에폭 16 | 퍼플렉서티 186.26
| 에폭 17 | 퍼플렉서티 184.17
| 에폭 18 | 퍼플렉서티 181.09
| 에폭 19 | 퍼플렉서티 182.24
| 에폭 20 | 퍼플렉서티 183.16
| 에폭 21 | 퍼플렉서티 181.32
| 에폭 22 | 퍼플렉서티 177.16
| 에폭 23 | 퍼플렉서티 173.52
| 에폭 24 | 퍼플렉서티 176.11
| 에폭 25 | 퍼플렉서티 172.72
| 에폭 26 | 퍼플렉서티 172.09
| 에폭 27 | 퍼플렉서티 167.49
| 에폭 28 | 퍼플렉서티 165.79
| 에폭 29 | 퍼플렉서티 162.90
| 에폭 30 | 퍼플렉서티 157.67
| 에폭 31 | 퍼플렉서티 158.03
| 에폭 32 | 퍼플렉서티 155.46
| 에폭 33 | 퍼플렉서티 152.98
| 에폭 34 | 퍼플렉서티 148.97
| 에폭 35 | 퍼플렉서티 146.00
| 에폭 36 | 퍼플렉서티 140.05
| 에폭 37 | 퍼플렉서티 137.26
| 에폭 38 | 퍼플렉서티 132.21
| 에폭 39 | 퍼플렉서티 126.39
| 에폭 40 | 퍼플렉서티 121.83
| 에폭 41 | 퍼플렉서티 123.57
| 에폭 42 | 퍼플렉서티 117.63
| 에폭 43 | 퍼플렉서티 109.64
| 에폭 44 | 퍼플렉서티 106.35
| 에폭 45 | 퍼플렉서티 103.40
| 에폭 46 | 퍼플렉서티 102.78
| 에폭 47 | 퍼플렉서티 97.08
| 에폭 48 | 퍼플렉서티 90.61
| 에폭 49 | 퍼플렉서티 86.97
| 에폭 50 | 퍼플렉서티 86.02
| 에폭 51 | 퍼플렉서티 81.20
| 에폭 52 | 퍼플렉서티 77.64
| 에폭 53 | 퍼플렉서티 72.92
| 에폭 54 | 퍼플렉서티 69.94
| 에폭 55 | 퍼플렉서티 67.76
| 에폭 56 | 퍼플렉서티 63.57
| 에폭 57 | 퍼플렉서티 61.00
| 에폭 58 | 퍼플렉서티 55.41
| 에폭 59 | 퍼플렉서티 53.46
| 에폭 60 | 퍼플렉서티 50.49
| 에폭 61 | 퍼플렉서티 49.04
| 에폭 62 | 퍼플렉서티 45.42
| 에폭 63 | 퍼플렉서티 41.66
| 에폭 64 | 퍼플렉서티 40.39
| 에폭 65 | 퍼플렉서티 39.09
| 에폭 66 | 퍼플렉서티 36.20
| 에폭 67 | 퍼플렉서티 34.13
| 에폭 68 | 퍼플렉서티 31.51
| 에폭 69 | 퍼플렉서티 30.88
| 에폭 70 | 퍼플렉서티 28.72
| 에폭 71 | 퍼플렉서티 26.68
| 에폭 72 | 퍼플렉서티 24.65
| 에폭 73 | 퍼플렉서티 23.72
| 에폭 74 | 퍼플렉서티 22.30
| 에폭 75 | 퍼플렉서티 21.96
| 에폭 76 | 퍼플렉서티 19.84
| 에폭 77 | 퍼플렉서티 18.64
| 에폭 78 | 퍼플렉서티 17.59
| 에폭 79 | 퍼플렉서티 16.88
| 에폭 80 | 퍼플렉서티 15.31
| 에폭 81 | 퍼플렉서티 15.17
| 에폭 82 | 퍼플렉서티 14.91
| 에폭 83 | 퍼플렉서티 13.40
| 에폭 84 | 퍼플렉서티 13.35
| 에폭 85 | 퍼플렉서티 12.27
| 에폭 86 | 퍼플렉서티 11.40
| 에폭 87 | 퍼플렉서티 10.72
| 에폭 88 | 퍼플렉서티 10.12
| 에폭 89 | 퍼플렉서티 9.65
| 에폭 90 | 퍼플렉서티 9.19
| 에폭 91 | 퍼플렉서티 8.76
| 에폭 92 | 퍼플렉서티 8.61
| 에폭 93 | 퍼플렉서티 8.17
| 에폭 94 | 퍼플렉서티 7.74
| 에폭 95 | 퍼플렉서티 7.36
| 에폭 96 | 퍼플렉서티 6.92
| 에폭 97 | 퍼플렉서티 6.69
| 에폭 98 | 퍼플렉서티 6.03
| 에폭 99 | 퍼플렉서티 6.19
| 에폭 100 | 퍼플렉서티 5.97
'''