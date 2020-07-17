#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:05:31 2020

@author: hajime.b
"""

import matplotlib.pyplot as plt
import cv2

import dataset
X_train,y_train = dataset.dataset()
    
for i in range(0, 8):

    plt.subplot(4, 4, i+1)
    plt.axis('off') #画像サイズの表記を消す

    if y_train[i] == 0:
        name = "dog"
    elif y_train[i] == 1:
        name = "cat"
    elif y_train[i] == 2:
        name = "gorilla"
    elif y_train[i] == 3:
        name = "Giraffes"
    elif y_train[i] == 4:
        name = "Lion"
        
    plt.title(label = name)
    img_array = cv2.cvtColor(X_train[i], cv2.COLOR_BGR2RGB)
    plt.subplots_adjust(bottom = 0,top = 1.3) #ラベルが画像とかぶらないよう調整
    plt.imshow(img_array)

plt.show()