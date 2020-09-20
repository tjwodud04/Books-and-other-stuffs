from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras import models
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
import numpy as np

base_model = VGG16(weights='imagenet', include_top=True)

print (base_model)
''' result
<tensorflow.python.keras.engine.functional.Functional object at 0x000001330636DF48>
'''

for i, layer in enumerate(base_model.layers):
	print (i, layer.name, layer.output_shape)
'''result
0 input_1 [(None, 224, 224, 3)]
1 block1_conv1 (None, 224, 224, 64)
2 block1_conv2 (None, 224, 224, 64)
3 block1_pool (None, 112, 112, 64)
4 block2_conv1 (None, 112, 112, 128)
5 block2_conv2 (None, 112, 112, 128)
6 block2_pool (None, 56, 56, 128)
7 block3_conv1 (None, 56, 56, 256)
8 block3_conv2 (None, 56, 56, 256)
9 block3_conv3 (None, 56, 56, 256)
10 block3_pool (None, 28, 28, 256)
11 block4_conv1 (None, 28, 28, 512)
12 block4_conv2 (None, 28, 28, 512)
13 block4_conv3 (None, 28, 28, 512)
14 block4_pool (None, 14, 14, 512)
15 block5_conv1 (None, 14, 14, 512)
16 block5_conv2 (None, 14, 14, 512)
17 block5_conv3 (None, 14, 14, 512)
18 block5_pool (None, 7, 7, 512)
19 flatten (None, 25088)
20 fc1 (None, 4096)
21 fc2 (None, 4096)
22 predictions (None, 1000)
'''

model = models.Model(inputs=base_model.input, outputs=base_model.get_layer('block4_pool').output)

img_path = 'cat.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

features = model.predict(x)

print(features)
'''result
[[[[  0.         0.        39.12757  ...   0.         0.
      0.      ]
   [  0.         0.         0.       ...   0.       261.40982
      0.      ]
   [  0.         0.         0.       ...   0.       376.4143
      0.      ]
   ...
   [  0.         0.         0.       ...   0.       175.46504
      0.      ]
   [  0.         0.        32.008057 ...   0.         0.
      0.      ]
   [  0.         0.        76.2813   ...   0.         0.
      0.      ]]

  [[  0.         0.         0.       ...   0.        50.920372
      0.      ]
   [  0.         0.        44.453056 ...   0.       123.95481
      0.      ]
   [  0.         0.        27.892405 ...   0.       573.442
      0.      ]
   ...
   [  0.         0.         0.       ...   0.       683.4284
      0.      ]
   [  0.         0.         0.       ...   0.        18.347548
      0.      ]
   [  0.         0.        60.561672 ...   0.         0.
      0.      ]]

  [[  0.         0.        27.617815 ...   0.         0.
      0.      ]
   [  0.       372.48434    0.       ...  29.13428    0.
      0.      ]
   [  0.        34.77293  105.495316 ...   0.         0.
      0.      ]
   ...
   [  0.         0.         0.       ...   0.       823.4674
      0.      ]
   [  0.         0.         0.       ...   0.        95.23569
      0.      ]
   [  0.         0.        20.043055 ...   0.         0.
      0.      ]]

  ...

  [[  0.         0.         0.       ...   0.        58.513264
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]
   ...
   [  0.         0.         0.       ...   0.       376.75186
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]
   [  0.         0.         9.004295 ...   0.         0.
      0.      ]]

  [[  0.         0.         0.       ...   0.       112.54105
      0.      ]
   [  0.         0.         0.       ...   0.        48.298763
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]
   ...
   [  0.         0.         0.       ...   0.       340.15616
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]]

  [[  0.         0.        33.473633 ...   0.        89.463806
      0.      ]
   [  0.         0.         0.       ...   0.       169.87445
      0.      ]
   [  0.         0.         0.       ...   0.         0.
      0.      ]
   ...
   [  0.         0.         0.       ...   0.       142.926
      0.      ]
   [  0.         0.         0.       ...   0.        14.979055
      0.      ]
   [  0.         0.        51.729137 ...   0.         0.
      0.      ]]]]
'''