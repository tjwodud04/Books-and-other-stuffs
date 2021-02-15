file = open("test2.txt", 'r', encoding='utf-8')
rl = file.readlines()

file.close()

for i in rl:
    print(i.rstrip("\n"))

'''
파이썬으로
만드는
게임 개발
'''