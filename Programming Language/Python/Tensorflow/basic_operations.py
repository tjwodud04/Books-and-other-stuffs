'''
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

from __future__ import print_function
import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print("a=2, b=3")
    print("상수의 합: %i" % sess.run(a+b))
    print("상수의 곱: %i" % sess.run(a*b))
    print()
''' result
a=2, b=3
상수의 합: 5
상수의 곱: 6
'''

a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

add = tf.add(a, b)
mul = tf.multiply(a, b)

with tf.Session() as sess:
    print("변수의 합: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print("변수의 곱: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))
    print()
'''result
변수의 합: 5
변수의 곱: 6
'''

matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])
product = tf.matmul(matrix1, matrix2)

with tf.Session() as sess:
    result = sess.run(product)
    print(result)
'''result
[[12.]]
'''