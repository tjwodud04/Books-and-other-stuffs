from DefinitionOfAll import preprocess, create_contexts_target,convert_one_hot, SimpleCBOW, Adam,Trainer

window_size = 1
hidden_size = 1
batch_size = 3
max_epoch = 1000

text = 'You say goobye and I say hello.'
corpus, word_to_id, id_to_word = preprocess(text)

vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
target = convert_one_hot(target, vocab_size)
contexts = convert_one_hot(contexts, vocab_size)

model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)

trainer.fit(contexts, target, max_epoch, batch_size)
#trainer.plot()

word_vecs = model.word_vecs
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])
'''
결과
you [1.579111]
say [-1.8447834]
goobye [1.6030273]
and [-1.6977293]
i [1.5945892]
hello [1.5903753]
. [-1.4129597]
'''

