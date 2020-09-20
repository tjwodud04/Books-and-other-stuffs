from tensorflow.keras.applications.vgg16 import VGG16
import numpy as np
import cv2
import matplotlib.pyplot as plt

model = VGG16(weights='imagenet', include_top=True)
model.compile(optimizer='sgd', loss='categorical_crossentropy')

im = cv2.resize(cv2.imread('steam-locomotive.jpg'), (224, 224))
im = np.expand_dims(im, axis=0)
im.astype(np.float32)

out = model.predict(im)
index = np.argmax(out)

print(index)
'''result
820
'''

plt.plot(out.ravel())
plt.show()
