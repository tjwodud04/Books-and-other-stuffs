import tensorflow as tf
import numpy as np
from tensorflow import keras

N_TRAIN_EXAMPLES = 1024*1024
N_FEATURES = 10
SIZE_BATCHES = 256

x = np.random.random((N_TRAIN_EXAMPLES, N_FEATURES))
y = np.random.randint(2, size=(N_TRAIN_EXAMPLES, 1))
x = tf.dtypes.cast(x, tf.float32)

print (x)

'''
tf.Tensor(
[[0.9783743  0.7815162  0.8472095  ... 0.3828216  0.5884804  0.2109141 ]
 [0.78924835 0.4037204  0.4865493  ... 0.178134   0.6014104  0.1510281 ]
 [0.8111321  0.5974956  0.3621483  ... 0.6340769  0.40925613 0.2965699 ]
 ...
 [0.14372525 0.00530197 0.07910276 ... 0.4398104  0.38092312 0.98014396]
 [0.84536123 0.2308754  0.37998244 ... 0.57827145 0.81608874 0.73648846]
 [0.03911881 0.93368524 0.9925995  ... 0.31832305 0.5305188  0.48448947]], shape=(1048576, 10), dtype=float32)
'''

dataset = tf.data.Dataset.from_tensor_slices((x, y))
dataset = dataset.shuffle(buffer_size=N_TRAIN_EXAMPLES).batch(SIZE_BATCHES)

distribution = tf.distribute.MirroredStrategy()

with distribution.scope():
  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(16, activation='relu', input_shape=(N_FEATURES,)))
  model.add(tf.keras.layers.Dense(1, activation='sigmoid'))
  optimizer = tf.keras.optimizers.SGD(0.2)
  model.compile(loss='binary_crossentropy', optimizer=optimizer)

model.summary()

'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 16)                176       
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 17        
=================================================================
Total params: 193
Trainable params: 193
Non-trainable params: 0
_________________________________________________________________
'''

model.fit(dataset, epochs=5, steps_per_epoch=100)

'''
Epoch 1/5
100/100 [==============================] - 0s 661us/step - loss: 0.6969
Epoch 2/5
100/100 [==============================] - 0s 630us/step - loss: 0.6945
Epoch 3/5
100/100 [==============================] - 0s 611us/step - loss: 0.6940
Epoch 4/5
100/100 [==============================] - 0s 641us/step - loss: 0.6938
Epoch 5/5
100/100 [==============================] - 0s 631us/step - loss: 0.6936
'''