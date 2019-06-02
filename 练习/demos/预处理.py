import os
import numpy as np
import pandas as pd

data_dir = r'E:\Hadoop\data'
file_name = 'poker-hand-testing1.csv'

data = np.loadtxt(os.path.join(data_dir, file_name))

data[:, 0] -= 1.
#shuffle
indices = list(range(data.shape[0]))
np.random.shuffle(indices)
data = data[indices]

labled = data[:500]
unlabled = data[500:]

np.savetxt(os.path.join(data_dir, 'poker-hand-testing1_labeled.txt'), labled, fmt='%.5f')
np.savetxt(os.path.join(data_dir, 'poker-hand-testing1.txt'), unlabled, fmt='%.5f')
print(unlabled.shape)
print(labled.shape)

