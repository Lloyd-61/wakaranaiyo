#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:32:36 2020

@author: hajime.b
"""


import os
import cv2
import random
import numpy as np

def dataset():
    DATADIR = "/Users/hajime.b/Documents/animals" #動物の画像フォルダ
    CATEGORIES = ["dogs", "cats","gorillas","Giraffes","Lions"] #各動物のフォルダ名
    training_data = []
    
    for animal_num,animal_name in enumerate(CATEGORIES):
        path = os.path.join(DATADIR, animal_name)
        for image_name in os.listdir(path):
            try:
                img = cv2.imread(os.path.join(path, image_name),)  # 画像の読み込み
                img_resize = cv2.resize(img, (50, 50))  # 画像のサイズを50x50に統一
                training_data.append([img_resize, animal_num])  # 画像データ、ラベル情報を追加
            except Exception :
                pass
    
    
    random.shuffle(training_data)  # データをシャッフル
    
    X_train = []  # 画像データ
    y_train = []  # ラベル情報
    
    # データセット作成
    for animal_img, label in training_data:
        X_train.append(animal_img)
        y_train.append(label)
    
    # numpy配列に変換
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    reshaped_train_data = np.reshape(X_train, (405, 2500))
    
    return (reshaped_train_data,y_train)