from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds
'''
print("버전: ", tf.__version__)
print("즉시 실행 모드: ", tf.executing_eagerly())
print("허브 버전: ", hub.__version__)
print("GPU ", "사용 가능" if tf.config.experimental.list_physical_devices("GPU") else "사용 불가능")
'''
'''result
버전:  1.14.0
즉시 실행 모드:  False
허브 버전:  0.6.0
GPU  사용 가능
'''

train_validation_split = tfds.Split.TRAIN.subsplit([6,4])

(train_data, validation_data), test_data = tfds.load(
    name = "imdb_reviews",
    split = (train_validation_split, tfds.Split.TEST),
    as_supervised = True
)

train_examples_batch, train_labels_batch = next(iter(train_data.batch(10)))
print(train_examples_batch)
print(train_labels_batch)

'''result
<tf.Tensor: shape=(10,), dtype=string, numpy=
array([b"As a lifelong fan of Dickens,
...
I think it would have all but the heartless reaching for the Prozac."],
      dtype=object)>
      
<tf.Tensor: shape=(10,), dtype=int64, numpy=array([1, 1, 1, 1, 1, 1, 0, 1, 1, 0], dtype=int64)>
'''

embedding = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(embedding, input_shape =[], dtype = tf.string, trainable=True)
print(train_examples_batch[:3])
'''result
<tf.Tensor: shape=(3,), dtype=string, numpy=
array([b"As a lifelong fan of Dickens, 
I have invariably been disappointed by adaptations of his novels.
...
Watch out for the scene where Dermot Mulroney runs from the disastrous counselling session 
- career performance."], dtype=object)>
'''

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.summary()
''' result
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
keras_layer (KerasLayer)     (None, 20)                400020    
_________________________________________________________________
dense (Dense)                (None, 16)                336       
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 17        
=================================================================
Total params: 400,373
Trainable params: 400,373
Non-trainable params: 0
_________________________________________________________________
'''

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_data.shuffle(10000).batch(512), epochs=20,
                    validation_data= validation_data.batch(512), verbose=1)

results = model.evaluate(test_data.batch(512), verbose=0)

for name, value in zip(model.metrics_names, results):
    print('%s: %.3f' % (name, value))
''' result
loss: 0.623
accuracy: 0.650
'''
