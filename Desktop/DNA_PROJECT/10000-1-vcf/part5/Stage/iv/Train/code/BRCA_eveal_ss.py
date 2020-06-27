#coding:utf-8

import tensorflow as tf

import BRCA_inference
import BRCA_batch
import BRCA_data
import BRCA_train

# 数据读取路径
Data_Read_PATH = "/home/sunysh/12Cancer/BRCA/10000-1-vcf/part5/test.Matrix"


def evaluate():
    with tf.Graph().as_default() as g:
        # 测试数据读取
        L = BRCA_data.readCase(Data_Read_PATH)

        # 定义输入输出格式
        x = tf.placeholder(tf.float32, [None, BRCA_inference.INPUT_NODE], name='x-input')
        y_ = tf.placeholder(tf.float32, [None, BRCA_inference.OUTPUT_NODE], name='y_input')

        # 用所有的数据来检测模型
        xc, yc, xn, yn = BRCA_batch.group(L)

        # 计算前向传播结果，测试时不关心正则化损失的值，所以这里设为None
        y = BRCA_inference.inference(x, None)

        # 计算准确率
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        print tf.cast(correct_prediction, tf.float32)
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

        # Create an ExponentialMovingAverage object
        variable_averages = tf.train.ExponentialMovingAverage(BRCA_train.MOVING_AVERAGE_DECAY)
        # 返回变量的名称来保存
        variables_to_restore = variable_averages.variables_to_restore()
        # 存储变量
        saver = tf.train.Saver(variables_to_restore)

        with tf.Session() as sess:
            # 找到目录中最新的文件名
            ckpt = tf.train.get_checkpoint_state(BRCA_train.MODEL_SAVE_PATH)
            if ckpt and ckpt.model_checkpoint_path:
                # 加载模型
                saver.restore(sess, ckpt.model_checkpoint_path)

                for i in range(2):
                    if i == 0:
                        validate_feed = {x: xc, y_: yc}
                        accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                        print("len(yc) cancer accuracy = %g" % accuracy_score)
                    if i == 1:
                        print ('BBB', len(yn))
                        validate_feed = {x: xn, y_: yn}
                        accuracy_score = sess.run(accuracy, feed_dict=validate_feed)
                        print("len(yn) normal accuracy = %g" % accuracy_score)


def main(argv = None):
    evaluate()


if __name__ == '__main__':
    tf.app.run()
