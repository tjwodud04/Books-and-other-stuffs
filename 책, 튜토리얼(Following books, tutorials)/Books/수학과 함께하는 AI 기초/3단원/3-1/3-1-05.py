# 전체 선수들의 이름과 선호하는 발 정보 출력하기
import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')
sub3 = fifa2019.loc[:,['Name', 'Preferred Foot']]

print(sub3)

'''
                     Name Preferred Foot
0                L. Messi           Left
1       Cristiano Ronaldo          Right
2               Neymar Jr          Right
3                  De Gea          Right
4            K. De Bruyne          Right
...                   ...            ...
18202        J. Lundstram          Right
18203  N. Christoffersson          Right
18204           B. Worman          Right
18205      D. Walker-Rice          Right
18206           G. Nugent          Right

[18207 rows x 2 columns]
'''