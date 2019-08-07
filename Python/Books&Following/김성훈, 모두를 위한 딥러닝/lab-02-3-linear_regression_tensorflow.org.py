import tensorflow as tf

x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]

W = tf.Variable([0.3], tf.float32)
b = tf.Variable([-0.3], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

hypothesis = x * W + b
cost = tf.reduce_sum(tf.square(hypothesis - y))
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(1000):
        sess.run(train, {x: x_train, y: y_train})
    W_val, b_val, cost_val = sess.run([W, b,cost],
                                            feed_dict={x: x_train, y: y_train})
    print(f"W: {W_val} b: {b_val} cost: {cost_val}")
    '''실행결과 W: [-0.9999969] b: [0.9999908] cost: 5.699973826267524e-11'''