import numpy as np
import struct
import cv2
 
def readfile():#读取源图片文件
    with open('E:\\t10k-images.idx3-ubyte','rb') as f1:
        buf1 = f1.read()
    return buf1
 
def get_image(buf1):#解析并保存图片
    image_index = 0
    image_index += struct.calcsize('>IIII')
    magic,numImages,imgRows,imgCols=struct.unpack_from(">IIII",buf1,0)
    im = []
    for i in range(numImages):
        temp = struct.unpack_from('>784B', buf1, image_index)
        im=np.array(temp)
        im2=im.reshape(28,28)
        cv2.imwrite("E:\\testImages\\testIM"+str(i)+".jpg",im2)#保存路径自己设置
        image_index += struct.calcsize('>784B')  # 28*28=784(B)
        if i%20==0:#知道图片保存的进度
            print i
        else:
            print i,
 
