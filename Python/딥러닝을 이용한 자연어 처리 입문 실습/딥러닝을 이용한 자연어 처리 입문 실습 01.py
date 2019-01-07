'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
1)토큰화
'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from konlpy.tag import Okt
from konlpy.tag import Kkma

kkma = Kkma()
okt = Okt()

text1 = "Time is an illusion. Lunchtime double so!"

text2 = "Don't be fooled by the dark sounding name, \
Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

text3 = "Starting a home-based restaurant may be an ideal. \
it doesn't have a food chain or restaurant of their own."

text4 = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. \
Finally, the barber went up a mountain and almost to the edge of a cliff. \
He dug a hole in the midst of some reeds. He looked about, to mae sure no one was near."

text5 = "I am actively looking for Ph.D. students. and you are a Ph.D. student."

text6 = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"
# print(sent_tokenize(text4))
# TokenizeSentence1 = nltk.word_tokenize(text1)
#
# print(TokenizeSentence1)
# print(word_tokenize(text2)) #영문에서 단어별 tokenize하기
# print(WordPunctTokenizer().tokenize(text2)) #영문에서 어퍼스트로피 s의 구분 가능하게 만들어 줌
#
# tokenizer = TreebankWordTokenizer()
#
# print(tokenizer.tokenize(text3))
# print(sent_tokenize(text4))
#
# print(word_tokenize(text5))
#
# x = word_tokenize(text5)
# print(pos_tag(x))
#
# print(okt.morphs(text6))
# print(okt.nouns(text6))

print(kkma.morphs(text6))
print(kkma.pos(text6))