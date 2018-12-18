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

#Summary
print(train.describe())

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

#Dira
plt.hist(signal.dira, range = (0.998, 1), bins = 100, label = 'Signal', alpha = 0.7, normed = True)
plt.hist(nonsignal.dira, range = (0.998, 1), bins = 100, label = 'Background', alpha = 0.7, normed = True)
plt.xlabel('Dira')
plt.ylabel('Count')
plt.legend()
plt.show()

#Flight Distance
plt.hist(signal.FlightDistance, range = (0, 100), bins = 100, label = 'Signal', alpha = 0.7, normed = True)
plt.hist(nonsignal.FlightDistance, range = (0, 100), bins = 100, label = 'Background', alpha = 0.7, normed = True)
plt.xlabel('Flight Distance')
plt.ylabel('Normalized Fraction')
plt.legend()
plt.show()

#Impact Paraneter
plt.hist(signal.IP, range = (0, 0.5), bins = 100, label = 'Signal', alpha = 0.7, normed = True)
plt.hist(nonsignal.IP, range = (0, 0.5), bins = 100, label = 'Background', alpha = 0.7, normed = True)
plt.xlabel('Impact Paraneter')
plt.ylabel('Count')
plt.legend()
plt.show()

#Track Isolation Variable
plt.hist(signal.iso, range=(0,20), bins=20, label='Signal', alpha=0.7,normed=True)
plt.hist(nonsignal.iso,range=(0,20),bins=20, label='Background',alpha=0.7,normed=True)
plt.xlabel('Track Isolation Variable')
plt.ylabel('Count')
plt.legend()
plt.show()

#Vertex chi^2
plt.hist(signal.VertexChi2, range=(0,16), bins=100, label='Signal', alpha=0.7,normed=True)
plt.hist(nonsignal.VertexChi2,range=(0,16),bins=100, label='Background',alpha=0.7,normed=True)
plt.xlabel(r'Vertex $\chi^2$')
plt.ylabel('Normalized Fraction')
plt.legend()
plt.show()

#Lifetime
plt.hist(signal.LifeTime, range=(0,1e-2), bins=50, label='Signal', alpha=0.7,normed=True)
plt.hist(nonsignal.LifeTime,range=(0,1e-2),bins=50, label='Background',alpha=0.7,normed=True)
plt.xlabel('Lifetime')
plt.ylabel('Count')
plt.legend()
plt.show()
