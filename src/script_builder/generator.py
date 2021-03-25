import tensorflow as tf 
from tensorflow import keras
import numpy as np
import data


class SAGenerator(keras.Model):

	def __init__(self):
		super(SAGenerator, self).__init()
		self.fconv = tf.keras.layers.conv2d(kernel_size = 1, padding = "same")
		self.gconv = tf.keras.layers.conv2d(kernel_size = 1, padding = "same")
		self.hconv = tf.keras.layers.conv2d(kernel_size = 1, padding = "same")
		self.probabilityDistributionMap = tf.keras.layers.Multiply()
		self.attnMapSoftmax = tf.keras.layers.Softmax()
		self.attnMap = tf.keras.layers.Multiply()
		self.vconv = tf.keras.layers.conv2d(kernel_size = 1, padding = "same")

	def call(self, inputs, training=false):
		finput, ginput, hinput = inputs
		query = self.fconv(finput)
		key = self.gconv(ginput)
		value = self.gconv(hinput)
		probabilityDistributionMap = self.probabilityDistributionMap(tf.transpose(query), key)
		probabilityDistributionMapSoftmax = self.attnMapSoftmax(probabilityDistributionMap)
		attentionMap = self.attnMap(probabilityDistributionMapSoftmax)
		selfAttentionMap = self.vconv(attentionMap)
		return selfAttentionMap

