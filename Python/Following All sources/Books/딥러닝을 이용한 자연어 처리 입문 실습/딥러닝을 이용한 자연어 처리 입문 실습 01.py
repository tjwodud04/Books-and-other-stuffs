'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
1)토큰화 2)정제 3)어간 추출 and 표제어 추출
'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from konlpy.tag import Okt
from konlpy.tag import Kkma
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

P = PorterStemmer()
n = WordNetLemmatizer()
kkma = Kkma()
okt = Okt()
L = LancasterStemmer()

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

wordslist1 = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

text7 = "This was not the map we found in Billy Bones's chest, but an accurate copy, \
complete in all things--names and heights and soundings--with the single \ exception of the red crosses and the written notes."

wordslist2 = ['formalize', 'allowance', 'electricical']

wordslist3 = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']

print(sent_tokenize(text4))
TokenizeSentence1 = nltk.word_tokenize(text1)

print(TokenizeSentence1)
print(word_tokenize(text2)) #영문에서 단어별 tokenize하기
print(WordPunctTokenizer().tokenize(text2)) #영문에서 어퍼스트로피 s의 구분 가능하게 만들어 줌

tokenizer = TreebankWordTokenizer()

print(tokenizer.tokenize(text3))
print(sent_tokenize(text4))

print(word_tokenize(text5))

x = word_tokenize(text5)
print(pos_tag(x))

print(okt.morphs(text6))
print(okt.nouns(text6))

print(kkma.morphs(text6))
print(kkma.pos(text6))
print([n.lemmatize(wl) for wl in wordslist1]) #제대로 출력되지 않는 'dy'나 'ha' 등이 있음
print(n.lemmatize('dies', 'v'))
print(n.lemmatize('watched', 'v'))
print(n.lemmatize('has', 'v'))

stemmizedwords = word_tokenize(text7)
print(stemmizedwords)
print([P.stem(sw) for sw in stemmizedwords])
print([P.stem(wl2) for wl2 in wordslist2])

print([P.stem(wl3) for wl3 in wordslist3])
print([L.stem(wl3) for wl3 in wordslist3])