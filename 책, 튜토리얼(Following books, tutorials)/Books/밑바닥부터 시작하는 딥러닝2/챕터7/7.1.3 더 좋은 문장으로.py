from DefinitionOfAll.BetterRnnlmGen import BetterRnnlmGen
from dataset import ptb
import numpy as np

corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
corpus_size = len(corpus)

model = BetterRnnlmGen()
model.load_params(r'BetterRnnlm.pkl')

start_word = 'you'
start_id = word_to_id[start_word]
skip_words = ['N', '<unk>', '$']
skip_ids = [word_to_id[w] for w in skip_words]

word_ids = model.generate(start_id, skip_ids)
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')

print(txt)
'''실행결과 
you do n't start it.
 yesterday.
 as may the company 's ability to use the pack continued by the troubled guild who will have to be sold to home-equity loans calculate the time to earth all that they can spend rates for the future to pay for each neighborhood on american express.
 the real estate investment trust affiliated in their goal has contributed to the woes of the management business and office of england.
 after a line of takeover overhaul of the company its interests of the corporation 's rockefeller group stores represented some of its
'''
model.reset_state()

start_words = 'the meaning of life is'
start_ids = [word_to_id[w] for w in start_words.split(' ')]

for x in start_ids[:-1]:
    x = np.array(x).reshape(1, 1)
    model.predict(x)

word_ids = model.generate(start_ids[-1], skip_ids)
word_ids = start_ids[:-1] + word_ids
txt = ' '.join([id_to_word[i] for i in word_ids])
txt = txt.replace(' <eos>', '.\n')
print('-' * 50)
print(txt)
'''실행결과
the meaning of life is n't what the issue is too interesting.
 some general accounting experts say it will be running more assistance to better than standardized television in asia.
 in the busiest new report shopping service 's first mural got out to that new york times no charge.
 mr. bryant said the pregnant & agreement is designed to block mr. connolly 's idea.
 he himself said that fox would end for its spouses have solar cleanup to the realty network of the sorrell who were incorporated in a separate interview against mr. sorrell.
 asked the researchers of the'''