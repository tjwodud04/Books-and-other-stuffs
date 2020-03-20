import numpy as np
import matplotlib.pyplot as plt
from DefinitionOfAll import sequence
from DefinitionOfAll.Adam import Adam
from DefinitionOfAll.Trainer import Trainer
from DefinitionOfAll.eval_seq2seq import eval_seq2seq
from DefinitionOfAll.AttentionSeq2seq import AttentionSeq2seq
from DefinitionOfAll.seq2seq import Seq2seq
from DefinitionOfAll.peeky_seq2seq import PeekySeq2seq

(x_train, t_train), (x_test, t_test) = sequence.load_data('date.txt')
char_to_id, id_to_char = sequence.get_vocab()

x_train, x_test = x_train[:, ::-1], x_test[:, ::-1]

vocab_size = len(char_to_id)
wordvec_size = 16
hidden_size = 256
batch_size = 128
max_epoch = 10
max_grad = 5.0

model = AttentionSeq2seq(vocab_size, wordvec_size, hidden_size)
model2 = Seq2seq(vocab_size, wordvec_size, hidden_size)
model3 = PeekySeq2seq(vocab_size, wordvec_size, hidden_size)

optimizer = Adam()
trainer = Trainer(model, optimizer)

acc_list = []
for epoch in range(max_epoch):
    trainer.fit(x_train, t_train, max_epoch=1,
                batch_size=batch_size, max_grad=max_grad)

    correct_num = 0
    for i in range(len(x_test)):
        question, correct = x_test[[i]], t_test[[i]]
        verbose = i < 10
        correct_num += eval_seq2seq(model, question, correct,
                                    id_to_char, verbose, is_reverse=True)
#-------------------------------------------------------------------------
    acc = float(correct_num) / len(x_test)
    acc_list.append(acc)
    print('정확도 %.3f%%' % (acc * 100))


trainer2 = Trainer(model2, optimizer)
acc_list2 = []
for epoch in range(max_epoch):
    trainer.fit(x_train, t_train, max_epoch=1,
                batch_size=batch_size, max_grad=max_grad)

    correct_num = 0
    for i in range(len(x_test)):
        question, correct = x_test[[i]], t_test[[i]]
        verbose = i < 10
        correct_num += eval_seq2seq(model2, question, correct,
                                    id_to_char, verbose, is_reverse=True)

    acc = float(correct_num) / len(x_test)
    acc_list2.append(acc)
    print('정확도 %.3f%%' % (acc * 100))
#----------------------------------------------------------------------------
trainer3 = Trainer(model3, optimizer)
acc_list3 = []
for epoch in range(max_epoch):
    trainer.fit(x_train, t_train, max_epoch=1,
                batch_size=batch_size, max_grad=max_grad)

    correct_num = 0
    for i in range(len(x_test)):
        question, correct = x_test[[i]], t_test[[i]]
        verbose = i < 10
        correct_num += eval_seq2seq(model3, question, correct,
                                    id_to_char, verbose, is_reverse=True)

    acc = float(correct_num) / len(x_test)
    acc_list3.append(acc)
    print('정확도 %.3f%%' % (acc * 100))

model.save_params()

x = np.arange(len(acc_list))
x = np.arange(len(acc_list2))
x = np.arange(len(acc_list3))
plt.plot(x, acc_list, marker='o')
plt.plot(x, acc_list2, marker='x')
plt.plot(x, acc_list3, marker='v')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.ylim(-0.05, 1.05)
plt.show()