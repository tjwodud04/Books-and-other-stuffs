import pandas as pd
import numpy as np
iris = pd.read_csv('Iris.csv')
 
# 150개 데이터의 특성 데이터와 종류 데이터를 나누어 저장하기
xy = np.array(iris)
features = xy[:, 1:-1]
target_value = xy[:, [-1]]

# 유클리드 거리법을 이용하여 두 데이터 간의 거리를 구하는 함수 선언하기
def Distance(A, B):
    return np.sqrt(np.sum(np.power((A-B),2)))

# 붓꽃 분류기 함수 작성하기
def K_NN(Unknown,features,K):
    distance_result = np.zeros(150)

    for i in  range(150):
        distance_result[i]= Distance(Unknown,features[i])

    index = distance_result.argsort()
    target_result = []
    result = [0, 0, 0]

    for i in range(K):
        target_result.append(target_value[index[i]])

        if target_result[i]=='Iris-setosa':
           result[0]+=1
        elif target_result[i]=='Iris-versicolor':
             result[1]+=1
        else:
             result[2]+=1

    max_label=result.index(max(result))
    species = {0:"setosa", 1:"versicolor", 2:"virginica"}
    species_result = species[max_label]

    return species_result

# 붓꽃 분류 함수를 사용하여 가상의 데이터 분류하기
test_1 = features[149]
test_2 = np.array([6,2.9,5,2])
result_1 = K_NN(test_1,features,5)
result_2 = K_NN(test_2,features,5)

print("실제 데이터를 분류한 결과 : {0}".format(result_1))
print("가상 데이터를 분류한 결과 : {0}" .format(result_2))

'''
실제 데이터를 분류한 결과 : virginica
가상 데이터를 분류한 결과 : virginica
'''