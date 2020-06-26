# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:16:56 2020

@author: duyif
"""

import numpy as np
import PIL


class DOG():
    def __init__(self, radius=5, sigema=1.6):
        self.radius=radius
        self.sigema=sigema   
        self.pi = 3.141593
        
    def gaussian(self,x,y):
        res1=1/(2*self.pi*self.sigema*self.sigema)
        res2=np.exp(-(x*x+y*y)/(2*self.sigema*self.sigema))
        return res1*res2
    
    def template(self):
        sideLength=self.radius*2+1
        result = np.zeros((sideLength, sideLength))
        for i in range(sideLength):
            for j in range(sideLength):
                result[i,j]=self.gaussian(i-self.radius, j-self.radius)
        all=result.sum()
        return result/all    
    
    def filter(self, image, template): 
        arr=np.array(image)
        height=arr.shape[0]
        width=arr.shape[1]
        newData=np.zeros((height, width))
        for i in range(self.radius, height-self.radius):
            for j in range(self.radius, width-self.radius):
                t=arr[i-self.radius:i+self.radius+1, j-self.radius:j+self.radius+1]
                a= np.multiply(t, template)
                newData[i, j] = a.sum()
        newImage = PIL.Image.fromarray(newData)          
        return newImage
    
    def diff(self, image):
        temp = self.template()
        
        image2 = self.filter(image, temp)
        image3 = self.filter(image2, temp)
        image4 = self.filter(image3, temp)
        
        DOG_result = np.zeros([3, image.size[1], image.size[0]], dtype = float)
        DOG_result[0, :, :] = np.asarray(image) - np.asarray(image2)
        DOG_result[1, :, :] = np.asarray(image2) - np.asarray(image3)
        DOG_result[2, :, :] = np.asarray(image3) - np.asarray(image4)
        return DOG_result
'''        
layer3=MyGaussianBlur(radius=5, sigema=4.8)#声明高斯模糊类
temp1=layer3.template()
layer4=MyGaussianBlur(radius=5, sigema=6.4)#声明高斯模糊类    
temp2=layer4.template()

im=PIL.Image.open("C:\\Users\\duyif\\OneDrive\\Birmingham\\GraduationProject\\code\\Surf\\BMW_1.png")#打开图片
im = im.convert("L")
image3=layer3.filter(im, temp1)#高斯模糊滤波，得到新的图片
image4=layer4.filter(im, temp2)#高斯模糊滤波，得到新的图片

image5 = np.asarray(image3) - np.asarray(image4)
PIL.Image.fromarray(np.uint8(image5)).show()
'''
test = DOG()
im=PIL.Image.open("C:\\Users\\duyif\\OneDrive\\Birmingham\\GraduationProject\\code\\Surf\\BMW_1.png")#打开图片
im = im.convert("L")

t1 = test.diff(im)
PIL.Image.fromarray(np.uint8(t1[0, :, :])).show()
PIL.Image.fromarray(np.uint8(t1[1, :, :])).show()
PIL.Image.fromarray(np.uint8(t1[2, :, :])).show()