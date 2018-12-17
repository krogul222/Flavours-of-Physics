#%%
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 

#Load data
train = pd.read_csv('data/training.csv', index_col = 0)
test = pd.read_csv('data/test.csv', index_col = 0)

#Head of train data
print(train.head())

#Info
print(train.info())

#Signal and backgorund
signal = train[train.signal == 1]
nonsignal = train[train.signal == 0]

#Transverse Momentum
plt.hist(signal.pt/1000, range = (0, 25), bins = 100, label = 'Signal', alpha = 0.7, normed = True)
plt.hist(nonsignal.pt/1000, range = (0, 25), bins = 100, label = 'Background', alpha = 0.7, normed = True)
plt.xlabel('Transverse Momentum')
plt.ylabel('Normalized Fraction')
plt.legend()
plt.show()