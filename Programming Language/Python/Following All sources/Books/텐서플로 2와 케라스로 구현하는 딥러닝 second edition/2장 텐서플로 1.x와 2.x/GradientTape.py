import tensorflow as tf

x = tf.constant(4.0)

with tf.GradientTape(persistent=True) as g:
  g.watch(x)
  y = x * x
  z = y * y

dz_dx = g.gradient(z, x)
dy_dx = g.gradient(y, x)

print (dz_dx)
print (dy_dx)
del g

'''
tf.Tensor(256.0, shape=(), dtype=float32)
tf.Tensor(8.0, shape=(), dtype=float32)
'''