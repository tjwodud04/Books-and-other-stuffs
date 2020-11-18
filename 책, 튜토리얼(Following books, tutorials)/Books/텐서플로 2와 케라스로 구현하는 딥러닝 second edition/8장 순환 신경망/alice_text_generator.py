import os
import numpy as np
import re
import shutil
import tensorflow as tf

DATA_DIR = "./data"
CHECKPOINT_DIR = os.path.join(DATA_DIR, "checkpoints")
LOG_DIR = os.path.join(DATA_DIR, "logs")

def clean_logs():
    shutil.rmtree(CHECKPOINT_DIR, ignore_errors=True)
    shutil.rmtree(LOG_DIR, ignore_errors=True)

def download_and_read(urls):
    texts = []

    for i, url in enumerate(urls):
        p = tf.keras.utils.get_file("ex1-{:d}.txt".format(i), url, cache_dir=".")

        text = open(p, "r", encoding='utf-8').read()
        text = text.replace("\ufeff", "")
        text = text.replace('\n', ' ')
        text = re.sub(r'\s+', " ", text)

        texts.extend(text)

    return texts

def split_train_labels(sequence):
    input_seq = sequence[0:-1]
    output_seq = sequence[1:]

    return input_seq, output_seq

class CharGenModel(tf.keras.Model):
    def __init__(self, vocab_size, num_timesteps, embedding_dim, **kwargs):
        super(CharGenModel, self).__init__(**kwargs)
        self.embedding_layer = tf.keras.layers.Embedding(
            vocab_size,
            embedding_dim
        )
        self.rnn_layer = tf.keras.layers.GRU(
            num_timesteps,
            recurrent_initializer="glorot_uniform",
            recurrent_activation="sigmoid",
            stateful=True,
            return_sequences=True
        )
        self.dense_layer = tf.keras.layers.Dense(vocab_size)

    def call(self, x):
        x = self.embedding_layer(x)
        x = self.rnn_layer(x)
        x = self.dense_layer(x)
        return x

def loss(labels, predictions):
    return tf.losses.sparse_categorical_crossentropy(
        labels,
        predictions,
        from_logits=True
    )

def generate_text(model, prefix_string, char2idx, idx2char,
        num_chars_to_generate=1000, temperature=1.0):
    input = [char2idx[s] for s in prefix_string]
    input = tf.expand_dims(input, 0)
    text_generated = []
    model.reset_states()

    for i in range(num_chars_to_generate):
        preds = model(input)
        preds = tf.squeeze(preds, 0) / temperature
        pred_id = tf.random.categorical(preds, num_samples=1)[-1, 0].numpy()

        text_generated.append(idx2char[pred_id])

        input = tf.expand_dims([pred_id], 0)

    return prefix_string + "".join(text_generated)

texts = download_and_read([
    "http://www.gutenberg.org/cache/epub/28885/pg28885.txt",
    "https://www.gutenberg.org/files/12/12-0.txt"
])
clean_logs()

vocab = sorted(set(texts))

print("vocab size: {:d}".format(len(vocab)))
'''
vocab size: 90
'''

char2idx = {c:i for i, c in enumerate(vocab)}
idx2char = {i:c for c, i in char2idx.items()}

texts_as_ints = np.array([char2idx[c] for c in texts])
data = tf.data.Dataset.from_tensor_slices(texts_as_ints)

seq_length = 100
sequences = data.batch(seq_length + 1, drop_remainder=True)
sequences = sequences.map(split_train_labels)

for input_seq, output_seq in sequences.take(1):
    print("input:[{:s}]".format("".join([idx2char[i] for i in input_seq.numpy()])))
    print("output:[{:s}]".format("".join([idx2char[i] for i in output_seq.numpy()])))
'''
input:[Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll This eBook is for the use of ]
output:[roject Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll This eBook is for the use of a]
'''

batch_size = 64
steps_per_epoch = len(texts) // seq_length // batch_size
dataset = sequences.shuffle(10000).batch(batch_size, drop_remainder=True)

print(dataset)
'''
<BatchDataset shapes: ((64, 100), (64, 100)), types: (tf.int32, tf.int32)>
'''

vocab_size = len(vocab)
embedding_dim = 256

model = CharGenModel(vocab_size, seq_length, embedding_dim)
model.build(input_shape=(batch_size, seq_length))
model.summary()
'''
Model: "char_gen_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        multiple                  23040     
_________________________________________________________________
gru (GRU)                    multiple                  107400    
_________________________________________________________________
dense (Dense)                multiple                  9090      
=================================================================
Total params: 139,530
Trainable params: 139,530
Non-trainable params: 0
_________________________________________________________________
'''

for input_batch, label_batch in dataset.take(1):
    pred_batch = model(input_batch)

print(pred_batch.shape)
'''
(64, 100, 90)
'''

assert(pred_batch.shape[0] == batch_size)
assert(pred_batch.shape[1] == seq_length)
assert(pred_batch.shape[2] == vocab_size)

model.compile(optimizer=tf.optimizers.Adam(), loss=loss)

num_epochs = 50

for i in range(num_epochs // 10):
    model.fit(
        dataset.repeat(),
        epochs=10,
        steps_per_epoch=steps_per_epoch
        # callbacks=[checkpoint_callback, tensorboard_callback]
    )
    checkpoint_file = os.path.join(
        CHECKPOINT_DIR, "model_epoch_{:d}".format(i+1))
    model.save_weights(checkpoint_file)

    gen_model = CharGenModel(vocab_size, seq_length, embedding_dim)

    gen_model.load_weights(checkpoint_file)
    gen_model.build(input_shape=(1, seq_length))

    print("after epoch: {:d}".format(i+1)*10)
    print(generate_text(gen_model, "Alice ", char2idx, idx2char))
    print("---")
'''
after epoch: 1after epoch: 1after epoch: 1after epoch: 1after epoch: 1after epoch: 1after epoch: 1after epoch: 1after epoch: 1after epoch: 1
Alice FOUw IlY but pokilly, and wIS said the wriken. "boursel she Kis awer!" “frame. Aphl teel," said siell you me uter,’ ‘Nouldly whay that I’l Vet with sandt of fomfading--’ Dowardent apbout! are was litioull non are. ‘Ald Duphing you the beanten to shery would I Mollm the berall, top have--the Lyoqueetly'd, ‘Y me:/welple_ cown to hat in loice, whill Desphat inst I. ‘You hon’t, at eaverfrodice pithe,’ He cuntorsiers the Kint. To gever the Mose. "Cone? I darker nark the bemorr she Res leage, so steaded an whis mace. "I'the of ed of dirghing to cvuttiless. "Wire yar crothet, but it downalping, and han, the agine prarger, youmned clace unde in hive I athe gottelf, and shough harms fat issed that said thoeseld the oant: any Fozeled shoughtold, you court_ hind asta. ‘and filenberg?’ sam itnodg in!’’ Twa sex, "I now whound the ent'll dove the Woid, hapen. YOU HverY ‘Usith, and wion. "hew wha rowed clattire mele the Morg the bester becon't dlying!" Want oun mimp, the the copming the Knowance athe
---
after epoch: 2after epoch: 2after epoch: 2after epoch: 2after epoch: 2after epoch: 2after epoch: 2after epoch: 2after epoch: 2after epoch: 2
Alice Qyeathing wat about to to lud the showing in ant to should be the live trifundly that of clase in all thisks 21 4? I’ll helped aicest my know." "And if isturing on shen1. get recoring.’-juer “Theme wasow. "Overutice! OIll as __but the thunes eecon’t NE ITH IPTED FIN’_GI IN KIng thing, in't make you reans.’ * * * *4 FO. Conet here in the dream elpure, and wentends, whor pantauc. ‘Its again?’ ‘he mind, should be fforg it the nughtatiful,’ the Queen cree mored. You time was agaid, as so thof I dibnam--I gext up time. "Who'll east, and with the seemepenclacke’t a tailing. ‘The prombor. trarader anch to sepliful fary tooks?" sabed one, ‘hit weng--" Alice cours it intally fierlad: ALE Angs freatertion," Nor off me twook file of the Redlan!’ They was If if her," said, ‘fins on quection----but you mal,’ Alice semely every: "the--the could sen,’ sundly dagrup as a finer is ire with the: Once leggibsing or interftance beed her hnook for to the plaste, bum. ‘Whith got her dees, you tank boment, s
---
after epoch: 3after epoch: 3after epoch: 3after epoch: 3after epoch: 3after epoch: 3after epoch: 3after epoch: 3after epoch: 3after epoch: 3
Alice HAR Efar_ quite dimpliegs Look a morun comforth it wasn't receister? and it will it was momedurinat,’ the King!" "Call anything, repling,’ said ALESc--"pensn’t sigusennisly. Sike to door, to intermacter ideam: ‘Acher a splain). ‘How so she--’ _iadsertmers Catermer,’ Alice one’s DTiind on or ensellers arms, which measer till a livisides!" sees. ‘he wuntitced it-ug head, along seeming in to the KingNo gitting (as some it vinge to herself livily must dotion.) "Iven prore of you had his down whiter. ‘Of look you--to Alice sept it, trunder you ran I found hin often mocked and doesed fare, and the Queen sutting dived do in the cour to help-catting belining see to may,’ thought thinks was a like at out of his, by them very feet got letty picked comded, or theirsed. So said the fortaid out, and know her hear) Son’t much). ‘Canding it upon "Comsered again. Prost 1._.6. It?’ tide, sable you never Queen soale them with this to felurtappound about reng on achest on a shile you feethous hered any a
---
after epoch: 4after epoch: 4after epoch: 4after epoch: 4after epoch: 4after epoch: 4after epoch: 4after epoch: 4after epoch: 4after epoch: 4
Alice King you (agSouse I wood, or keep into-sock.'" Alice I areh to be age, of chith to got hisld tell be: said the Paglestoor a little. ‘Queen old site after of the shorted to the ovemy, Of croent of the work, they alrooks to for only answered it with--now (she only the fing to meach the caition again donees as he starms Alice when you’ll go like or mor, and that--’ He said ‘the Shack tevingain. Then her kevemen was al if upthong up all in the took him happen if I wonder you arg and her mans lige. ‘So she said that,’ she was a seveles.’ Alice said in on, 'I a growle considery to broke the rather pet; but as the one about this was quick and you knowh in the Queen, Dor, she table; "it werine shouted a rebbligerptroning an enoughth tone his or long the edginces subjected out attered to must when she said in a like the ot like a surd," the King say you all it all beacal coppone fear," said Alice. She said a nere.’ Alice didn’tly tell in its off an orcanch her amout Beat about it.’ ‘I sain day 
---
after epoch: 5after epoch: 5after epoch: 5after epoch: 5after epoch: 5after epoch: 5after epoch: 5after epoch: 5after epoch: 5after epoch: 5
Alice For ear worst her something copiand to long. She went on, for shy, it very brittle, and thirst again-soolber Project Gutenberg). Besied empt, but why salk it it down: In on, though per it going our horsenced thain, and found a little tried it in a fing is a ganders, he was his face together-look way in a poor anxiously deophing way dear if you dire.’ ‘IBberash I lised a Lares by than knetHummbout AH dust me knowly got came voice reat whrate the Mock Turry after hturn. So only it one and the remark. Cons_'t a good as sose-exaling hig have had fistring ever you are a-box, I never said. How!’ Bn, to see the Rabbit," said Alice, sea up at rean!” And this learowh, and found in so drapef. Till you, and that dandant. ‘I for a blowes of the then seemed on and far?’ HOW MUsS_ and you. ‘What it is the Queen, and followed the croin two, make, the backs mates of playe; he,’ said Alice, and immasibut," the Moce to choace how the bottled at all.’ By the went some, for the kning and on setsecop, ‘if 
---
'''

'''
Epoch 1/10
54/54 [==============================] - 1s 11ms/step - loss: 3.4714
Epoch 2/10
54/54 [==============================] - 1s 11ms/step - loss: 2.7771
Epoch 3/10
54/54 [==============================] - 1s 11ms/step - loss: 2.4888
Epoch 4/10
54/54 [==============================] - 1s 12ms/step - loss: 2.3406
Epoch 5/10
54/54 [==============================] - 1s 11ms/step - loss: 2.2271
Epoch 6/10
54/54 [==============================] - 1s 12ms/step - loss: 2.1400
Epoch 7/10
54/54 [==============================] - 1s 13ms/step - loss: 2.0617
Epoch 8/10
54/54 [==============================] - 1s 12ms/step - loss: 1.9944
Epoch 9/10
54/54 [==============================] - 1s 11ms/step - loss: 1.9422
Epoch 10/10
54/54 [==============================] - 1s 13ms/step - loss: 1.8939

Epoch 1/10
54/54 [==============================] - 1s 12ms/step - loss: 1.8509
Epoch 2/10
54/54 [==============================] - 1s 11ms/step - loss: 1.8145
Epoch 3/10
54/54 [==============================] - 1s 12ms/step - loss: 1.7787
Epoch 4/10
54/54 [==============================] - 1s 13ms/step - loss: 1.7530
Epoch 5/10
54/54 [==============================] - 1s 13ms/step - loss: 1.7236
Epoch 6/10
54/54 [==============================] - 1s 12ms/step - loss: 1.6965
Epoch 7/10
54/54 [==============================] - 1s 12ms/step - loss: 1.6760
Epoch 8/10
54/54 [==============================] - 1s 12ms/step - loss: 1.6542
Epoch 9/10
54/54 [==============================] - 1s 12ms/step - loss: 1.6366
Epoch 10/10
54/54 [==============================] - 1s 11ms/step - loss: 1.6227

Epoch 1/10
54/54 [==============================] - 1s 13ms/step - loss: 1.6018
Epoch 2/10
54/54 [==============================] - 1s 13ms/step - loss: 1.5888
Epoch 3/10
54/54 [==============================] - 1s 10ms/step - loss: 1.5749
Epoch 4/10
54/54 [==============================] - 1s 13ms/step - loss: 1.5604
Epoch 5/10
54/54 [==============================] - 1s 13ms/step - loss: 1.5492
Epoch 6/10
54/54 [==============================] - 1s 11ms/step - loss: 1.5394
Epoch 7/10
54/54 [==============================] - 1s 13ms/step - loss: 1.5262
Epoch 8/10
54/54 [==============================] - 1s 11ms/step - loss: 1.5205
Epoch 9/10
54/54 [==============================] - 1s 12ms/step - loss: 1.5106
Epoch 10/10
54/54 [==============================] - 1s 12ms/step - loss: 1.5044

Epoch 1/10
54/54 [==============================] - 1s 12ms/step - loss: 1.4939
Epoch 2/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4861
Epoch 3/10
54/54 [==============================] - 1s 12ms/step - loss: 1.4784
Epoch 4/10
54/54 [==============================] - 1s 12ms/step - loss: 1.4727
Epoch 5/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4649
Epoch 6/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4604
Epoch 7/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4530
Epoch 8/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4506
Epoch 9/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4371
Epoch 10/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4391

Epoch 1/10
54/54 [==============================] - 1s 13ms/step - loss: 1.4328
Epoch 2/10
54/54 [==============================] - 1s 13ms/step - loss: 1.4302
Epoch 3/10
54/54 [==============================] - 1s 13ms/step - loss: 1.4225
Epoch 4/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4183
Epoch 5/10
54/54 [==============================] - 1s 12ms/step - loss: 1.4157
Epoch 6/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4140
Epoch 7/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4032
Epoch 8/10
54/54 [==============================] - 1s 11ms/step - loss: 1.4036
Epoch 9/10
54/54 [==============================] - 1s 12ms/step - loss: 1.3999
Epoch 10/10
54/54 [==============================] - 1s 13ms/step - loss: 1.3972
'''