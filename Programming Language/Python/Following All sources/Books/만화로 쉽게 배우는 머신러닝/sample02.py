from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

breast_cancer = load_breast_cancer()
X = breast_cancer.data
Y = breast_cancer.target

clf1 = LogisticRegression()
clf1.fit(X,Y)

print("Logistic Regression")
for f, w in zip(breast_cancer.feature_names,clf1.coef_[0]):
    print("{0:<23} {1:6.2f}".format(f,w))

clf2 = DecisionTreeClassifier(max_depth=2)
clf2.fit(X,Y)
print("\n")
print("DecisionTree Classifier")
for f, w in zip(breast_cancer.feature_names,clf1.coef_[0]):
    print("{0:<23} {1:6.2f}".format(f,w))
