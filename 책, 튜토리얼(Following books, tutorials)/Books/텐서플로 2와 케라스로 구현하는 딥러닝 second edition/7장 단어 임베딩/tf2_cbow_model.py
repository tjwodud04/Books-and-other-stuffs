import tensorflow as tf

class CBOWModel(tf.keras.Model):
    def __init__(self, vocab_sz, emb_sz, window_sz, **kwargs):
        super(CBOWModel, self).__init__(**kwargs)
        self.embedding = tf.keras.layers.Embedding(
            input_dim=vocab_sz,
            output_dim=emb_sz,
            embeddings_initializer="glorot_uniform",
            input_length=window_sz*2
        )
        self.dense = tf.keras.layers.Dense(
            vocab_sz,
            kernel_initializer="glorot_uniform",
            activation="softmax"
        )

    def call(self, x):
        x = self.embedding(x)
        x = tf.reduce_mean(x, axis=1)
        x = self.dense(x)
        return x

VOCAB_SIZE = 5000
EMBED_SIZE = 300
WINDOW_SIZE = 1

model = CBOWModel(VOCAB_SIZE, EMBED_SIZE, WINDOW_SIZE)
model.build(input_shape=(None, VOCAB_SIZE))
model.compile(optimizer=tf.optimizers.Adam(),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

model.summary()
'''
Model: "cbow_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        multiple                  1500000   
_________________________________________________________________
dense (Dense)                multiple                  1505000   
=================================================================
Total params: 3,005,000
Trainable params: 3,005,000
Non-trainable params: 0
_________________________________________________________________
'''

emb_layer = [layer for layer in model.layers if layer.name.startswith("embedding")][0]
emb_weight = [weight.numpy() for weight in emb_layer.weights if weight.name.endswith("/embeddings:0")][0]

print(emb_weight, emb_weight.shape)
'''
[[-0.00572428  0.01988228 -0.01012505 ... -0.01063765  0.0132046
   0.02141862]
 [ 0.02374578  0.03060674  0.00305181 ...  0.02927439  0.00609263
  -0.02793145]
 [-0.0155357   0.00470876 -0.00169583 ... -0.02775752 -0.01873024
   0.02709173]
 ...
 [ 0.02812816  0.00374214 -0.02001397 ...  0.02371029  0.03101737
   0.02531628]
 [ 0.02015195 -0.00475615  0.01750962 ... -0.00634791 -0.01900101
   0.01833694]
 [ 0.00839748  0.02732043 -0.00321293 ...  0.01427403 -0.01608856
  -0.02168583]]
  (5000, 300)
'''


