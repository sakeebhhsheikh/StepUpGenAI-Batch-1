import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

(xtrain, xtest), (ytrain, ytest) = datasets.cifar10.load_data()

#print(xtrain[0])

