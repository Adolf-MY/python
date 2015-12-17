__author__ = 'Frank'
from sklearn import datasets,svm
iris  = datasets.load_iris()
digits = datasets.load_digits()
#print digits.data
#print digits.target
#print digits.images
clf = svm.SVC(gamma=0.0001,C=100.)