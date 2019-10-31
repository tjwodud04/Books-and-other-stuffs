import tensorflow as tf
tf.set_random_seed(777)

x_data = [[1, 2],
          [2, 3],
          [3, 1],
          [4, 3],
          [5, 3],
          [6, 2]]
y_data = [[0],
          [0],
          [0],
          [1],
          [1],
          [1]]

X = tf.placeholder(tf.float32, shape=[None, 2])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([2, 1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1 -hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        cost_val, _ = sess.run([cost, train], feed_dict= {X: x_data, Y: y_data})
        if step % 200 == 0:
            print(step, cost_val)

    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X: x_data, Y: y_data})
    print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)

'''result
0 1.8553263
200 0.8420143
400 0.77422076
600 0.72896576
800 0.69408923
1000 0.66457146
1200 0.63815105
1400 0.6137374
1600 0.59077877
1800 0.5689866
2000 0.54820484
2200 0.52834624
2400 0.50935894
2600 0.49120882
2800 0.47386906
3000 0.4573163
3200 0.44152716
3400 0.42647743
3600 0.4121414
3800 0.39849246
4000 0.3855029
4200 0.37314424
4400 0.36138752
4600 0.35020426
4800 0.33956575
5000 0.32944423
5200 0.31981245
5400 0.310644
5600 0.3019136
5800 0.29359698
6000 0.28567094
6200 0.27811348
6400 0.27090392
6600 0.26402238
6800 0.25745028
7000 0.2511701
7200 0.24516511
7400 0.23942006
7600 0.23392022
7800 0.22865187
8000 0.22360219
8200 0.21875925
8400 0.21411164
8600 0.20964883
8800 0.205361
9000 0.20123859
9200 0.19727308
9400 0.19345622
9600 0.18978035
9800 0.1862383
10000 0.18282332

Hypothesis:  [[0.04589509]
 [0.17536531]
 [0.3707354 ]
 [0.7526998 ]
 [0.9200944 ]
 [0.9738756 ]] 
Correct (Y):  [[0.]
 [0.]
 [0.]
 [1.]
 [1.]
 [1.]] 
Accuracy:  1.0
'''