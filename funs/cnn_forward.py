import numpy as np


def cnn_forward(layer_in, conv_filter, pad, stride=1):
    w, h, ci = layer_in.shape
    k, k, _, co = conv_filter.shape

    # np.pad(array, pad_width, mode, **kwargs)
    # 在array边缘填充数值，个数为pad_width，数值为constant_values
    # A = np.pad(A, ((1, 2), (2, 1)), 'constant', constant_values=((1, 2), (3, 4)))
    padded_layer = np.pad(layer_in, ((pad,), (pad,), (0,)), 'constant', constant_values=(0,))
    w_out = 1 + (w+2*pad-k)//stride
    h_out = 1 + (h+2*pad-k)//stride
    out = np.zeros((w_out, h_out, co))
    # 对每个输出空间位置(i,j)和每个深度列k
    for i in range(w_out):
        for j in range(h_out):
            layer_in_mask = padded_layer[i*stride:i*stride+k, j*stride:j*stride+k, :]
            for k in range(co):
                out[i, j, k] = np.sum(layer_in_mask*conv_filter[:, :, :, k])
    return out

