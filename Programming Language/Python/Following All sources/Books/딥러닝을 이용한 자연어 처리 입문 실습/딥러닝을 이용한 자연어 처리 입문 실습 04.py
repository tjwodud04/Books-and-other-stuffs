'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
4-2)Bag of Words(BoW)
'''

from konlpy.tag import Okt
import re

okt = Okt()

token = re.sub("(\.)","","정부가 발표하는 물가상승률과 소비자가 \
느끼는 물가상승률은 다르다.")

token2 = re.sub("(\.)","","발표가 정부하는 소비자과 물가상승률가 \
느끼는 물가상승률은 다르다.")

token3 = re.sub("(\.)","","소비자는 주로 소비하는 상품을 기준으로 물가상승률을 느낀다.")

token4 = re.sub("(\.)","","정부가 발표하는 물가상승률과 소비자가 느끼는 물가상승률은 다르다. \
소비자는 주로 소비하는 상품을 기준으로 물가상승률을 느낀다.")

token = okt.morphs(token)  #문서1
token2 = okt.morphs(token2)#문서1 (token 순서 바꾸기)
token3 = okt.morphs(token3)#문서2
token4 = okt.morphs(token4)#문서3

word2index = {}
bow = []
for voca in token:
    if voca not in word2index.keys():
        word2index[voca] = len(word2index)
        bow.insert(len(word2index),1)
    else:
        index = word2index.get(voca)
        bow[index] = bow[index]+1

print(word2index)
print(bow, "\n")

word2index2 = {}
bow2 = []
for voca2 in token2:
    if voca2 not in word2index2.keys():
        word2index2[voca2] = len(word2index2)
        bow2.insert(len(word2index2),1)
    else:
        index2 = word2index2.get(voca2)
        bow2[index2] = bow2[index2]+1

print(word2index2)
print(bow2, "\n")

word2index3 = {}
bow3 = []
for voca3 in token3:
    if voca3 not in word2index3.keys():
        word2index3[voca3] = len(word2index3)
        bow3.insert(len(word2index3),1)
    else:
        index3 = word2index3.get(voca3)
        bow3[index3] = bow3[index3]+1

print(word2index3)
print(bow3, "\n")

word2index4 = {}
bow4 = []
for voca4 in token4:
    if voca4 not in word2index4.keys():
        word2index4[voca4] = len(word2index4)
        bow4.insert(len(word2index4),1)
    else:
        index4 = word2index4.get(voca4)
        bow4[index4] = bow4[index4]+1

print(word2index4)
print(bow4)