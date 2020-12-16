'''
https://keras.io/examples/babi_rnn/
'''

from __future__ import print_function
from functools import reduce

import re
import tarfile
import numpy as np

from keras.utils.data_utils import get_file
from keras.layers.embeddings import Embedding
from keras import layers
from keras.layers import recurrent
from keras.models import Model
from keras.preprocessing.sequence import pad_sequences

def tokenize(sent):
    return [x.strip() for x in re.split(r'(\W+)', sent) if x.strip()]

def parse_stories(lines, only_supporting=False):
    data = []
    story = []

    for line in lines:
        line = line.decode('utf-8').strip()
        nid, line = line.split(' ', 1)
        nid = int(nid)

        if nid == 1:
            story = []

        if '\t' in line:
            q, a, supporting = line.split('\t')
            q = tokenize(q)

            if only_supporting:
                supporting = map(int, supporting.split())
                substory = [story[i - 1] for i in supporting]
            else:
                substory = [x for x in story if x]

            data.append((substory, q, a))
            story.append('')

        else:
            sent = tokenize(line)
            story.append(sent)
    return data

def get_stories(f, only_supporting=False, max_length=None):
    data = parse_stories(f.readlines(), only_supporting=only_supporting)
    flatten = lambda data: reduce(lambda x, y: x + y, data)
    data = [(flatten(story), q, answer) for story, q, answer in data
            if not max_length or len(flatten(story)) < max_length]
    return data

def vectorize_stories(data, word_idx, story_maxlen, query_maxlen):
    xs = []
    xqs = []
    ys = []

    for story, query, answer in data:
        x = [word_idx[w] for w in story]
        xq = [word_idx[w] for w in query]
        y = np.zeros(len(word_idx) + 1)
        y[word_idx[answer]] = 1
        xs.append(x)
        xqs.append(xq)
        ys.append(y)
    return (pad_sequences(xs, maxlen=story_maxlen),
            pad_sequences(xqs, maxlen=query_maxlen), np.array(ys))

RNN = recurrent.LSTM
EMBED_HIDDEN_SIZE = 50
SENT_HIDDEN_SIZE = 100
QUERY_HIDDEN_SIZE = 100
BATCH_SIZE = 32
EPOCHS = 20
print('RNN / Embed / Sent / Query = {}, {}, {}, {}'.format(RNN,
                                                           EMBED_HIDDEN_SIZE,
                                                           SENT_HIDDEN_SIZE,
                                                           QUERY_HIDDEN_SIZE))

try:
    path = get_file('babi-tasks-v1-2.tar.gz',
                    origin='https://s3.amazonaws.com/text-datasets/'
                           'babi_tasks_1-20_v1-2.tar.gz')
except:
    print('Error downloading dataset, please download it manually:\n'
          '$ wget http://www.thespermwhale.com/jaseweston/babi/tasks_1-20_v1-2'
          '.tar.gz\n'
          '$ mv tasks_1-20_v1-2.tar.gz ~/.keras/datasets/babi-tasks-v1-2.tar.gz')
    raise

challenge = 'tasks_1-20_v1-2/en/qa2_two-supporting-facts_{}.txt'

with tarfile.open(path) as tar:
    train = get_stories(tar.extractfile(challenge.format('train')))
    test = get_stories(tar.extractfile(challenge.format('test')))

vocab = set()
for story, q, answer in train + test:
    vocab |= set(story + q + [answer])
vocab = sorted(vocab)

vocab_size = len(vocab) + 1
word_idx = dict((c, i + 1) for i, c in enumerate(vocab))
story_maxlen = max(map(len, (x for x, _, _ in train + test)))
query_maxlen = max(map(len, (x for _, x, _ in train + test)))

x, xq, y = vectorize_stories(train, word_idx, story_maxlen, query_maxlen)
tx, txq, ty = vectorize_stories(test, word_idx, story_maxlen, query_maxlen)

print('vocab = {}'.format(vocab))
print('x.shape = {}'.format(x.shape))
print('xq.shape = {}'.format(xq.shape))
print('y.shape = {}'.format(y.shape))
print('story_maxlen, query_maxlen = {}, {}'.format(story_maxlen, query_maxlen))

print('Build model...')

sentence = layers.Input(shape=(story_maxlen,), dtype='int32')
encoded_sentence = layers.Embedding(vocab_size, EMBED_HIDDEN_SIZE)(sentence)
encoded_sentence = RNN(SENT_HIDDEN_SIZE)(encoded_sentence)

question = layers.Input(shape=(query_maxlen,), dtype='int32')
encoded_question = layers.Embedding(vocab_size, EMBED_HIDDEN_SIZE)(question)
encoded_question = RNN(QUERY_HIDDEN_SIZE)(encoded_question)

merged = layers.concatenate([encoded_sentence, encoded_question])
preds = layers.Dense(vocab_size, activation='softmax')(merged)

model = Model([sentence, question], preds)
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training')
model.fit([x, xq], y,
          batch_size=BATCH_SIZE,
          epochs=EPOCHS,
          validation_split=0.05)

print('Evaluation')
loss, acc = model.evaluate([tx, txq], ty,
                           batch_size=BATCH_SIZE)
print('Test loss / test accuracy = {:.4f} / {:.4f}'.format(loss, acc))

'''
Using TensorFlow backend.
The default version of TensorFlow in Colab will soon switch to TensorFlow 2.x.
We recommend you upgrade now or ensure your notebook will continue to use TensorFlow 1.x via the %tensorflow_version 1.x magic: more info.

RNN / Embed / Sent / Query = <class 'keras.layers.recurrent.LSTM'>, 50, 100, 100
Downloading data from https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz
11747328/11745123 [==============================] - 1s 0us/step
vocab = ['.', '?', 'Daniel', 'John', 'Mary', 'Sandra', 'Where', 'apple', 'back', 'bathroom', 'bedroom', 'discarded', 'down', 'dropped', 'football', 'garden', 'got', 'grabbed', 'hallway', 'is', 'journeyed', 'kitchen', 'left', 'milk', 'moved', 'office', 'picked', 'put', 'the', 'there', 'to', 'took', 'travelled', 'up', 'went']
x.shape = (1000, 552)
xq.shape = (1000, 5)
y.shape = (1000, 36)
story_maxlen, query_maxlen = 552, 5
Build model...
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:66: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:541: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:4432: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/optimizers.py:793: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:3576: The name tf.log is deprecated. Please use tf.math.log instead.

Training
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/tensorflow_core/python/ops/math_grad.py:1424: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:1033: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:1020: The name tf.assign is deprecated. Please use tf.compat.v1.assign instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:3005: The name tf.Session is deprecated. Please use tf.compat.v1.Session instead.

Train on 950 samples, validate on 50 samples
Epoch 1/20

950/950 [==============================] - 21s 23ms/step - loss: 2.6150 - acc: 0.2032 - val_loss: 1.7573 - val_acc: 0.3000
Epoch 2/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7961 - acc: 0.2095 - val_loss: 1.8893 - val_acc: 0.0600
Epoch 3/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7984 - acc: 0.1947 - val_loss: 1.9000 - val_acc: 0.0600
Epoch 4/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7903 - acc: 0.2032 - val_loss: 1.9315 - val_acc: 0.0600
Epoch 5/20
950/950 [==============================] - 19s 20ms/step - loss: 1.8030 - acc: 0.2011 - val_loss: 1.9023 - val_acc: 0.0600
Epoch 6/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7937 - acc: 0.2000 - val_loss: 1.8240 - val_acc: 0.0600
Epoch 7/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7914 - acc: 0.1958 - val_loss: 1.7512 - val_acc: 0.2000
Epoch 8/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7889 - acc: 0.2147 - val_loss: 1.7197 - val_acc: 0.3000
Epoch 9/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7787 - acc: 0.2095 - val_loss: 1.8141 - val_acc: 0.0600
Epoch 10/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7939 - acc: 0.2021 - val_loss: 1.8058 - val_acc: 0.0600
Epoch 11/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7796 - acc: 0.2105 - val_loss: 1.8139 - val_acc: 0.0600
Epoch 12/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7836 - acc: 0.2042 - val_loss: 1.9017 - val_acc: 0.0600
Epoch 13/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7884 - acc: 0.2063 - val_loss: 1.8336 - val_acc: 0.0600
Epoch 14/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7840 - acc: 0.2326 - val_loss: 1.7923 - val_acc: 0.3400
Epoch 15/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7747 - acc: 0.2347 - val_loss: 1.7860 - val_acc: 0.1000
Epoch 16/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7696 - acc: 0.2316 - val_loss: 1.8268 - val_acc: 0.1400
Epoch 17/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7696 - acc: 0.2263 - val_loss: 1.8060 - val_acc: 0.1400
Epoch 18/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7468 - acc: 0.2674 - val_loss: 1.8271 - val_acc: 0.1800
Epoch 19/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7483 - acc: 0.2684 - val_loss: 1.7021 - val_acc: 0.3200
Epoch 20/20
950/950 [==============================] - 19s 20ms/step - loss: 1.7406 - acc: 0.2663 - val_loss: 1.7039 - val_acc: 0.2800
Evaluation
1000/1000 [==============================] - 3s 3ms/step
Test loss / test accuracy = 1.8002 / 0.2020
'''