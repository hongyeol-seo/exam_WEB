from PIL import Image, ImageFilter
import cv2
import numpy as np
import pandas as pd
FILE = 'lenna.png'
# FILE = 'image/2469014858A79ABA0C.jpg'

# img = Image.open(FILE)
# print(img.size)
# print(img.format)

# img.show()

# area = (100, 100, 320, 320)
# cropImage = img.crop(area)

# cropImage.show()

# size = (64, 64)
# img.thumbnail(size) # Thumbnail 이미지 생성
# img.save('lenna_2.png')
# img.show()

# img = Image.open('lenna.png')
# img2 = img.resize((300, 300)) # tuple 형태의 크기(가로 크기, 세로 크기)
# img2.save('lenna_300.png')
# img2.show()

# img3 = img.rotate(90) # counter-clockwise (반시계방향)
# img3.save('lenna_rotate.png')
# img3.show()

img = Image.open('lenna.png')
# contourImage = img.filter(ImageFilter.CONTOUR)
# contourImage.save('lenna-contour.png')
# contourImage.show()


# new_york = Image.open('newyork.jpg')

# r, g, b = new_york.split()
# r.save('newyork_r.jpg')
# g.save('newyork_g.jpg')
# b.save('newyork_b.jpg')
# r.show()
# g.show()
# b.show()

from PIL import Image
import matplotlib.pyplot as plt 
car = Image.open('newyork.jpg')

test = cv2.imread('newyork.jpg')
print(test)
print("*"*50)

# print(test.shape)
# print(type(test))


#판다스

# pd1 = pd.DataFrame(test)
# print(pd1)



# cv2.imshow('iu',test.transpose)
# cv2.waitKey(50000)


# print(len(test[0]))

for i in range(864):
    
    # test[i].reverse()
    test[i] = np.flip(test[i],axis=0)

print(test)

# # print(Image(test))
# # plt.imshow(test)

# # test.save("t1.png")
# # test.show() 


# # contourImage.save('lenna-contour.png')
# # contourImage.show()


# 1번 출력
cv2.imshow('iu',test).save('test.jpg')

# cv2.waitKey(50000)

# t2 = np.transpose(t1,(1,0,2))
# cv2.imshow('iu', t2)
# cv2.waitKey(50000)



