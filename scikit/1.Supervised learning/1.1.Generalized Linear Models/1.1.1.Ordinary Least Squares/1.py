__author__ = 'Frank'
from sklearn import linear_model
clf = linear_model.LinearRegression()
clf.fit([[0,0],[1,1],[2,2]],[1,2,3])
print clf.coef_
print clf.residues_
print clf.intercept_