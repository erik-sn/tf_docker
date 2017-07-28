""" learning tensorflow """

import tensorflow as tf

def main():
    """ main script """
    x_1 = tf.constant(5)
    x_2 = tf.constant(6)

    result = tf.multiply(x_1, x_2)
    print(result)


if __name__ == "__main__":
    main()
