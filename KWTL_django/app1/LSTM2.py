import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os
import argparse

normalize_data = []

time_step = 30
mean = 0
std = 0
rnn_unit = 10
batch_size = 10
input_size = 1
output_size = 1
lr = 0.0006
train_x, train_y = [], []

X = tf.placeholder(tf.float32, [None, time_step, input_size])
Y = tf.placeholder(tf.float32, [None, time_step, output_size])
#
weights = {
    'in': tf.Variable(tf.random_normal([input_size, rnn_unit])),
    'out': tf.Variable(tf.random_normal([rnn_unit, 1]))
}
biases = {
    'in': tf.Variable(tf.constant(0.1, shape=[rnn_unit, ])),
    'out': tf.Variable(tf.constant(0.1, shape=[1, ]))
}

def lstm(batch):  #
    #tf.keras.backend.clear_session()
    w_in = weights['in']
    b_in = biases['in']
    input = tf.reshape(X, [-1, input_size])  #
    input_rnn = tf.matmul(input, w_in) + b_in
    input_rnn = tf.reshape(input_rnn, [-1, time_step, rnn_unit])  #
    cell = tf.nn.rnn_cell.LSTMCell(rnn_unit)
    init_state = cell.zero_state(batch, dtype=tf.float32)
    with tf.variable_scope('scope', reuse=tf.AUTO_REUSE):
        output_rnn, final_states = tf.nn.dynamic_rnn(cell, input_rnn, initial_state=init_state, dtype=tf.float32)
    output = tf.reshape(output_rnn, [-1, rnn_unit])  #
    w_out = weights['out']
    b_out = biases['out']
    pred = tf.matmul(output, w_out) + b_out
    return pred, final_states


def train_lstm(epoch):
    global batch_size
    pred, _ = lstm(batch_size)
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1]) - tf.reshape(Y, [-1])))
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)
    saver = tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(int(epoch)):
            step = 0
            start = 0
            end = start + batch_size
            while (end < len(train_x)):
                _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[start:end], Y: train_y[start:end]})
                start += batch_size
                end = start + batch_size
                if step % 50 == 0:
                    print(i, step, loss_)
                    saver.save(sess, os.getcwd() + '\\app1\\data\\module\\stock1.model', global_step=i)
                    #print("保存模型：", saver.save(sess, os.getcwd() + '\\app1\\data\\module\\stock1.model', global_step=i))
                step += 1


def prediction(num):
    pred, _ = lstm(1)  #
    saver = tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        module_file = tf.train.latest_checkpoint(os.getcwd() + '\\app1\\data\\module')
        saver.restore(sess, module_file)
        prev_seq = train_x[-1]
        predict = []
        for i in range(int(num)):  #
            next_seq = sess.run(pred, feed_dict={X: [prev_seq]})
            predict.append(next_seq[-1].tolist()[0]*std + mean)
            prev_seq = np.vstack((prev_seq[1:], next_seq[-1]))
        return predict
        #plt.figure()
        #plt.plot(list(range(len(normalize_data))), normalize_data, color='b')
        #plt.plot(list(range(len(normalize_data), len(normalize_data) + len(predict))), predict, color='r')
        #plt.show()
def train_prediction(num):
    global batch_size
    pred, _ = lstm(batch_size)
    loss = tf.reduce_mean(tf.square(tf.reshape(pred, [-1]) - tf.reshape(Y, [-1])))
    train_op = tf.train.AdamOptimizer(lr).minimize(loss)
    #saver = tf.train.Saver(tf.global_variables())
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(100):
            step = 0
            start = 0
            end = start + batch_size
            while (end < len(train_x)):
                _, loss_ = sess.run([train_op, loss], feed_dict={X: train_x[start:end], Y: train_y[start:end]})
                start += batch_size
                end = start + batch_size
                if step % 50 == 0:
                    print(i, step, loss_)
                    #saver.save(sess, os.getcwd() + '\\app1\\data\\module\\stock1.model', global_step=i)
                    # print("保存模型：", saver.save(sess, os.getcwd() + '\\app1\\data\\module\\stock1.model', global_step=i))
                step += 1

        prev_seq = train_x[-1]
        predict = []
        for i in range(int(num)):  #
            next_seq = sess.run(pred, feed_dict={X: [prev_seq]})
            predict.append(next_seq[-1].tolist()[0] * std + mean)
            prev_seq = np.vstack((prev_seq[1:], next_seq[-1]))
        return predict

def setdata(data):
    #tf.keras.backend.clear_session()
    data = data.split(',', data.count(','))
    data = [float(i) for i in data]
    global mean,std
    mean= np.mean(data)
    std = np.std(data)
    normalize_data = (data - np.mean(data)) / np.std(data)
    normalize_data = normalize_data[:, np.newaxis]
    for i in range(len(normalize_data) - time_step - 1):
        x = normalize_data[i:i + time_step]
        y = normalize_data[i + 1:i + time_step + 1]
        train_x.append(x.tolist())
        train_y.append(y.tolist())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', default='65.08,65.08,65.08,65.08,68.59,63.45,63.45,61.9,61.9,65.08,66.79,66.79,66.79,66.79,68.59,70.5,68.59,70.5,70.5,70.5,68.59,68.59,68.59,65.08,61.9,61.9,61.9,65.08,68.59,70.5,68.59,66.79,65.08,66.79,66.79,66.79,68.59,65.08,65.08,65.08,65.08,66.79,70.5,68.59,68.59,68.59,68.59,70.5,70.5,70.5,70.5,68.59,65.08,66.79,66.79,66.79,68.59,68.59,66.79,68.59,66.79,66.79,68.59,66.79,68.59')
    parser.add_argument('-n', '--predNum', default='10')
    parser.add_argument('-e', '--epoch', default='50')
    args = parser.parse_args()
    print(args.data)
    print(args.predNum)
    setdata(args.data)
    train_lstm(args.epoch)
    print("output:")
    print(prediction(args.predNum))  # requ


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        os._exit(1)