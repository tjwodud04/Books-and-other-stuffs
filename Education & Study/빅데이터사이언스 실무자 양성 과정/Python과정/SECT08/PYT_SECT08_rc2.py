#08
def introduceMyCar(brand, seats=4, type='세단'):
    print('나의 차는 {b} {s}인승 {t}이다'.format(
        b = brand,
        s = seats,
        t = type
    ))
introduceMyCar('아우디')
introduceMyCar(brand='렉서스')
introduceMyCar('제규어', seats=2)
introduceMyCar(brand='머큐리', type='머슬카')
introduceMyCar(type='미니벤', brand='카니발')
introduceMyCar('카니발', 9, '미니벤')
introduceMyCar('쉐보레', type='SUV ', seats=7)
'''result
나의 차는 아우디 4인승 세단이다
나의 차는 렉서스 4인승 세단이다
나의 차는 제규어 2인승 세단이다
나의 차는 머큐리 4인승 머슬카이다
나의 차는 카니발 4인승 미니벤이다
나의 차는 카니발 9인승 미니벤이다
나의 차는 쉐보레 7인승 SUV 이다
'''

#09
def introduceMyFamily(my_name, *family_names, **family_info):
    print('안녕하세요, 저는 %s 입니다.' % (my_name))
    print('-' * 35)
    print('제 가족들의 이름은 아래와 같아요. ')

    for name in family_names:
        print('* %s ' % (name), end='\t')
    else:
        print()
    print('-' * 35)

    for key in family_info.keys():
        print('- %s : %s ' % (key, family_info[key]))

introduceMyFamily('진수', '희영', '찬영', '준영', '채영',
                  주소='롯데캐슬', 가훈='극기상진', 소망='세계일주')

'''result
안녕하세요, 저는 진수 입니다.
-----------------------------------
제 가족들의 이름은 아래와 같아요. 
* 희영 	* 찬영 	* 준영 	* 채영 	
-----------------------------------
- 주소 : 롯데캐슬 
- 가훈 : 극기상진 
- 소망 : 세계일주 
'''

#10
def add(a, b):
    return a + b

data = (10, 20)
print(add(*data))
'''result
30
'''
def introduce(name, greeting):
    return "{name}님, {greeting}".format(
        name=name,
        greeting=greeting,
    )

introduce_dict = {
    "name" : "김진수",
    "greeting" : "안녕하세요",
}
print(introduce(**introduce_dict))
'''result
김진수님, 안녕하세요
'''

#11
param   = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print('func1.strdata = %s, id = %d' % (strdata, id(strdata)))

def func2(param):
    param = 20
    print('func2.param = %d, id = %d' % (param, id(param)))

def func3():
    global param
    param = 30
    print('func3.param = %d, id = %d' % (param, id(param)))

func1()
print('main1.strdata = %s, id = %d' % (strdata, id(strdata)))
func2(param)
print('main2.param = %d, id = %d' % (param, id(param)))
func3()
print('main3.param = %d, id = %d' % (param, id(param)))
'''result
func1.strdata = 지역변수, id = 2249228591776
main1.strdata = 전역변수, id = 2249228591880
func2.param = 20, id = 140719810983344
main2.param = 10, id = 140719810983024
func3.param = 30, id = 140719810983664
main3.param = 30, id = 140719810983664
'''

#12
def my_function():
    """ 아무것도 하지 않지만, 문서만 기술한 함수

    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.
    """
    pass

print(my_function.__doc__)

# 문서화를 위한 문자열 활용
def introduce_your_family(name, *family_names, **family_info):
    '''
    가족을 소개하는 함수입니다.
    Args:
        name: 자기이름 입력하기
        *family_names: 가족이름 입력하기
        **family_info: 가족소개하기

    Returns: 없습니다.
    '''
    pass