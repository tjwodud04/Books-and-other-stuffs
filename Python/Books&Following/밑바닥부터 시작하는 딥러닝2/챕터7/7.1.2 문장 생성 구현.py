from dataset import ptb
from DefinitionOfAll.RnnlmGen import RnnlmGen

corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
corpus_size = len(corpus)

model = RnnlmGen()
model.load_params(r'Rnnlm.pkl')

start_word = 'you'
start_id = word_to_id[start_word]
skip_words = ['N', '<unk>', '$']
skip_ids = [word_to_id[w] for w in skip_words]

word_ids = model.generate(start_id, skip_ids)
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')
print(txt)

'''실행결과
you was determined.
 in edition of the international meanwhile the milton river has said it will still think about two.
 the cypress plan developed year results are almost effective as conflicts aimed subsidiaries and defense suits.
 nor bracing for turning off companies to do a richer directs between the highway or industrial average.
 robert j. judge george dorfman said the project had paid universities dr. phelan said that doing a new chancellor of its new philippines instead of dismissed building to work for mr. ingersoll 's.
 but mr. trudeau was a real post of them'''