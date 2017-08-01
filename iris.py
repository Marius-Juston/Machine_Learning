from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

data = load_iris()

features = np.array( data['data'][:, [0, 2, 3]])
labels = np.array(data['target'])

fig = plt.figure()
ax = Axes3D(fig)

from sklearn.preprocessing import MinMaxScaler

scaller = MinMaxScaler()

features = scaller.fit_transform(features)

colors = ['r', 'g', 'b']

ax.scatter(features[:,0],features[:,1], features[:,2], c=labels)
plt.show()

clf = KNeighborsClassifier(n_neighbors=3)

kf = KFold(n_splits=10, random_state=42, shuffle=True)

for  train_index, test_index in kf.split(X):
  train_x, train_y, test_x, test_y = features[train_index], labels[train_index] , features[test_index], lables[test_index]
  
  
  
  
  
  
  
