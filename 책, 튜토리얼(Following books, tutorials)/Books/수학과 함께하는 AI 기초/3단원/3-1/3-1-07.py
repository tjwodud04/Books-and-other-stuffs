# 우리나라 선수들 출력하기
import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')
korea_player=fifa2019['Nationality'] == 'Korea Republic'
sub5 = fifa2019.loc[korea_player]

print(korea_player)
print(sub5)

'''
0        False
1        False
2        False
3        False
4        False
         ...  
18202    False
18203    False
18204    False
18205    False
18206    False
Name: Nationality, Length: 18207, dtype: bool
       Unnamed: 0      ID  ... GKReflexes  Release Clause
125           125  200104  ...       10.0          €71.2M
1295         1295  180283  ...       10.0          €14.3M
1407         1407  182152  ...        9.0          €12.8M
2002         2002  211927  ...        8.0          €17.6M
2021         2021  221671  ...        8.0          €13.8M
...           ...     ...  ...        ...             ...
17955       17955  240272  ...       12.0            €73K
17959       17959  245401  ...       12.0            €73K
17965       17965  243359  ...       11.0           €131K
18058       18058  244108  ...       10.0           €104K
18084       18084  244411  ...        5.0            €73K

[335 rows x 89 columns]
'''