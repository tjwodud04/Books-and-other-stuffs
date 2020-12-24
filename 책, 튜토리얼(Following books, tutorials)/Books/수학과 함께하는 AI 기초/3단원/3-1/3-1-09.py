# 선수들이 선호하는 발의 종류 데이터를 막대그래프로 나타내기
import pandas as pd
import matplotlib.pyplot as plt

fifa2019 = pd.read_csv('fifa2019.csv')

fifa2019['Preferred Foot'].value_counts().plot(kind='bar')

plt.legend()
plt.show()
