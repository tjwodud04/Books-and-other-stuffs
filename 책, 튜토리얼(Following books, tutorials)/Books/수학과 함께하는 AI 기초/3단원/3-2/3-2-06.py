import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('Iris.csv')

# 꽃받침(Sepal)의 길이와 너비에 따른 분산형(scatter) 그래프
fig = iris[iris.Species=='Iris-setosa'].plot(
    kind='scatter',
    x='SepalLengthCm',
    y='SepalWidthCm',
    color='orange',
    label='Setosa')

iris[iris.Species=='Iris-versicolor'].plot(
    kind='scatter',
    x='SepalLengthCm',
    y='SepalWidthCm',
    color='blue',
    label='versicolor',
    ax=fig)

iris[iris.Species=='Iris-virginica'].plot(
    kind='scatter',
    x='SepalLengthCm',
    y='SepalWidthCm',
    color='green',
    label='virginica',
    ax=fig)

fig.set_xlabel("Sepal Length")
fig.set_ylabel("Sepal Width")
fig.set_title("Sepal Length VS Width")

fig=plt.gcf()

fig.set_size_inches(10,6)
plt.show()

