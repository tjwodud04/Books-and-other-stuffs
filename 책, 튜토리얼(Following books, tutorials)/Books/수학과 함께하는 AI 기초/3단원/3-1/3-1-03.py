# 궁금한 선수의 데이터 검색하기

import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')
sub1 = fifa2019.loc[14]

print(sub1)

'''
Unnamed: 0                                                    14
ID                                                        215914
Name                                                    N. Kanté
Age                                                           27
Photo             https://cdn.sofifa.org/players/4/19/215914.png
                                       ...                      
GKHandling                                                    12
GKKicking                                                     10
GKPositioning                                                  7
GKReflexes                                                    10
Release Clause                                           €121.3M
Name: 14, Length: 89, dtype: object
'''