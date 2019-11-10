'''
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)

Xtr, Ytr = mnist.train.next_batch(5000)
Xte, Yte = mnist.test.next_batch(200)

xtr = tf.placeholder("float", [None, 784])
xte = tf.placeholder("float", [784])

distance = tf.reduce_sum(tf.abs(tf.add(xtr, tf.negative(xte))), reduction_indices=1)
pred = tf.arg_min(distance, 0)
accuracy = 0.
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)

    for i in range(len(Xte)):
        nn_index = sess.run(pred, feed_dict={xtr: Xtr, xte: Xte[i, :]})
        print("Test", i, "Prediction:", np.argmax(Ytr[nn_index]), "True Class:", np.argmax(Yte[i]))

        if np.argmax(Ytr[nn_index]) == np.argmax(Yte[i]):
            accuracy += 1./len(Xte)

    print("Accuracy:", accuracy)

'''result
Test 0 Prediction: 2 True Class: 2 Test 1 Prediction: 0 True Class: 0
Test 2 Prediction: 4 True Class: 4 Test 3 Prediction: 4 True Class: 4
Test 4 Prediction: 9 True Class: 9 Test 5 Prediction: 5 True Class: 8
Test 6 Prediction: 8 True Class: 8 Test 7 Prediction: 1 True Class: 1
Test 8 Prediction: 3 True Class: 3 Test 9 Prediction: 0 True Class: 0
Test 10 Prediction: 8 True Class: 8 Test 11 Prediction: 5 True Class: 5
Test 12 Prediction: 7 True Class: 7 Test 13 Prediction: 8 True Class: 8
Test 14 Prediction: 8 True Class: 8 Test 15 Prediction: 9 True Class: 9
Test 16 Prediction: 4 True Class: 4 Test 17 Prediction: 5 True Class: 5
Test 18 Prediction: 8 True Class: 8 Test 19 Prediction: 8 True Class: 8
Test 20 Prediction: 3 True Class: 3 Test 21 Prediction: 9 True Class: 9
Test 22 Prediction: 3 True Class: 3 Test 23 Prediction: 4 True Class: 4
Test 24 Prediction: 0 True Class: 0 Test 25 Prediction: 6 True Class: 6
Test 26 Prediction: 3 True Class: 3 Test 27 Prediction: 3 True Class: 3
Test 28 Prediction: 6 True Class: 6 Test 29 Prediction: 6 True Class: 6
Test 30 Prediction: 6 True Class: 6 Test 31 Prediction: 5 True Class: 5
Test 32 Prediction: 5 True Class: 5 Test 33 Prediction: 6 True Class: 6
Test 34 Prediction: 9 True Class: 9 Test 35 Prediction: 2 True Class: 2
Test 36 Prediction: 3 True Class: 3 Test 37 Prediction: 4 True Class: 4
Test 38 Prediction: 2 True Class: 2 Test 39 Prediction: 0 True Class: 0
Test 40 Prediction: 3 True Class: 3 Test 41 Prediction: 1 True Class: 1
Test 42 Prediction: 8 True Class: 8 Test 43 Prediction: 5 True Class: 5
Test 44 Prediction: 2 True Class: 2 Test 45 Prediction: 0 True Class: 0
Test 46 Prediction: 6 True Class: 6 Test 47 Prediction: 4 True Class: 4
Test 48 Prediction: 2 True Class: 2 Test 49 Prediction: 9 True Class: 9
Test 50 Prediction: 7 True Class: 7 Test 51 Prediction: 5 True Class: 5
Test 52 Prediction: 2 True Class: 2 Test 53 Prediction: 7 True Class: 7
Test 54 Prediction: 8 True Class: 8 Test 55 Prediction: 8 True Class: 8
Test 56 Prediction: 3 True Class: 3 Test 57 Prediction: 4 True Class: 4
Test 58 Prediction: 1 True Class: 1 Test 59 Prediction: 6 True Class: 6
Test 60 Prediction: 1 True Class: 1 Test 61 Prediction: 1 True Class: 1
Test 62 Prediction: 0 True Class: 0 Test 63 Prediction: 9 True Class: 9
Test 64 Prediction: 2 True Class: 2 Test 65 Prediction: 2 True Class: 2
Test 66 Prediction: 5 True Class: 8 Test 67 Prediction: 3 True Class: 3
Test 68 Prediction: 6 True Class: 6 Test 69 Prediction: 3 True Class: 3
Test 70 Prediction: 0 True Class: 0 Test 71 Prediction: 8 True Class: 8
Test 72 Prediction: 6 True Class: 6 Test 73 Prediction: 0 True Class: 0
Test 74 Prediction: 6 True Class: 5 Test 75 Prediction: 3 True Class: 3
Test 76 Prediction: 1 True Class: 1 Test 77 Prediction: 6 True Class: 6
Test 78 Prediction: 9 True Class: 9 Test 79 Prediction: 1 True Class: 1
Test 80 Prediction: 9 True Class: 9 Test 81 Prediction: 0 True Class: 0
Test 82 Prediction: 1 True Class: 1 Test 83 Prediction: 8 True Class: 8
Test 84 Prediction: 5 True Class: 5 Test 85 Prediction: 1 True Class: 1
Test 86 Prediction: 7 True Class: 7 Test 87 Prediction: 8 True Class: 8
Test 88 Prediction: 6 True Class: 6 Test 89 Prediction: 3 True Class: 5
Test 90 Prediction: 1 True Class: 1 Test 91 Prediction: 0 True Class: 0
Test 92 Prediction: 8 True Class: 8 Test 93 Prediction: 9 True Class: 9
Test 94 Prediction: 1 True Class: 1 Test 95 Prediction: 2 True Class: 2
Test 96 Prediction: 0 True Class: 0 Test 97 Prediction: 0 True Class: 8
Test 98 Prediction: 0 True Class: 0 Test 99 Prediction: 9 True Class: 9
Test 100 Prediction: 4 True Class: 4 Test 101 Prediction: 0 True Class: 0
Test 102 Prediction: 1 True Class: 1 Test 103 Prediction: 9 True Class: 9
Test 104 Prediction: 2 True Class: 2 Test 105 Prediction: 9 True Class: 9
Test 106 Prediction: 7 True Class: 7 Test 107 Prediction: 6 True Class: 6
Test 108 Prediction: 9 True Class: 9 Test 109 Prediction: 0 True Class: 0
Test 110 Prediction: 7 True Class: 7 Test 111 Prediction: 3 True Class: 3
Test 112 Prediction: 4 True Class: 4 Test 113 Prediction: 4 True Class: 9
Test 114 Prediction: 7 True Class: 7 Test 115 Prediction: 1 True Class: 1
Test 116 Prediction: 2 True Class: 2 Test 117 Prediction: 1 True Class: 1
Test 118 Prediction: 9 True Class: 9 Test 119 Prediction: 5 True Class: 5
Test 120 Prediction: 9 True Class: 9 Test 121 Prediction: 6 True Class: 6
Test 122 Prediction: 2 True Class: 2 Test 123 Prediction: 0 True Class: 0
Test 124 Prediction: 6 True Class: 6 Test 125 Prediction: 8 True Class: 8
Test 126 Prediction: 9 True Class: 9 Test 127 Prediction: 8 True Class: 8
Test 128 Prediction: 0 True Class: 9 Test 129 Prediction: 6 True Class: 6
Test 130 Prediction: 6 True Class: 6 Test 131 Prediction: 2 True Class: 2
Test 132 Prediction: 0 True Class: 0 Test 133 Prediction: 5 True Class: 5
Test 134 Prediction: 1 True Class: 1 Test 135 Prediction: 3 True Class: 3
Test 136 Prediction: 0 True Class: 0 Test 137 Prediction: 9 True Class: 9
Test 138 Prediction: 5 True Class: 5 Test 139 Prediction: 0 True Class: 0
Test 140 Prediction: 6 True Class: 6 Test 141 Prediction: 4 True Class: 4
Test 142 Prediction: 7 True Class: 7 Test 143 Prediction: 2 True Class: 2
Test 144 Prediction: 7 True Class: 7 Test 145 Prediction: 1 True Class: 1
Test 146 Prediction: 3 True Class: 3 Test 147 Prediction: 7 True Class: 7
Test 148 Prediction: 4 True Class: 4 Test 149 Prediction: 8 True Class: 8
Test 150 Prediction: 3 True Class: 3 Test 151 Prediction: 1 True Class: 1
Test 152 Prediction: 6 True Class: 2 Test 153 Prediction: 3 True Class: 3
Test 154 Prediction: 1 True Class: 1 Test 155 Prediction: 9 True Class: 9
Test 156 Prediction: 2 True Class: 2 Test 157 Prediction: 4 True Class: 4
Test 158 Prediction: 9 True Class: 9 Test 159 Prediction: 2 True Class: 2
Test 160 Prediction: 9 True Class: 9 Test 161 Prediction: 1 True Class: 1
Test 162 Prediction: 8 True Class: 8 Test 163 Prediction: 0 True Class: 0
Test 164 Prediction: 0 True Class: 0 Test 165 Prediction: 4 True Class: 4
Test 166 Prediction: 1 True Class: 1 Test 167 Prediction: 5 True Class: 8
Test 168 Prediction: 9 True Class: 9 Test 169 Prediction: 3 True Class: 3
Test 170 Prediction: 9 True Class: 9 Test 171 Prediction: 6 True Class: 6
Test 172 Prediction: 5 True Class: 5 Test 173 Prediction: 3 True Class: 3
Test 174 Prediction: 9 True Class: 9 Test 175 Prediction: 4 True Class: 4
Test 176 Prediction: 2 True Class: 2 Test 177 Prediction: 6 True Class: 6
Test 178 Prediction: 4 True Class: 4 Test 179 Prediction: 9 True Class: 9
Test 180 Prediction: 0 True Class: 0 Test 181 Prediction: 2 True Class: 2
Test 182 Prediction: 5 True Class: 5 Test 183 Prediction: 7 True Class: 7
Test 184 Prediction: 3 True Class: 3 Test 185 Prediction: 0 True Class: 0
Test 186 Prediction: 0 True Class: 8 Test 187 Prediction: 4 True Class: 4
Test 188 Prediction: 8 True Class: 8 Test 189 Prediction: 8 True Class: 8
Test 190 Prediction: 2 True Class: 2 Test 191 Prediction: 6 True Class: 6
Test 192 Prediction: 3 True Class: 3 Test 193 Prediction: 3 True Class: 3
Test 194 Prediction: 8 True Class: 8 Test 195 Prediction: 0 True Class: 0
Test 196 Prediction: 3 True Class: 3 Test 197 Prediction: 7 True Class: 7
Test 198 Prediction: 6 True Class: 6 Test 199 Prediction: 8 True Class: 8
Accuracy: 0.9500000000000007
'''