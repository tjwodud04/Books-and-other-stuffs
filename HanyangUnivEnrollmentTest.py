import random

def sum(n):
    integers = 0
    for N in range(1, n+1):
        integers += N
    return integers

def sumoflist(n):
    A = []
    for i in range(1, n+1):
        A.append(i)
    newA = random.choice(A)
    A.remove(newA)
    total = 0
    for j in range(len(A)):
        total += A[j]
    return total

def missingnum(n):
    lasttotal = sum(n) - sumoflist(n)
    return lasttotal

#print(sum(100))
#print(sumoflist(100))
# print(sum(100)-sumoflist(100))
print(missingnum(100))

#생각한 방식
# 1부터 n+1의 연속된 합(n(n+1)/2)을 A라는 리스트 안의 정수를 모두 더한 값으로 빼면 missing된 값이 나올 것이다.