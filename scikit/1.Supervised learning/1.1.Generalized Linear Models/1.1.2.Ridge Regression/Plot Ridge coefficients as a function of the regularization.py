__author__ = 'Frank'
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
x = 1./(np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
y = np.ones(10)
n_alphas = 200
alphas = np.logspace(-10,-2,n_alphas)
clf = linear_model.Ridge(fit_intercept = False)
coefs= []
for i in alphas:
    clf.set_params(alpha = i)
    clf.fit(x,y)
    coefs.append(clf.coef_)