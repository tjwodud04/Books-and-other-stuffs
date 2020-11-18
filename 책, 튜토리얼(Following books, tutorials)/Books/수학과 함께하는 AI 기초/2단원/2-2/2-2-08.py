# 합성한 이미지 저장하기

import numpy as np
import matplotlib.pyplot as plt 
import PIL.Image as pilimg

im1 = pilimg.open("jeju_summer.jpg")
im2 = pilimg.open("baby1.jpg")
im3 = pilimg.open("baby2.jpg")

pix1 = np.array(im1)

resizeX2 = pix1.shape[1]/2

if(pix1.shape[1] % 2 > 0) :
    resizeX1 = pix1.shape[1]/2 + 1
else :
    resizeX1 = pix1.shape[1]/2

im2 = im2.resize((int(resizeX1), int(pix1.shape[0])))
pix2 = np.array(im2)

im3 = im3.resize((int(resizeX2), int(pix1.shape[0])))
pix3 = np.array(im3)

pix4 = np.concatenate((pix2, pix3), axis = 1)

pix1 = (1/255)*pix1
pix4 = (1/255)*pix4 

weight = 0.3

pix5 = pix1 * weight + pix4 * (1-weight)
pix6 = pix1 * (1-weight) + pix4 * weight

pix5 = pix5*255
im5 = pilimg.fromarray(pix5.astype(np.uint8))
im5.save("BlendedPic_70.png")

pix6 = pix6*255
im6 = pilimg.fromarray(pix6.astype(np.uint8))
im6.save("BlendedPic_30.png")
