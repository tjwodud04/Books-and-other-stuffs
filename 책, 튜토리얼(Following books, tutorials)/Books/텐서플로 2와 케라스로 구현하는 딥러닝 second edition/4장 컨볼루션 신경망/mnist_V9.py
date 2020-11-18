import tensorflow as tf
from tensorflow import keras

EPOCHS = 5
BATCH_SIZE = 256
VERBOSE = 1
NB_CLASSES = 10
N_HIDDEN = 2048
VALIDATION_SPLIT=0.999
DROPOUT = 0.3

mnist = keras.datasets.mnist
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

RESHAPED = 784

X_train = X_train.reshape(60000, RESHAPED)
X_test = X_test.reshape(10000, RESHAPED)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

X_train, X_test = X_train / 255.0, X_test / 255.0

print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
'''result
60000 train samples
10000 test samples
'''

Y_train = tf.keras.utils.to_categorical(Y_train, NB_CLASSES)
Y_test = tf.keras.utils.to_categorical(Y_test, NB_CLASSES)

model = tf.keras.models.Sequential()
model.add(keras.layers.Dense(N_HIDDEN, input_shape=(RESHAPED,), name='dense_layer', activation='relu'))
model.add(keras.layers.Dropout(DROPOUT))
model.add(keras.layers.Dense(N_HIDDEN, name='dense_layer_2', activation='relu'))
model.add(keras.layers.Dropout(DROPOUT))
model.add(keras.layers.Dense(NB_CLASSES, name='dense_layer_3', activation='softmax'))

model.summary()
''' result
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_layer (Dense)          (None, 2048)              1607680   
_________________________________________________________________
dropout (Dropout)            (None, 2048)              0         
_________________________________________________________________
dense_layer_2 (Dense)        (None, 2048)              4196352   
_________________________________________________________________
dropout_1 (Dropout)          (None, 2048)              0         
_________________________________________________________________
dense_layer_3 (Dense)        (None, 10)                20490     
=================================================================
Total params: 5,824,522
Trainable params: 5,824,522
Non-trainable params: 0
_________________________________________________________________
'''

model.compile(optimizer='Adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=VERBOSE,
		  validation_split=VALIDATION_SPLIT)

test_loss, test_acc = model.evaluate(X_test, Y_test)

print('Test accuracy:', test_acc)
'''result
Test accuracy: 0.6553999781608582
'''

predictions = model.predict(X_test)
'''
Epoch 1/5
1/1 [==============================] - 2s 2s/step - loss: 2.3267 - accuracy: 0.1000 - val_loss: 2.0021 - val_accuracy: 0.3096
Epoch 2/5
1/1 [==============================] - 2s 2s/step - loss: 1.5198 - accuracy: 0.5667 - val_loss: 1.5751 - val_accuracy: 0.5357
Epoch 3/5
1/1 [==============================] - 2s 2s/step - loss: 0.8585 - accuracy: 0.8667 - val_loss: 1.2478 - val_accuracy: 0.6343
Epoch 4/5
1/1 [==============================] - 2s 2s/step - loss: 0.4584 - accuracy: 0.9667 - val_loss: 1.0869 - val_accuracy: 0.6655
Epoch 5/5
1/1 [==============================] - 2s 2s/step - loss: 0.2176 - accuracy: 0.9833 - val_loss: 1.0815 - val_accuracy: 0.6573
313/313 [==============================] - 2s 6ms/step - loss: 1.0765 - accuracy: 0.6554
'''