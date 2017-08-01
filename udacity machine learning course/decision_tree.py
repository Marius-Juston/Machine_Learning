#!/usr/bin/python

""" lecture and example code for decision tree unit """

from class_vis import prettyPicture
from classifyDT import classify
from prep_terrain_data import makeTerrainData

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the classify() function in classifyDT is where the magic
### happens--fill in this function in the file 'classifyDT.py'!
clf = classify(features_train, labels_train)

print clf.score(features_test, labels_test)

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
