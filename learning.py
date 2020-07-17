#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:55:28 2020

@author: hajime.b
"""
import cv2
from sklearn import svm

import dataset
X_train,y_train = dataset.dataset()
print(X_train.ndim)

clf = svm.SVC(gamma=0.001)
clf.fit(X_train,y_train)

#img = cv2.imread("/Users/hajime.b/Documents/test") 

#predict = clf.predict(img)
#print(predict)