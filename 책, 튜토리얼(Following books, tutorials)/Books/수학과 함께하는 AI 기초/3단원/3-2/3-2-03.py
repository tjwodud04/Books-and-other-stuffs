import csv

f = open('iris.csv')
data = csv.reader(f)
header = next(data)
result =[]

#전체 데이터를 행별로 result 리스트에 저장
for row in data :
    result.append(row)

#result에 저장된 값 중 꽃받침과 꽃잎의 길이, 너비 값을 숫자로 바꾸기
for i in result :
    for j in range(1,5) :
        i[j] = float(i[j])

#꽃 종류별 데이터 저장하기
a = []
b = []
c = []

for i in result :
    if i[5]=='Iris-setosa' :
        a.append(i[0:5])
    if i[5]=='Iris-versicolor' :
        b.append(i[0:5])
    if i[5]=='Iris-virginica' :
        c.append(i[0:5])

# iris-setosa의 꽃잎과 꽃받침 너비, 길이에 따른 평균값 구해보기
SL = []
SW = []
PL = []
PW = []

for i in a :
    SL.append(i[1])
    SW.append(i[2])
    PL.append(i[3])
    PW.append(i[4])
    
print('<Iris-setosa의 특성별 평균값>')
print('꽃받침 길이 평균:',round(sum(SL)/len(SL),3),
      '\n꽃받침 너비 평균:',round(sum(SW)/len(SW),3),
      '\n꽃잎 길이 평균:',round(sum(PL)/len(PL),3),
      '\n꽃잎 너비 평균:',round(sum(PW)/len(PW),3))

'''
<Iris-setosa의 특성별 평균값>
꽃받침 길이 평균: 5.006 
꽃받침 너비 평균: 3.418 
꽃잎 길이 평균: 1.464 
꽃잎 너비 평균: 0.244
'''
