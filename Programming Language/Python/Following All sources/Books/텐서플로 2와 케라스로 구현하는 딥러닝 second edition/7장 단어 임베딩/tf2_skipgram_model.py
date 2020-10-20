import tensorflow as tf

class SkipgramModel(tf.keras.Model):
    def __init__(self, vocab_sz, embed_sz, window_sz, **kwargs):
        super(SkipgramModel, self).__init__(**kwargs)
        self.word_model = tf.keras.Sequential([
            tf.keras.layers.Embedding(
                input_dim=vocab_sz,
                output_dim=embed_sz,
                embeddings_initializer="glorot_uniform",
                input_length=1
            ),
            tf.keras.layers.Reshape((embed_sz,))
        ])
        self.context_model = tf.keras.Sequential([
            tf.keras.layers.Embedding(
                input_dim=vocab_sz,
                output_dim=embed_sz,
                embeddings_initializer="glorot_uniform",
                input_length=1
            ),
            tf.keras.layers.Reshape((embed_sz,))
        ])
        self.merge = tf.keras.layers.Dot(axes=1) #Changing existing code (axes=0) -> (axes=1)
        self.dense = tf.keras.layers.Dense(1, kernel_initializer="glorot_uniform", activation="sigmoid")

    def call(self, input):
        word, context = input
        word_emb = self.word_model(word)
        context_emb = self.context_model(context)
        x = self.merge([word_emb, context_emb])
        x = self.dense(x)
        return x

VOCAB_SIZE = 5000
EMBED_SIZE = 300
WINDOW_SIZE = 1

model = SkipgramModel(VOCAB_SIZE, EMBED_SIZE, WINDOW_SIZE)
model.build(input_shape=[(VOCAB_SIZE, None), (VOCAB_SIZE, None)])
#Changing existing code [(None, VOCAB_SIZE), (None, VOCAB_SIZE)]) -> [(VOCAB_SIZE, None), (VOCAB_SIZE, None)]
model.compile(optimizer=tf.optimizers.Adam(),
              loss="categorical_crossentropy",
              metrics=["accuracy"])

model.summary()
'''
Model: "skipgram_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
sequential (Sequential)      (None, 300)               1500000   
_________________________________________________________________
sequential_1 (Sequential)    (None, 300)               1500000   
_________________________________________________________________
dot (Dot)                    multiple                  0         
_________________________________________________________________
dense (Dense)                multiple                  2         
=================================================================
Total params: 3,000,002
Trainable params: 3,000,002
Non-trainable params: 0
_________________________________________________________________
'''

word_model = model.layers[0]
word_emb_layer = word_model.layers[0]
emb_weights = None

for weight in word_emb_layer.weights:
    if weight.name == "embedding/embeddings:0":
        emb_weights = weight.numpy()

print(emb_weights, emb_weights.shape)
'''
[[-0.01546515 -0.01022839  0.01725376 ... -0.00563864  0.01793675
   0.02436406]
 [ 0.01338347  0.01043614 -0.00911259 ...  0.02533719  0.01901378
   0.01490542]
 [-0.02934115  0.01357176 -0.03029594 ...  0.03259882 -0.02180077
  -0.03358893]
 ...
 [ 0.03015737  0.02543042  0.02174363 ...  0.02998263 -0.02844361
  -0.00528611]
 [-0.02284687  0.01668065  0.02356544 ... -0.00070568 -0.02237626
   0.027332  ]
 [ 0.01130722  0.00611316  0.00992544 ...  0.01310709  0.00693739
   0.00702661]]
(5000, 300)
'''