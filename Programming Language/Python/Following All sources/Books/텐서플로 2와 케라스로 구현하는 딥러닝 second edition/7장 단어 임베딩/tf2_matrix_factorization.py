import numpy as np
import tensorflow as tf

class MatrixFactorizationLayer(tf.keras.layers.Layer):
    def __init__(self, emb_sz, **kwargs):
        super(MatrixFactorizationLayer, self).__init__(**kwargs)
        self.emb_sz = emb_sz

    def build(self, input_shape):
        num_rows, num_cols = input_shape
        self.P = self.add_variable("P", 
            shape=[num_rows, self.emb_sz], 
            dtype=tf.float32,
            initializer=tf.initializers.GlorotUniform)
        self.Q = self.add_variable("Q", 
            shape=[num_cols, self.emb_sz],
            dtype=tf.float32, 
            initializer=tf.initializers.GlorotUniform)

    def call(self, input):
        return tf.matmul(self.P, tf.transpose(self.Q))

class MatrixFactorizationModel(tf.keras.Model):
    def __init__(self, embedding_size):
        super(MatrixFactorizationModel, self).__init__()
        self.mfl = MatrixFactorizationLayer(embedding_size)
        self.sigmoid = tf.keras.layers.Activation("sigmoid")

    def call(self, x):
        x = self.mfl(x)
        x = self.sigmoid(x)
        return x

def loss_fn(source, target):
    mse = tf.keras.losses.MeanSquaredError()
    loss = mse(source, target)
    return loss

EMBEDDING_SIZE = 15
NUM_ROWS = 1000
NUM_COLS = 5000

R = np.random.random((NUM_ROWS, NUM_COLS))

model = MatrixFactorizationModel(EMBEDDING_SIZE)
model.build(input_shape=R.shape)
model.summary()

optimizer = tf.optimizers.RMSprop(learning_rate=1e-3, momentum=0.9)

mf_layer = model.layers[0]
P, Q = [weight.numpy() for weight in mf_layer.weights]
print(P.shape, Q.shape)

'''result

Model: "matrix_factorization_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
matrix_factorization_layer ( multiple                  90000     
_________________________________________________________________
activation (Activation)      multiple                  0         
=================================================================
Total params: 90,000
Trainable params: 90,000
Non-trainable params: 0
_________________________________________________________________
(1000, 15) (5000, 15)
'''