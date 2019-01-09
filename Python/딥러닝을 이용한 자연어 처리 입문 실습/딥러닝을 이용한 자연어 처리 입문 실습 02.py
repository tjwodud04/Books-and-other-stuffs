'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
4)불용어(한글 부분 추가 예정) 5)정규 표현식 6)단어 분리
'''

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

example1 = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english'))

example2 = "고기를 아무렇게나 구우려고 하면 안 돼. \
고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"
word_tokens1 = word_tokenize(example1)
word_tokens2 = word_tokenize(example2)
result1 = []
result2 = []

for word in word_tokens1:
    if word not in stop_words:
        result1.append(word)

for words in word_tokens2:
    if word not in stop_words:
        result2.append(word)

print(stopwords.words('english')[:10])
print(word_tokens1)
print(result1)
print(word_tokens2)
print(result2)

#----------------------
# r1 = re.compile("a.c")
# print(r1.search("kkk"))
# print(r1.search("abc"))
# print(r1.search("a!c"))
# print(r1.search("a#c"))
#
# r2 = re.compile("ab?c")
# print(r2.search("abbc"))
# print(r2.search("abc"))
# print(r2.search("ac"))
#
# r3 = re.compile("ab*c")
# print(r3.search("ac"))
# print(r3.search("abc"))
# print(r3.search("abbbbc"))
# print(r3.search("abtkc"))
#
# r4 = re.compile("ab+c")
# print(r3.search("abc"))
# print(r3.search("abbbbbc"))
# print(r3.search("abtkc"))
# print(r3.search("atkc"))
#
# r5 = re.compile("^a")
# print(r5.search("bbc"))
# print(r5.search("ab"))
#
# r6 = re.compile("ab{2}c")
# print(r6.search("ac"))
# print(r6.search("abc"))
# print(r6.search("abbc"))
# print(r6.search("abbbbbbbc"))
#
# r7 = re.compile("ab{2,8}c")
# print(r7.search("ac"))
# print(r7.search("abc"))
# print(r7.search("abbc"))
# print(r7.search("abbbbbbbc"))
# print(r7.search("abbbbbbbsdfc"))
# print(r7.search("abbbbbbbbbbbc"))
#
# r8 = re.compile("a{2,}bc")
# print(r8.search("bc"))
# print(r8.search("aa"))
# print(r8.search("aabc"))
# print(r8.search("aaaaaaaaaabc"))
# print(r8.search("abbbbbbbsdfc"))

r8 = re.compile("[abc]kdf")
print(r8.search('zzz'))
print(r8.search('akdf'))
print(r8.search("baac"))
print(r8.search("bkdf"))

r9 = re.compile("[a-z]")
print(r9.search('AAA'))
print(r9.search('aBC'))
print(r9.search('111'))