import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("input", one_hot=True)
from inference import inference
from loss import loss
from evaluation import accuracy_batch
from training import train
from save import save_model

if __name__ == "__main__":
    with tf.name_scope("inputs"):
        xs = tf.placeholder(tf.float32, [None, 784], name="x_input")
        ys = tf.placeholder(tf.float32, [None, 10], name="y_input")
        keep_prob = tf.placeholder(tf.float32, name="dropout")
    x_image = tf.reshape(xs, [-1, 28, 28, 1], name="image_input")  # 最后一个参数是色深channel
    prediction, logits = inference(x_image)
    predict_op = tf.argmax(prediction, 1, name="predict_op")
    cross_entropy = loss(prediction, ys)
    # accuracy(prediction, mnist)
    train_step = train(cross_entropy)

    train_prediction = tf.nn.softmax(prediction)  # accuracy

    sess = tf.Session()
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("logs/", sess.graph)
    sess.run(tf.initialize_all_variables())

    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5})
        if i % 50 == 0:
            loss_value, accuracy_value = sess.run(
                [cross_entropy, train_prediction],
                feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5},
            )
            result = sess.run(
                merged, feed_dict={xs: batch_xs, ys: batch_ys, keep_prob: 0.5}
            )
            writer.add_summary(result, i)
            acc_v = accuracy_batch(accuracy_value, batch_ys)
            print("Loss", loss_value)
            print("Accuracy", acc_v)

    save_model("export", x_image, predict_op, sess)

