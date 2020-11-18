import tensorflow as tf
from tensorflow.keras import layers, models

cnn_model = models.Sequential()
cnn_model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(224, 224, 3)))
cnn_model.add(layers.Conv2D(64, (3, 3), activation='relu'))
cnn_model.add(layers.MaxPooling2D(2, 2))
cnn_model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
cnn_model.add(layers.Conv2D(128, (3, 3), activation='relu'))
cnn_model.add(layers.MaxPooling2D(2, 2))
cnn_model.add(layers.Conv2D(256, (3, 3), activation='relu', padding='same'))
cnn_model.add(layers.Conv2D(256, (3, 3), activation='relu'))
cnn_model.add(layers.Conv2D(256, (3, 3), activation='relu'))
cnn_model.add(layers.MaxPooling2D(2, 2))
cnn_model.add(layers.Flatten())
cnn_model.summary()
'''result
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 224, 224, 64)      1792      
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 222, 222, 64)      36928     
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 111, 111, 64)      0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 111, 111, 128)     73856     
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 109, 109, 128)     147584    
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 54, 54, 128)       0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 54, 54, 256)       295168    
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 52, 52, 256)       590080    
_________________________________________________________________
conv2d_6 (Conv2D)            (None, 50, 50, 256)       590080    
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 25, 25, 256)       0         
_________________________________________________________________
flatten (Flatten)            (None, 160000)            0         
=================================================================
Total params: 1,735,488
Trainable params: 1,735,488
Non-trainable params: 0
_________________________________________________________________
'''

image_input = layers.Input(shape=(224, 224, 3))
visual_model = cnn_model(image_input)

question_input = layers.Input(shape=(100,), dtype='int32')
emdedding = layers.Embedding(input_dim=10000, output_dim=256, input_length=100)(question_input)
encoded_question = layers.LSTM(256)(emdedding)

merged = layers.concatenate([encoded_question, visual_model])
output = layers.Dense(1000, activation='softmax')(merged)

vqa_model = models.Model(inputs=[image_input, question_input], outputs=output)
vqa_model.summary()
'''
Model: "functional_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_2 (InputLayer)            [(None, 100)]        0                                            
__________________________________________________________________________________________________
embedding (Embedding)           (None, 100, 256)     2560000     input_2[0][0]                    
__________________________________________________________________________________________________
input_1 (InputLayer)            [(None, 224, 224, 3) 0                                            
__________________________________________________________________________________________________
lstm (LSTM)                     (None, 256)          525312      embedding[0][0]                  
__________________________________________________________________________________________________
sequential (Sequential)         (None, 160000)       1735488     input_1[0][0]                    
__________________________________________________________________________________________________
concatenate (Concatenate)       (None, 160256)       0           lstm[0][0]                       
                                                                 sequential[0][0]                 
__________________________________________________________________________________________________
dense (Dense)                   (None, 1000)         160257000   concatenate[0][0]                
==================================================================================================
Total params: 165,077,800
Trainable params: 165,077,800
Non-trainable params: 0
__________________________________________________________________________________________________
'''