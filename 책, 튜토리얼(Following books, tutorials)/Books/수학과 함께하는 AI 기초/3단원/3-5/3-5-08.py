# And 연산 함수
def AND(x1,x2):
  #파라미터 값(w1,w2,임계값)
  w1,w2,threshold = 0.2,0.2,0.3
  temp = w1*x1+w2*x2

  if temp <= threshold:
    return 0
  elif temp > threshold:
    return 1

# OR 연산 함수
def OR(x1,x2):
  #파라미터 값(w1,w2,임계값)
  w1,w2,threshold = 0.3,0.3,0.2
  temp = w1*x1+w2*x2

  if temp <= threshold:
    return 0
  elif temp > threshold:
    return 1

# NAND 연산 함수
def NAND(x1,x2):
  #파라미터 값(w1,w2,임계값),AND의 역이므로 AND 가중치에 -1을 곱함
  w1,w2,threshold = -0.2,-0.2,-0.3
  temp = w1*x1+w2*x2

  if temp <= threshold:
    return 0
  elif temp > threshold:
    return 1

# XOR 연산을 퍼셉트론 함수로 나타내기
def XOR(x1,x2):
  h1 = NAND(x1,x2)
  h2 = OR(x1,x2)
  y = AND(h1,h2)
  return y

print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))

'''
0
1
1
0
'''
