from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris

data = load_iris()

features = data['data'][:, [0, 2, 3]]
labels = data['target']

import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)

from sklearn.preprocessing import MinMaxScaler

scaller = MinMaxScaler()

features = scaller.fit_transform(features)

colors = ['r', 'g', 'b']

ax.scatter(features[:,0],features[:,1], features[:,2], c=labels)

ax.cla()

plt.show()