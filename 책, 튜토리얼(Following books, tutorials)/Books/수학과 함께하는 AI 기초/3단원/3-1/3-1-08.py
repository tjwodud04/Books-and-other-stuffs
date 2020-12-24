# 우리나라 선수들의 이름 출력하기
import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')
korea_player = fifa2019['Nationality'] == 'Korea Republic'
sub5 = fifa2019.loc[korea_player]
sub6 = sub5['Name']

print(sub6)

'''
125               H. Son
1295       Ki Sung Yueng
1407        Koo Ja Cheol
2002     Kwon Chang Hoon
2021        Lee Jae Sung
              ...       
17955     Min Gyeong Min
17959       Lee Dong Hee
17965       Kim Jong Jin
18058    Hong Hyeon Seok
18084        Kwon Ki Pyo
Name: Name, Length: 335, dtype: object
'''