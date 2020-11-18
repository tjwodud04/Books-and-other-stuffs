import tensorflow as tf
from tensorflow.keras import datasets, layers, models, optimizers

class LeNet:
	@staticmethod
	def build(input_shape, classes):
		model = models.Sequential()
		model.add(layers.Convolution2D(20, (5, 5), activation='relu', input_shape=input_shape))
		model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
		model.add(layers.Convolution2D(50, (5, 5), activation='relu'))
		model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
		model.add(layers.Flatten())
		model.add(layers.Dense(500, activation='relu'))
		model.add(layers.Dense(classes, activation="softmax"))

		return model

EPOCHS = 5
BATCH_SIZE = 128
VERBOSE = 1
OPTIMIZER = tf.keras.optimizers.Adam()
VALIDATION_SPLIT=0.90

IMG_ROWS, IMG_COLS = 28, 28
INPUT_SHAPE = (IMG_ROWS, IMG_COLS, 1)
NB_CLASSES = 10

(X_train, y_train), (X_test, y_test) = datasets.mnist.load_data()

X_train = X_train.reshape((60000, 28, 28, 1))
X_test = X_test.reshape((10000, 28, 28, 1))

X_train, X_test = X_train / 255.0, X_test / 255.0

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')
'''result
60000 train samples
10000 test samples
'''

y_train = tf.keras.utils.to_categorical(y_train, NB_CLASSES)
y_test = tf.keras.utils.to_categorical(y_test, NB_CLASSES)

model = LeNet.build(input_shape=INPUT_SHAPE, classes=NB_CLASSES)
model.compile(loss="categorical_crossentropy", optimizer=OPTIMIZER,	metrics=["accuracy"])
model.summary()
''' result
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 24, 24, 20)        520       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 12, 12, 20)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 8, 8, 50)          25050     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 4, 4, 50)          0         
_________________________________________________________________
flatten (Flatten)            (None, 800)               0         
_________________________________________________________________
dense (Dense)                (None, 500)               400500    
_________________________________________________________________
dense_1 (Dense)              (None, 10)                5010      
=================================================================
Total params: 431,080
Trainable params: 431,080
Non-trainable params: 0
_________________________________________________________________
'''
callbacks = [tf.keras.callbacks.TensorBoard(log_dir='./logs')]

history = model.fit(X_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=VERBOSE,
					validation_split=VALIDATION_SPLIT, callbacks=callbacks)

score = model.evaluate(X_test, y_test, verbose=VERBOSE)

print("\nTest score:", score[0])
print('Test accuracy:', score[1])
'''result
Test score: 0.08003084361553192
Test accuracy: 0.9747999906539917
'''
'''
Epoch 1/5
1/47 [..............................] - ETA: 0s - loss: 2.3206 - accuracy: 0.0781
47/47 [==============================] - 5s 96ms/step - loss: 0.8218 - accuracy: 0.7650 - val_loss: 0.3057 - val_accuracy: 0.9084
Epoch 2/5
47/47 [==============================] - 4s 94ms/step - loss: 0.2187 - accuracy: 0.9353 - val_loss: 0.1850 - val_accuracy: 0.9436
Epoch 3/5
47/47 [==============================] - 4s 93ms/step - loss: 0.1317 - accuracy: 0.9603 - val_loss: 0.1409 - val_accuracy: 0.9558
Epoch 4/5
47/47 [==============================] - 4s 95ms/step - loss: 0.0905 - accuracy: 0.9722 - val_loss: 0.1177 - val_accuracy: 0.9639
Epoch 5/5
47/47 [==============================] - 5s 97ms/step - loss: 0.0683 - accuracy: 0.9790 - val_loss: 0.0947 - val_accuracy: 0.9704
313/313 [==============================] - 1s 4ms/step - loss: 0.0800 - accuracy: 0.9748
'''