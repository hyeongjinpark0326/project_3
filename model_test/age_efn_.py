from keras.layers.core import Dropout
import matplotlib.pyplot as plt
import tensorflow  as tf
import keras
from tensorflow.keras.layers import Input
import matplotlib.image as mpimg
import tensorflow.keras as Keras
from tensorflow.keras.applications import EfficientNetB0, EfficientNetB1
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.utils import *
from tensorflow.keras.layers import Dense, Flatten, GlobalMaxPooling2D, LeakyReLU, BatchNormalization
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint, EarlyStopping, LearningRateScheduler, ReduceLROnPlateau, CSVLogger
import efficientnet.keras as efn
from keras.regularizers import l1, l2
from tensorflow.keras import regularizers, optimizers
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from keras.layers import Conv2D, Conv3D, MaxPool2D, Flatten, AveragePooling2D
import cv2
import os, re, glob
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.layers.advanced_activations import LeakyReLU
from adabelief_tf import AdaBeliefOptimizer

path = "C:/Users/admin/Desktop/dddd/man/"
save_dir = os.path.join(os.getcwd(), 'age_gender_saved_models')
if not os.path.isdir(save_dir):
    os.makedirs(save_dir)

model_name = 'age_gender_mentor_1110.h5'
model_path = os.path.join(save_dir, model_name)
pixels = []
age = []
gender = []

for img in os.listdir(path):
    ages = img.split("_")[0]
    print(img.split("_")[1])
#     genders = img.split("_")[1]
#     # print(ages)
#     # print(str(path)+str(img))
#     img = cv2.imread(path+img)
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     pixels.append(np.array(img))
#     age.append(np.array(ages))
#     gender.append(np.array(genders))

# age = np.array(age,dtype=np.int64)
# pixels = np.array(pixels)
# gender = np.array(gender,np.uint64)
# # print(age)

# x_train,x_test,y_train,y_test = train_test_split(pixels,age,random_state=100)
# x_train_2,x_test_2,y_train_2,y_test_2 = train_test_split(pixels,gender,random_state=100)
# input = Input(shape=(200,200,3))
# conv1 = Conv2D(140,(5,5),activation="relu")(input)
# conv2 = Conv2D(130,(5,5),activation="relu")(conv1)
# batch1 = BatchNormalization()(conv2)
# pool3 = MaxPool2D((2,2))(batch1)
# conv3 = Conv2D(120,(3,3),activation="relu")(pool3)
# batch2 = BatchNormalization()(conv3)
# pool4 = MaxPool2D((2,2))(batch2)
# flt = Flatten()(pool4)
# #age neural network
# age_l = Dense(128,activation="relu")(flt)
# age_l = Dense(64,activation="relu")(age_l)
# age_l = Dense(32,activation="relu")(age_l)
# age_l = Dense(1,activation="relu")(age_l)

# # #gender neural network
# gender_l = Dense(128,activation="relu")(flt)
# gender_l = Dense(80,activation="relu")(gender_l)
# gender_l = Dense(64,activation="relu")(gender_l)
# gender_l = Dense(32,activation="relu")(gender_l)
# gender_l = Dropout(0.5)(gender_l)
# gender_l = Dense(2,activation="softmax")(gender_l)

# model = Model(inputs=input,outputs=[age_l, gender_l]) #??????????????? 2?????? ????????????
# model.summary() #?????? ?????? ?????????

# # plot_model(model, to_file='model_shapes.png', show_shapes=True) #?????? ?????? ????????????

# opt = AdaBeliefOptimizer(learning_rate=0.001)
# model.compile(optimizer=opt,
# loss=["mse","sparse_categorical_crossentropy"], #integer type ????????? -> one-hot encoding?????? ?????? ?????? ????????? label(y)??? ?????????
# metrics=['mae','accuracy']) #mse(mean squared error),mae(mean absolute error)
# early_stopping = keras.callbacks.EarlyStopping(
# monitor='val_loss', #val_loss??? ????????? ???????????? ?????? ??????
# patience=10, #????????? monitor ?????? ???????????? ??? ?????? epoch??? ????????? ??? ????????? ???
# verbose=1, #0??? ??????, ????????? ????????? ?????? ???????????????.
# mode='auto') #"auto"??? ????????? ????????? ???????????????.
# checkpoint = ModelCheckpoint(
# filepath= save_dir + "/1108.h5",
# monitor='val_loss', #validation set??? loss??? ?????? ?????? ??? ??????
# verbose=1, #0??? ?????? ????????? ???????????? ??? ?????? ?????? ?????? ????????? ???????????????.
# save_best_only=True,
# save_freq='epoch') #??????

# save = model.fit(x_train,[y_train,y_train_2],
# validation_data=(x_test,[y_test,y_test_2]),
# epochs=200,
# batch_size=16, #????????? ????????? ?????? ????????? ??????(16)
# callbacks=[early_stopping,checkpoint])
# #model.save(model_path)
# #print(save.history.keys()) #key ?????????

# #?????? ?????? ?????? ????????? ??????
# #loss ?????????
# plt.figure(figsize=(17, 4)) #???????????? ??????
# plt.subplot(1, 3, 1)
# plt.plot(save.history['dense_3_loss'], label='dense_3_loss')
# plt.plot(save.history['dense_8_loss'], label='dense_8_loss')
# plt.plot(save.history['val_dense_3_loss'], label='val_dense_3_loss')
# plt.plot(save.history['val_dense_8_loss'], label='val_dense_8_loss')
# plt.xlabel('Epochs')
# plt.ylabel('loss')
# plt.title('loss VS Epochs')
# plt.grid()
# plt.legend()

# #accuracy ?????????
# plt.subplot(1, 3, 2)
# plt.plot(save.history['dense_3_accuracy'], label='dense_3_accuracy')
# plt.plot(save.history['dense_8_accuracy'], label='dense_8_accuracy')
# plt.plot(save.history['val_dense_3_accuracy'], label='val_dense_3_accuracy')
# plt.plot(save.history['val_dense_8_accuracy'], label='val_dense_8_accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('accuracy')
# plt.title('accuracy VS Epochs')
# plt.grid()
# plt.legend()

# #MAE(Mean Absolute Error) ?????????
# plt.subplot(1, 3, 3)
# plt.plot(save.history['dense_3_mae'], label='dense_3_mae')
# plt.plot(save.history['dense_8_mae'], label='dense_8_mae')
# plt.plot(save.history['val_dense_3_mae'], label='val_dense_3_mae')
# plt.plot(save.history['val_dense_8_mae'], label='val_dense_8_mae')
# plt.xlabel('Epochs')
# plt.ylabel('mae')
# plt.title('mae VS Epochs')
# plt.grid()
# plt.legend()

# plt.show()