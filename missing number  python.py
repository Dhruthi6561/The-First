# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 20:05:23 2023

@author: sampa
"""
class My:
     def my():
         print("My")
     for i in range(0,6):
         my()
      
import numpy as np
arr = [[20, 2, 7, 1, 34],[20,2,7,1,2]]
  
print("arr : ", np.std(arr)) 
print("std of arr : ", np.std(arr,axis=0))         
a = np.empty([3,4],dtype=int)
for i in range(3):
    for j in range(4):
        a[i][j]=np.abs(i-j)
print(a)      
 
arr=np.array[1,2,3,4,5]
i=0
print(arr[i:i+1])
import numpy as np 
labels=np.zeros((9,10))
print(labels,end='\t')
import sys, numpy as np
from keras.datasets import mnist
import sys, numpy as np
(x_train, y_train), (x_test, y_test) = mnist.load_data()
images, labels = (x_train[0:1000].reshape(1000,28*28) /
 255, y_train[0:1000])
print(int(True))