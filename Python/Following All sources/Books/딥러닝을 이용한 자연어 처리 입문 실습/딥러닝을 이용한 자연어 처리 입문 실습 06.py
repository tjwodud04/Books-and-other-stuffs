'''
Reference book :
https://wikidocs.net/21698
딥러닝을 이용한 자연어 처리 입문
5-1) 코사인 유사도
'''

from numpy import dot
from numpy.linalg import norm
import numpy as np

def cos_sim(A, B):
    return dot(A, B)/(norm(A)*norm(B))

doc1 = np.array([0,1,1,1])
doc2 = np.array([1,0,1,1])
doc3 = np.array([2,0,2,2])

print(cos_sim(doc1, doc2))
print(cos_sim(doc1, doc3))
print(cos_sim(doc2, doc3 ), "\n")
#------------------------------------------------

import pandas as pd
data = pd.read_csv(r'C:\Users\J\Desktop\movies_metadata.csv', low_memory=False)
print(data.head(5), "\n")

data.head(20000)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#tf-idf : 어떤 단어가 특정 문서 내에서 얼마나 중요한 것인지를 나타내는 통계적 수치
tfidf = TfidfVectorizer(stop_words='english')
data['overview'] = data['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(data['overview'])
print(tfidf_matrix.shape, "\n")

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(data.index, index=data['title']).drop_duplicates()
print(indices.head(5), "\n")

idx = indices['Father of the Bride Part II']
print(idx, "\n")

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return data['title'].iloc[movie_indices]

print(get_recommendations('The Dark Knight Rises'))