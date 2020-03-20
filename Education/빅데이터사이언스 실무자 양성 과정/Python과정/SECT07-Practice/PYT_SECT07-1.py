#01
dan = input('출력할 단을 입력해주세요.[2~9] ')
dan = int(dan)
gop = 0

print(dan, '단 출 력 \n' + '-'*20)
for i in range(9):
    num = i + 1
    gop = dan * num
    print(dan, '*', num, '=', gop)

idx, gop, hap = 0, 0, 0
factorial = []
total_hap = []

num_chk_list = list('0123456789')

while True:
    key_in = input('숫자를 입력해 주세요.[1~100] => ')
    chk_num = True
    for char in key_in:
        is_num = char in num_chk_list
        chk_num *= is_num
        if not is_num:
            break
    if chk_num:
        last_num = int(key_in)
        print('입력한 숫자:', last_num)
        break
    else:
        print('입력한 값이 숫자가 아닙니다.')

title = str(last_num) + ' 까지의 합계 및 팩토리얼 테이블 구하기!!'
print('-'*50)
print(title)
print('-'*50)

numbers = list(range(last_num+1))

while idx < len(numbers):
    num = numbers[idx]
    hap += num
    gop *= num
    gop = 1 if gop < 1 else gop
    total_hap.append(hap)
    factorial.append(gop)
    idx += 1

print(last_num, '까지의 합계는', total_hap[-1], '입니다.')
print('아래는 팩토리얼 테이블입니다.')
for fact_num in range(len(factorial)):
    print(str(fact_num)+'!\t= ', factorial[fact_num])

#03
s = input('영어 대소문자로 이루어진 문장을 입력하세요.\n')  # 문자열 입력

print('모두 대문자로 출력\n' + s.upper())
print('모두 소문자로 출력\n' + s.lower())
new_s = str()
for c in s:
    if c.islower():
        new_s += c.upper()
    else:
        new_s += c.lower()
print('대소문자 바꿔서 출력\n' + new_s)
print('대소문자 바꿔서 출력\n' + s.swapcase())

#04
s = input('영어 문장을 입력하세요.\n')
new_s = str()
for x in range(len(s)-1, -1, -1):
    new_s += s[x]
print(new_s)
print(s[::-1])

#05
books = list()
many_page     = [ book['제목']  for book in books  if book['쪽수'] > 250 ]
recommends    = [ book['제목']  for book in books  if book['추천유무']  ]
pub_companies = { book['출판사'] for book in books }
all_pages     = sum([book['쪽수'] for book in books])

print(' ### 도서 목록 출력 내용 ### \n', '-'*90)
print(' 1. 쪽수가 250 쪽 넘는 책 리스트 :', many_page)
print(' 2. 내가 추천하는 책 리스트      :', recommends)
print(' 3. 내가 읽은 책 전체 쪽수       :', all_pages)
print(' 4. 내가 읽은 책의 출판사 목록   :', sorted(pub_companies) )