'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer

Sentence1 = "Time is an illusion. Lunchtime double so!"
Sentence2 = "Don't be fooled by the dark sounding name, \
Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."

TokenizeSentence1 = nltk.word_tokenize(Sentence1)
#TokenizeSentence2 = nltk.word_tokenize(Sentence2)
print(TokenizeSentence1)
#print(TokenizeSentence2)
print(word_tokenize(Sentence2)) #영문에서 단어별 tokenize하기
print(WordPunctTokenizer().tokenize(Sentence2)) #영문에서 어퍼스트로피 s의 구분 가능하게 만들어 줌

tokenizer = TreebankWordTokenizer()
Sentence3 = "Starting a home-based restaurant may be an ideal. \
it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(Sentence3))