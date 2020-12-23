# 여러 행의 데이터 중 원하는 열 값만 골라 출력하기
import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')
sub4 = fifa2019.iloc[0:10,1:3]

print(sub4)

'''
       ID               Name
0  158023           L. Messi
1   20801  Cristiano Ronaldo
2  190871          Neymar Jr
3  193080             De Gea
4  192985       K. De Bruyne
5  183277          E. Hazard
6  177003          L. Modrić
7  176580          L. Suárez
8  155862       Sergio Ramos
9  200389           J. Oblak
'''