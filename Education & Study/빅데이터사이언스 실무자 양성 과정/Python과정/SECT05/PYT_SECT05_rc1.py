#01
bts_members = ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
print('멤버 :', bts_members)
print('타입 :', type(bts_members))
print('크기 :', len(bts_members))
'''result
멤버 : ['RM', '슈가', '진', '제이홉', '지민', '뷔', '정국']
타입 : <class 'list'>
크기 : 7
'''

#02
print('리스트멤버 호출')
print(bts_members[0])
print(bts_members[1])
print(bts_members[2])
print(bts_members[3])
'''result
리스트멤버 호출
RM
슈가
진
제이홉
'''

#03
print('리스트멤버 호출(역순)')
print(bts_members[-1])
print(bts_members[-2])
print(bts_members[-3])
print(bts_members[-4])
'''result
리스트멤버 호출(역순)
정국
뷔
지민
제이홉
'''

#04
sistar_members = ['효린', '소유']
print('씨스타 \t:', sistar_members)

sistar_members.append('다솜')
print('append \t:', sistar_members)
sistar_members.insert(1, '보라')
print('insert \t:', sistar_members)

sistar_members.remove('소유')
print('remove \t:', sistar_members)

pickup = sistar_members.pop(0)
print('pop   \t:', sistar_members, end=' ---> ')
print(pickup)
'''result
씨스타 	: ['효린', '소유']
append 	: ['효린', '소유', '다솜']
insert 	: ['효린', '보라', '소유', '다솜']
remove 	: ['효린', '보라', '다솜']
pop   	: ['보라', '다솜'] ---> 효린
'''

#05
rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
print('\n무지개색깔 \t :', rainbow)
result = rainbow[2:5]
print('rainbow[2:5] :', result)
result = rainbow[:3]
print('rainbow[ :3] :', result)
result = rainbow[:]
print('rainbow[ : ] :', result)
result = rainbow[::2]
print('rainbow[::2] :', result)
result = rainbow[-3:]
print('rainbow[-3:] :', result)
result = rainbow[::-1]
print('rainbow[::-1]:', result)
'''result
무지개색깔 	 : ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
rainbow[2:5] : ['노랑', '초록', '파랑']
rainbow[ :3] : ['빨강', '주황', '노랑']
rainbow[ : ] : ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']
rainbow[::2] : ['빨강', '노랑', '파랑', '보라']
rainbow[-3:] : ['파랑', '남색', '보라']
rainbow[::-1]: ['보라', '남색', '파랑', '초록', '노랑', '주황', '빨강']
'''