'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
4-2)Bag of Words(BoW) 4-3)단어 문서 행렬(Term-Document Matrix)
'''

from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

corpus = ['you know I want your love, because I love you.']
vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray())
print(vector.vocabulary_, "\n")

text1 = ["Family is not an important thing. It's everything."]
vect1 = CountVectorizer(stop_words="english")
print(vect1.fit_transform(text1).toarray())
print(vect1.vocabulary_, "\n")

sw = stopwords.words("english")
vect1 = CountVectorizer(stop_words =sw)
print(vect1.fit_transform(text1).toarray())
print(vect1.vocabulary_)

#----------------------------------------------------------------

