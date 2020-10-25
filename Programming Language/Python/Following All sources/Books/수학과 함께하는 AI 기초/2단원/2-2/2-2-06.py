# 여러 색을 갖는 이미지 데이터 표현하기

import numpy as np                  # 벡터, 행렬 데이터를 쉽게 처리하기 위한 모듈
import matplotlib.pyplot as plt     # 화면에 이미지 데이터를 보여주기 위한 모듈 
import PIL.Image as pilimg          # 이미지 파일과 데이터 처리를 위한 모듈

im = pilimg.open( "rgb_circle.bmp" )

pix = np.array(im)
pixSize = np.array(pix.shape)

print(pixSize)

pix_R = pix.copy()
pix_R[:, :, (1,2)] = 0
pix_G = pix.copy()
pix_G[:, :, (0,2)] = 0
pix_B = pix.copy()
pix_B[:, :, (0,1)] = 0

plt.subplot(141)
plt.imshow(pix)
plt.axis("off")
plt.title("RGB")

plt.subplot(142)
plt.imshow(pix_R)
plt.axis("off")
plt.title("R(Red)")

plt.subplot(143)
plt.imshow(pix_G)
plt.axis("off")
plt.title("G(Green)")

plt.subplot(144)
plt.imshow(pix_B)
plt.axis("off")
plt.title("B(Blue)")
plt.show()

'''
[219 230   3]
'''