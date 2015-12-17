__author__ = 'Frank'
from sklearn import linear_model
clf = linear_model.RidgeCV(alphas = [0.001,0.0099,0.1,0.2,0.3,1.0,10])
clf.fit([[0,0],[0,0],[1,1]],[0,0.1,1])
print clf.alpha_