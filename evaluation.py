import tensorflow as tf
import numpy
def accuracy(logits, mnist):
    with tf.name_scope("accuracy"):
        correct_prediction = tf.equal(
            tf.argmax(logits, -1), tf.argmax(mnist.test.labels, -1)
        )
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar("accuracy", accuracy)

def accuracy_batch(predictions, batch_y):
    print(predictions.shape, batch_y.shape)
    return (100.0 * numpy.sum(numpy.argmax(predictions, 1) == numpy.argmax(batch_y, 1)) / predictions.shape[0])