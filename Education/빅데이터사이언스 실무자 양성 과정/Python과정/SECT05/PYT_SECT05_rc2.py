#06
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
print('태양계 :', solarsys)

planet = '지구'
pos = solarsys.index(planet)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
pos = solarsys.index(planet, 5)
print('%s 행성은 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))

solarsys.pop(-1)
print('태양계 :', solarsys)

planet = '화성'
pos = solarsys.index(planet)
solarsys [pos] = 'Mars'
print('태양계 :', solarsys)

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:5]
gas_planets  = solarsys[5: ]

print('암석형 행성: ', end=''); print(rock_planets);
print('가스형 행성: ', end=''); print(gas_planets);

solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print('태양계 :', solarsys)
'''result
태양계 : ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
지구 행성은 태양계에서 3번째에 위치하고 있습니다.
지구 행성은 태양계에서 9번째에 위치하고 있습니다.
태양계 : ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
태양계 : ['태양', '수성', '금성', '지구', 'Mars', '목성', '토성', '천왕성', '해왕성']
암석형 행성: ['수성', '금성', '지구', '화성']
가스형 행성: ['목성', '토성', '천왕성', '해왕성']
태양계 : ['태양', '수성', '금성', '지구', '화성', '소행성', '목성', '토성', '천왕성', '해왕성']
'''

#07
city = [
    ['서울',  '도쿄',  '베이징'],
    ['런던',  '파리',  '로마'  ],
    ['워싱턴','시카고','잭슨빌']
]

print('city      :', city)
print('city[0]   :', city[0])
print('city[1]   :', city[1])
print('city[-1]  :', city[-1])
print('city[0][0]:', city[0][0])
print('city[0][1]:', city[0][1])
print('city[0][2]:', city[0][2])
print('city[1][1]:', city[1][1])
print('city[2][0]:', city[2][0])
'''result
city      : [['서울', '도쿄', '베이징'], ['런던', '파리', '로마'], ['워싱턴', '시카고', '잭슨빌']]
city[0]   : ['서울', '도쿄', '베이징']
city[1]   : ['런던', '파리', '로마']
city[-1]  : ['워싱턴', '시카고', '잭슨빌']
city[0][0]: 서울
city[0][1]: 도쿄
city[0][2]: 베이징
city[1][1]: 파리
city[2][0]: 워싱턴
'''

#08
girl_group = ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')

print('girl_group    \t: ', girl_group)
print('girl_group[:2] \t: ', girl_group[:2])
print('girl_group[-2:] : ', girl_group[-2:])
'''result
girl_group    	:  ('트와이스', '레드벨벳', '에이핑크', '걸스데이', '우주소녀')
girl_group[:2] 	:  ('트와이스', '레드벨벳')
girl_group[-2:] :  ('걸스데이', '우주소녀')
'''
girl_group = list(girl_group)
girl_group[2] = '블랙핑크'
girl_group = tuple(girl_group)
print('girl_group   \t: ', girl_group)
'''result
girl_group   	:  ('트와이스', '레드벨벳', '블랙핑크', '걸스데이', '우주소녀')
'''

#09
width  = 20
height = 30
area = width * height

print('너비 :', width);
print('높이 :', height);
print('넓이 :', area)
'''result
너비 : 20
높이 : 30
넓이 : 600
'''