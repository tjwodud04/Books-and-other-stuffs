from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import numpy

boston = load_boston()
X = boston.data
Y = boston.target

lr1 = LinearRegression()
lr1.fit(X,Y)

print("Linear Regression")
for f, w in zip(boston.feature_names,lr1.coef_):
    print("{0:7s} {1:6.2f}".format(f,w))
print("coef = {0:4.2f}".format(sum(lr1.coef_**2)))

lr2 = Ridge(alpha=10.0)
lr2.fit(X,Y)
print("\n")
print("Ridge")
for f,w in zip(boston.feature_names,lr2.coef_):
    print("{0:7s} {1:6.2f}".format(f,w))
print("coef = {0:4.2f}".format(sum(lr2.coef_**2)))

lr3 = Ridge(alpha=2.0)
lr3.fit(X,Y)
print("\n")
print("Lasso")
for f,w in zip(boston.feature_names,lr3.coef_):
    print("{0:7s} {1:6.2f}".format(f,w))
print("coef = {0:4.2f}".format(sum(lr3.coef_**2)))