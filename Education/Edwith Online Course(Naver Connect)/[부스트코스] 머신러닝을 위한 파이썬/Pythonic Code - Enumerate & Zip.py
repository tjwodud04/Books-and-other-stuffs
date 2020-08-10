alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for a, b in zip(alist, blist):
    print(a, b)
'''
a1 b1
a2 b2
a3 b3
'''

a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 200, 300))
print(a, b, c)

'''
(1, 10, 100) (2, 20, 200) (3, 30, 300)
'''

print([sum(x) for x in zip((1, 2, 3), (10, 20, 30), (100, 200, 300))])
'''
[111, 222, 333]
'''

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

for i, (a, b) in enumerate(zip(alist, blist)):
    print(i, a, b)
'''
0 a1 b1
1 a2 b2
2 a3 b3
'''