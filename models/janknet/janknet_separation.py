# -*- coding: utf-8 -*-
"""

Very minimal architecture similar to Keras basic autoencoder 

Allen Ma
"""

import sys
sys.path.insert(0, '../../')

import keras
import tensorflow as tf
import keras.backend

from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Dropout
from keras.models import Model
from keras import backend as K
from keras.models import load_model

from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint
from keras.losses import mse

from supermodel import SuperModel

# true image is the illumination map that was used to construct the input image
# pred image is the generated illumination map * 0.5 


# input_img = Input(shape=(128, 128, 3))  # adapt this if using `channels_first` image data format

class JankNet(SuperModel):
    def __init__(self, input_size=(128, 128, 3)):

        input_img = Input(shape=(128,128,3))

        # encoder layer
        x = Conv2D(8, (3, 3), activation='selu', padding='same')(input_img)
        x = MaxPooling2D((2, 2), padding='same')(x)
        x = Conv2D(16, (3, 3), activation='selu', padding='same')(x)
        x = MaxPooling2D((2, 2), padding='same')(x)
        x = Conv2D(32, (3, 3), activation='selu', padding='same')(x)
        x = Conv2D(32, (3, 3), activation='selu', padding='same')(x)
        x = MaxPooling2D((2, 2), padding='same')(x)
        x = Conv2D(64, (3, 3), activation='selu', padding='same')(x)
        x = Conv2D(32, (1, 1), activation='sigmoid', padding='same')(x)
        encoded = MaxPooling2D((2, 2), padding='same')(x)
        # ensure everything is between 0 and 1

        # at this point the representation is (16, 16, 32) i.e. 2048-dimensional

        x = Conv2D(32, (3, 3), activation='selu', padding='same')(encoded)
        x = UpSampling2D((2, 2))(x)
        x = Conv2D(16, (3, 3), activation='selu', padding='same')(x)
        x = UpSampling2D((2, 2))(x)
        x = Conv2D(8, (3, 3), activation='selu', padding='same')(x)
        x = UpSampling2D((2, 2))(x)
        x = Conv2D(1, (3, 3), activation='selu', padding='same')(x)
        x = UpSampling2D((2, 2))(x)
        decoded_imap = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)


        self.model = Model(input_img, decoded_imap)
        self.model.compile(optimizer='adam', loss=self.imap_only_loss, metrics=['mse'])
        
        
    def imap_only_loss(self, true_img, pred_img):
       return K.mean(K.square(true_img - pred_img))


    # def __str__(self):
    #     return self.model.summary()
    
    # def train(self, len_data, batch_size, num_epochs, gen, callbacks_list=[]):
    #     '''
    #         call this to train the network
    #         gen - a generator function to pass into model.fit_generator()
    #     '''
    #     return self.model.fit_generator(gen, steps_per_epoch= len_data / batch_size, epochs=num_epochs, verbose=1)

    # def evaluate(self, len_data, batch_size, gen, callbacks_list=[]):
    #     '''
    #         call this to run keras evaluate_generator on the network
    #     '''
    #     return self.model.evaluate_generator(gen, steps=len_data / batch_size, verbose=1)

        
        




