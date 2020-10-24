import numpy as np
import os
import shutil
import tensorflow as tf

from sklearn.metrics import accuracy_score, confusion_matrix

def clean_logs(data_dir):
    logs_dir = os.path.join(data_dir, "logs")
    shutil.rmtree(logs_dir, ignore_errors=True)
    return logs_dir

def download_and_read(url):
    local_file = url.split('/')[-1]
    local_file = local_file.replace("%20", " ")
    p = tf.keras.utils.get_file(local_file, url, 
        extract=True, cache_dir=".")
    local_folder = os.path.join("datasets", local_file.split('.')[0])
    labeled_sentences = []

    for labeled_filename in os.listdir(local_folder):
        if labeled_filename.endswith("_labelled.txt"):
            with open(os.path.join(local_folder, labeled_filename), "r") as f:
                for line in f:
                    sentence, label = line.strip().split('\t')
                    labeled_sentences.append((sentence, label))

    return labeled_sentences

class SentimentAnalysisModel(tf.keras.Model):
    def __init__(self, vocab_size, max_seqlen, **kwargs):
        super(SentimentAnalysisModel, self).__init__(**kwargs)
        self.embedding = tf.keras.layers.Embedding(vocab_size, max_seqlen)
        self.bilstm = tf.keras.layers.Bidirectional(
            tf.keras.layers.LSTM(max_seqlen)
        )
        self.dense = tf.keras.layers.Dense(64, activation="relu")
        self.out = tf.keras.layers.Dense(1, activation="sigmoid")

    def call(self, x):
        x = self.embedding(x)
        x = self.bilstm(x)
        x = self.dense(x)
        x = self.out(x)
        return x

tf.random.set_seed(42)

data_dir = "./data"
logs_dir = clean_logs(data_dir)

labeled_sentences = download_and_read(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/00331/sentiment%20labelled%20sentences.zip")
sentences = [s for (s, l) in labeled_sentences]
labels = [int(l) for (s, l) in labeled_sentences]

tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(sentences)
vocab_size = len(tokenizer.word_counts)

print("vocabulary size: {:d}".format(vocab_size))
'''
vocabulary size: 5271
'''

word2idx = tokenizer.word_index
idx2word = {v:k for (k, v) in word2idx.items()}

# seq_lengths = np.array([len(s.split()) for s in sentences])
# print([(p, np.percentile(seq_lengths, p)) for p 
max_seqlen = 64

sentences_as_ints = tokenizer.texts_to_sequences(sentences)
sentences_as_ints = tf.keras.preprocessing.sequence.pad_sequences(
    sentences_as_ints, maxlen=max_seqlen)
labels_as_ints = np.array(labels)
dataset = tf.data.Dataset.from_tensor_slices(
    (sentences_as_ints, labels_as_ints))

dataset = dataset.shuffle(10000)
test_size = len(sentences) // 3
val_size = (len(sentences) - test_size) // 10
test_dataset = dataset.take(test_size)
val_dataset = dataset.skip(test_size).take(val_size)
train_dataset = dataset.skip(test_size + val_size)

batch_size = 64
train_dataset = train_dataset.batch(batch_size)
val_dataset = val_dataset.batch(batch_size)
test_dataset = test_dataset.batch(batch_size)

model = SentimentAnalysisModel(vocab_size+1, max_seqlen)
model.build(input_shape=(batch_size, max_seqlen))
model.summary()
'''
Model: "sentiment_analysis_model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        multiple                  337408    
_________________________________________________________________
bidirectional (Bidirectional multiple                  66048     
_________________________________________________________________
dense (Dense)                multiple                  8256      
_________________________________________________________________
dense_1 (Dense)              multiple                  65        
=================================================================
Total params: 411,777
Trainable params: 411,777
Non-trainable params: 0
_________________________________________________________________
'''

model.compile(
    loss="binary_crossentropy",
    optimizer="adam", 
    metrics=["accuracy"]
)

best_model_file = os.path.join(data_dir, "best_model.h5")
checkpoint = tf.keras.callbacks.ModelCheckpoint(best_model_file,
    save_weights_only=True,
    save_best_only=True)
tensorboard = tf.keras.callbacks.TensorBoard(log_dir=logs_dir)
num_epochs = 10
history = model.fit(train_dataset, epochs=num_epochs, 
    validation_data=val_dataset,
    callbacks=[checkpoint, tensorboard])

best_model = SentimentAnalysisModel(vocab_size+1, max_seqlen)
best_model.build(input_shape=(batch_size, max_seqlen))
best_model.load_weights(best_model_file)
best_model.compile(
    loss="binary_crossentropy",
    optimizer="adam", 
    metrics=["accuracy"]
)

test_loss, test_acc = best_model.evaluate(test_dataset)

print("test loss: {:.3f}, test accuracy: {:.3f}".format(test_loss, test_acc))
'''
test loss: 0.039, test accuracy: 0.991
'''

labels, predictions = [], []
idx2word[0] = "PAD"
is_first_batch = True

for test_batch in test_dataset:
    inputs_b, labels_b = test_batch
    pred_batch = best_model.predict(inputs_b)
    predictions.extend([(1 if p > 0.5 else 0) for p in pred_batch])
    labels.extend([l for l in labels_b])

    if is_first_batch:
        for rid in range(inputs_b.shape[0]):
            words = [idx2word[idx] for idx in inputs_b[rid].numpy()]
            words = [w for w in words if w != "PAD"]
            sentence = " ".join(words)

            print("{:d}\t{:d}\t{:s}".format(labels[rid], predictions[rid], sentence))

        is_first_batch = False
'''
0	0	this is a chilly unremarkable movie about an author living working in a chilly abstruse culture
0	0	i don't recommend unless your car breaks down in front of it and you are starving
1	1	it's a gloriously fun fast paced and fairly accurate portrayal of the night of a raver
0	0	bad characters bad story and bad acting
1	1	i enjoyed reading this book to my children when they were little
0	0	once your food arrives it's meh
1	1	the vanilla ice cream was creamy and smooth while the profiterole choux pastry was fresh enough
1	1	the mic is great
1	1	we thought you'd have to venture further away to get good sushi but this place really hit the spot that night
1	1	tom wilkinson broke my heart at the end and everyone else's judging by the amount of fumbling for hankies and hands going up to faces among males and females alike
1	1	mark my words this is one of those cult films like evil dead 2 or phantasm that people will still be discovering and falling in love with 20 30 40 years down the line
1	1	the film's dialogue is natural real to life
0	0	you get what you pay for i guess
0	0	this place is not worth your time let alone vegas
1	1	very very fun chef
0	0	the place was fairly clean but the food simply wasn't worth it
1	1	this film highlights the fundamental flaws of the legal process that it's not about discovering guilt or innocence but rather is about who presents better in court
1	1	but it wasn't until i watched this film that i realised how great he actually was
1	1	phone is sturdy as all nokia bar phones are
0	0	kind of flops around
1	1	all of the tapas dishes were delicious
0	0	i have been to very few places to eat that under no circumstances would i ever return to and this tops the list
0	0	your servers suck wait correction our server heimer sucked
1	1	will be back again
1	1	delicious
1	1	worked perfectly
0	0	i probably won't be coming back here
1	1	think of the film being like a dream
1	1	loved it friendly servers great food wonderful and imaginative menu
1	1	that just screams legit in my book somethat's also pretty rare here in vegas
0	0	this results in the phone being either stuck at max volume or mute
0	0	what a waste
1	1	they were excellent
1	1	does everything it should and more
1	1	however paul schrader has indeed made a film about mishima that is both superb complex
1	1	call me a nut but i think this is one of the best movies ever
1	1	the food was very good
0	0	after all the rave reviews i couldn't wait to eat here what a disappointment
1	1	good service very clean and inexpensive to boot
0	0	friend's pasta also bad he barely touched it
0	0	i'm still trying to get over how bad it was
1	1	our server was fantastic and when he found out the wife loves roasted garlic and bone marrow he added extra to our meal and another marrow to go
1	1	our waiter was very attentive friendly and informative
1	1	their steaks are 100 recommended
0	0	the desserts were a bit strange
1	1	i've only had my bluetooth for a few weeks but i really like it
0	0	the death row scenes were entirely unmoving
1	1	the bartender was also nice
1	1	each track commands sentiment actually contributing to the scenes and characters
1	1	as always the evening was wonderful and the food delicious
0	0	i'm not sure what he was trying to do with this film
0	0	there is no real plot
1	1	excellent dual purpose headset
1	1	my colleague i now get great reception a little expensive but performance is great
1	1	the range is very decent i've been able to roam around my house with the phone in the living room with no reception sound quality issues
1	1	this is the number one best th game in the series
0	0	this is by far the worst purchase i've made on amazon
0	0	i checked everywhere and there is no feature for it which is really disappointing
1	0	the soundtrack wasn't terrible either
0	0	shrimp when i unwrapped it i live only 1 2 a mile from brushfire it was literally ice cold
1	1	plus it's only 8 bucks
1	1	i had ordered a motorola data cable got a very well finished and working product
0	0	there was nothing believable about it at all
0	0	the fish is badly made and some of its underwater shots are repeated a thousand times in the film
'''

print("accuracy score: {:.3f}".format(accuracy_score(labels, predictions)))
print("confusion matrix")
print(confusion_matrix(labels, predictions))
'''
accuracy score: 0.991
confusion matrix
[[486   3]
 [  6 505]]
'''
'''
Epoch 1/10
29/29 [==============================] - 1s 31ms/step - loss: 0.6930 - accuracy: 0.5339 - val_loss: 0.6861 - val_accuracy: 0.7200
Epoch 2/10
29/29 [==============================] - 0s 10ms/step - loss: 0.6434 - accuracy: 0.7406 - val_loss: 0.4777 - val_accuracy: 0.8500
Epoch 3/10
29/29 [==============================] - 0s 10ms/step - loss: 0.4065 - accuracy: 0.8372 - val_loss: 0.2722 - val_accuracy: 0.8950
Epoch 4/10
29/29 [==============================] - 0s 9ms/step - loss: 0.2319 - accuracy: 0.9200 - val_loss: 0.1763 - val_accuracy: 0.9350
Epoch 5/10
29/29 [==============================] - 0s 9ms/step - loss: 0.1623 - accuracy: 0.9417 - val_loss: 0.1426 - val_accuracy: 0.9550
Epoch 6/10
29/29 [==============================] - 0s 9ms/step - loss: 0.1422 - accuracy: 0.9550 - val_loss: 0.1354 - val_accuracy: 0.9550
Epoch 7/10
29/29 [==============================] - 0s 9ms/step - loss: 0.0951 - accuracy: 0.9689 - val_loss: 0.0560 - val_accuracy: 0.9850
Epoch 8/10
29/29 [==============================] - 0s 9ms/step - loss: 0.0704 - accuracy: 0.9811 - val_loss: 0.0633 - val_accuracy: 0.9900
Epoch 9/10
29/29 [==============================] - 0s 9ms/step - loss: 0.0520 - accuracy: 0.9861 - val_loss: 0.0266 - val_accuracy: 0.9900
Epoch 10/10
29/29 [==============================] - 0s 9ms/step - loss: 0.0387 - accuracy: 0.9894 - val_loss: 0.0435 - val_accuracy: 0.9950
'''