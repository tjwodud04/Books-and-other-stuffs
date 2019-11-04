'''
https://keras.io/examples/imdb_lstm/
'''

from __future__ import print_function

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding
from keras.layers import LSTM
from keras.datasets import imdb

max_features = 20000
maxlen = 80
batch_size = 32

print('Loading data...')

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

print(len(x_train), 'train sequences')
print(len(x_test), 'test sequences')
print('Pad sequences (samples x time)')

x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
x_test = sequence.pad_sequences(x_test, maxlen=maxlen)

print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)
print('Build model...')

model = Sequential()
model.add(Embedding(max_features, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=15,
          validation_data=(x_test, y_test))
score, acc = model.evaluate(x_test, y_test,
                            batch_size=batch_size)

print('Test score:', score)
print('Test accuracy:', acc)

'''
Using TensorFlow backend.
The default version of TensorFlow in Colab will soon switch to TensorFlow 2.x.
We recommend you upgrade now or ensure your notebook will continue to use TensorFlow 1.x via the %tensorflow_version 1.x magic: more info.

Loading data...
Downloading data from https://s3.amazonaws.com/text-datasets/imdb.npz
17465344/17464789 [==============================] - 120s 7us/step
25000 train sequences
25000 test sequences
Pad sequences (samples x time)
x_train shape: (25000, 80)
x_test shape: (25000, 80)
Build model...
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:66: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:541: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:4432: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:148: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:3733: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/optimizers.py:793: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:3657: The name tf.log is deprecated. Please use tf.math.log instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/tensorflow_core/python/ops/nn_impl.py:183: where (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train...
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:1033: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:1020: The name tf.assign is deprecated. Please use tf.compat.v1.assign instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:3005: The name tf.Session is deprecated. Please use tf.compat.v1.Session instead.

Train on 25000 samples, validate on 25000 samples
Epoch 1/15
WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:190: The name tf.get_default_session is deprecated. Please use tf.compat.v1.get_default_session instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:197: The name tf.ConfigProto is deprecated. Please use tf.compat.v1.ConfigProto instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:207: The name tf.global_variables is deprecated. Please use tf.compat.v1.global_variables instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:216: The name tf.is_variable_initialized is deprecated. Please use tf.compat.v1.is_variable_initialized instead.

WARNING:tensorflow:From /usr/local/lib/python3.6/dist-packages/keras/backend/tensorflow_backend.py:223: The name tf.variables_initializer is deprecated. Please use tf.compat.v1.variables_initializer instead.

25000/25000 [==============================] - 143s 6ms/step - loss: 0.4636 - acc: 0.7775 - val_loss: 0.4388 - val_acc: 0.7996
Epoch 2/15
25000/25000 [==============================] - 140s 6ms/step - loss: 0.3058 - acc: 0.8773 - val_loss: 0.3875 - val_acc: 0.8298
Epoch 3/15
25000/25000 [==============================] - 139s 6ms/step - loss: 0.2147 - acc: 0.9168 - val_loss: 0.4143 - val_acc: 0.8286
Epoch 4/15
25000/25000 [==============================] - 139s 6ms/step - loss: 0.1554 - acc: 0.9426 - val_loss: 0.4680 - val_acc: 0.8259
Epoch 5/15
25000/25000 [==============================] - 140s 6ms/step - loss: 0.1174 - acc: 0.9572 - val_loss: 0.5442 - val_acc: 0.8168
Epoch 6/15
25000/25000 [==============================] - 140s 6ms/step - loss: 0.0810 - acc: 0.9714 - val_loss: 0.6376 - val_acc: 0.8042
Epoch 7/15
25000/25000 [==============================] - 139s 6ms/step - loss: 0.0641 - acc: 0.9785 - val_loss: 0.7523 - val_acc: 0.8181
Epoch 8/15
25000/25000 [==============================] - 140s 6ms/step - loss: 0.0485 - acc: 0.9831 - val_loss: 0.8706 - val_acc: 0.8134
Epoch 9/15
25000/25000 [==============================] - 140s 6ms/step - loss: 0.0353 - acc: 0.9881 - val_loss: 0.9655 - val_acc: 0.8105
Epoch 10/15
25000/25000 [==============================] - 139s 6ms/step - loss: 0.0263 - acc: 0.9918 - val_loss: 0.9119 - val_acc: 0.8158
Epoch 11/15
25000/25000 [==============================] - 142s 6ms/step - loss: 0.0239 - acc: 0.9928 - val_loss: 0.8956 - val_acc: 0.8124
Epoch 12/15
25000/25000 [==============================] - 144s 6ms/step - loss: 0.0212 - acc: 0.9936 - val_loss: 1.0002 - val_acc: 0.8115
Epoch 13/15
25000/25000 [==============================] - 149s 6ms/step - loss: 0.0158 - acc: 0.9956 - val_loss: 1.0369 - val_acc: 0.8080
Epoch 14/15
25000/25000 [==============================] - 144s 6ms/step - loss: 0.0160 - acc: 0.9948 - val_loss: 1.1245 - val_acc: 0.8065
Epoch 15/15
25000/25000 [==============================] - 139s 6ms/step - loss: 0.0122 - acc: 0.9963 - val_loss: 1.1736 - val_acc: 0.8075
25000/25000 [==============================] - 16s 642us/step
Test score: 1.1736065911588818
Test accuracy: 0.80748
'''