# 데이터 불러오기
import pandas as pd

fifa2019 = pd.read_csv('fifa2019.csv')
df = pd.DataFrame.copy(fifa2019.sort_values(by = 'Overall', ascending = False).head(200))
test_features = ['Name','Stamina','Dribbling','ShortPassing','Penalties']
test_df = pd.DataFrame(df, columns = test_features)

print(test_df.head(5))

'''
                Name  Stamina  Dribbling  ShortPassing  Penalties
0           L. Messi     72.0       97.0          90.0       75.0
1  Cristiano Ronaldo     88.0       88.0          81.0       85.0
2          Neymar Jr     81.0       96.0          84.0       81.0
3             De Gea     43.0       18.0          50.0       40.0
4       K. De Bruyne     90.0       86.0          92.0       79.0
'''