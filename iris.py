from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import recall_score, precision_score, f1_score, accuracy_score, confusion_matrix

def get_accuracy(i, true_y, pred_y):
  pass

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

for i,  train_index, test_index in enumarate( kf.split(X)):
  train_x, train_y, test_x, test_y = features[train_index], labels[train_index] , features[test_index], lables[test_index]
  
  clf.fit(train_x, train_y)
  
  pred = clf.predict(test_x)
  
  get_accuracy(i, test_y, pred)
  
  
  
  
  
