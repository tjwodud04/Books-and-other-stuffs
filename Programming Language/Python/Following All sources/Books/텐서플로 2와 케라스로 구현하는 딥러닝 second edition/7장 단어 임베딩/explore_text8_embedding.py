from gensim.models import KeyedVectors

def print_most_similar(word_conf_pairs, k):
    for i, (word, conf) in enumerate(word_conf_pairs):
        print("{:.3f} {:s}".format(conf, word))
        if i >= k-1:
            break
    if k < len(word_conf_pairs):
        print("...")



model = KeyedVectors.load("data/text8-word2vec.bin")
word_vectors = model.wv

# get words in the vocabulary
words = word_vectors.vocab.keys()
print([x for i, x in enumerate(words) if i < 10])
assert("king" in words)

'''['anarchism', 'originated', 'as', 'a', 'term', 'of', 'abuse', 'first', 'used', 'against']'''


print("# words similar to king")
print_most_similar(word_vectors.most_similar("king"), 5)

'''# words similar to king
0.728 prince
0.717 queen
0.710 emperor
0.708 throne
0.690 kings'''

print("# vector arithmetic with words (cosine similarity)")
print("# france + berlin - paris = ?")
print_most_similar(word_vectors.most_similar(
    positive=["france", "berlin"], negative=["paris"]), 1
)

'''# vector arithmetic with words (cosine similarity)
# france + berlin - paris = ?
0.812 germany'''

print("# vector arithmetic with words (Levy and Goldberg)")
print("# france + berlin - paris = ?")
print_most_similar(word_vectors.most_similar_cosmul(
    positive=["france", "berlin"], negative=["paris"]), 1
)

'''# vector arithmetic with words (Levy and Goldberg)
# france + berlin - paris = ?
0.968 germany'''

print("# find odd one out")
print("# [hindus, parsis, singapore, christians]")
print(word_vectors.doesnt_match(["hindus", "parsis", 
    "singapore", "christians"]))

'''# find odd one out
# [hindus, parsis, singapore, christians]
singapore'''

print("# similarity between words")

for word in ["woman", "dog", "whale", "tree"]:
    print("similarity({:s}, {:s}) = {:.3f}".format(
        "man", word,
        word_vectors.similarity("man", word)
    ))

'''# similarity between words
similarity(man, woman) = 0.739
similarity(man, dog) = 0.445
similarity(man, whale) = 0.277
similarity(man, tree) = 0.262'''

print("# similar by word")
print(print_most_similar(word_vectors.similar_by_word("singapore"), 5))

'''# similar by word
0.873 malaysia
0.844 indonesia
0.818 zambia
0.815 uganda
0.811 thailand'''

print("# distance between vectors")
print("distance(singapore, malaysia) = {:.3f}".format(word_vectors.distance("singapore", "malaysia")))

'''# distance between vectors
distance(singapore, malaysia) = 0.127'''

vec_song = word_vectors["song"]
print("\n# output vector obtained directly, shape:", vec_song.shape)

'''# output vector obtained directly, shape: (100,)'''

vec_song_2 = word_vectors.word_vec("song", use_norm=True)
print("# output vector obtained using word_vec, shape:", vec_song_2.shape)

'''# output vector obtained using word_vec, shape: (100,)'''