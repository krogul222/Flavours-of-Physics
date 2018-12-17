import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

#Load data
train = pd.read_csv('training.csv', index_col = 0)
test = pd.read_csv('test.csv', index_col = 0)

#Head of train data
print(train.head())

#Info
print(train.info())

signal = train[train.signal == 1]
nonsignal = train[train.signal == 0]
plt.hist(signal.pt/1000, range = (0, 25), bins = 100, label = 'Signal', alpha = 0.7, normed = True)
plt.hist(signal.pt/1000, range = (0, 25), bins = 100, label = 'Background', alpha = 0.7, normed = True)