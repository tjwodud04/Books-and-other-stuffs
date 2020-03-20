from DefinitionOfAll import preprocess, create_contexts_target,convert_one_hot

text = 'You say goobye and I say hello.'

corpus, word_to_id, id_to_word = preprocess(text)

# print(corpus)
# print(id_to_word)

contexts, target = create_contexts_target(corpus, window_size=1)

# print(contexts)
# print(target)

vocab_size = len(word_to_id)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)