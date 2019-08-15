import tensorflow as tf
from keras.layers import DepthwiseConv2D


def split_channels(total_filters, num_groups):
    split = [total_filters // num_groups for _ in range(num_groups)]
    split[0] += total_filters - sum(split)
    return split


def mixconv(inputs, kernel_sizes, strides, padding):
    convs = []
    for kernel_size in kernel_sizes:
        convs.append(DepthwiseConv2D(kernel_size, strides=strides, padding=padding))

    if len(convs) == 1:
        return convs[0](inputs)
    filters = inputs.shape[-1].value
    splits = split_channels(filters, len(convs))
    x_splits = tf.split(inputs, splits, -1)
    x_outputs = [c(x) for x, c in zip(x_splits, convs)]
    x = tf.concat(x_outputs, -1)
    return x


# example = ['r1_k3.5.7.9.11_a1_p1_s22_e6_i120_o200_se0.5_sw',
#            'r2_k3.5.7.9_a1_p1.1_s11_e6_i200_o200_se0.5_sw',]
# kernel_sizes = [3, 5, 7, 9]
# strides = [1, 1]
# depthwise_initializer = conv_kernel_initializer
# padding = 'same'
# data_format = self._data_format
# use_bias = False
# dilated = self._block_args.dilated

