import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')

x1 = tf.constant([5])
x2 = tf.constant([6])

result = tf.multiply(x1,x2)

with tf.Session() as sess:
    output = sess.run(result)
    print(output)

