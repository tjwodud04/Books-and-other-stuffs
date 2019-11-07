from __future__ import print_function
import tensorflow as tf

hello = tf.constant('안녕, 텐서플로!')
sess = tf.Session()

print(sess.run(hello).decode('UTF-8'))