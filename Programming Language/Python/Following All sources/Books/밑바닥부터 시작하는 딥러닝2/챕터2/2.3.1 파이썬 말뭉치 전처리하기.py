import numpy as np

text = 'You say goobye and I say hello.'

text.lower()
text = text.replace('.',' .')
print(text)

words = text.split(' ')
print(words)

word_to_id = {}
id_to_word = {}

for word in words:
    if word not in word_to_id:
        new_id = len(word_to_id)
        word_to_id[word] = new_id
        id_to_word[new_id] = word

print(id_to_word)
print(word_to_id)
print(id_to_word[1])
print(word_to_id['hello'])

corpus = [word_to_id[w] for w in words]
corpus = np.array(corpus)
print(corpus)
#-----------------------------------------------#

def preprocess(text):
    text.lower()
    text = text.replace('.', ' .')
    words = text.split(' ')
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word

corpus, word_to_id, id_to_word = preprocess(text)