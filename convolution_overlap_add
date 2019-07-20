import numpy as np
from scipy import signal

from utils.chunks_func import chunks
from utils.convolution_toeplitz_matrix import conv_toeplitz


def conv_overlap_add(signal_1, signal_2, mode='numpy_convolve'):
    """Executes the convolution between signal_1 and signal_2 by dividing the
    larger signal into blocks with the same length as the smaller one.

    For now: length(bigger signal) mod length(smaller signal) must be == 0
    (the bigger signal length must be exactly divisible by the length of the
    smaller signal)

    Args:
        signal_1 (array) and signal_2 (array): arrays used on the linear convolution.
        mode (string):
            toeplitz: computes the linear convolution using a toeplitz
            matrix

            numpy_convolve: computes the linear convolution using
            numpy.convolve

            scipy_auto: computes the linear convolution using
            scipy.signal.convolve using method='auto'

            scipy_direct: computes the linear convolution using
            scipy.signal.convolve using method='direct'

            scipy_fft: computes the linear convolution using
            scipy.signal.convolve using method='fft'


    Returns:
        array: convolution (signal_1 * signal_2), where * indicates the linear
        convolution operator.
    """
    # TODO: option to divide the bigger signal into a block with N elements

    # signal_1 is always the biggest vector
    if (len(signal_2) > len(signal_1)):
        signal_1, signal_2 = signal_2, signal_1

    bigger_len = len(signal_1)
    block_len = len(signal_2)
    result_len = bigger_len + block_len - 1

    num_block = bigger_len / block_len

    x_sliced = list(chunks(signal_1, block_len))

    slices_convd = []
    for i in range(int(num_block)):
        if mode == 'toeplitz':
            conv_matrix = conv_toeplitz(x_sliced[i], block_len)
            conv_result = np.dot(conv_matrix, signal_2)

        elif mode == 'numpy_convolve':
            conv_result = np.convolve(x_sliced[i], signal_2)

        elif mode == 'scipy_auto':
            conv_result = signal.convolve(x_sliced[i], signal_2, method='auto')

        elif mode == 'scipy_direct':
            conv_result = signal.convolve(x_sliced[i], signal_2, method='direct')

        elif mode == 'scipy_fft':
            conv_result = signal.convolve(x_sliced[i], signal_2, method='fft')

        conv_result_with_zeros = np.append(conv_result, np.zeros(bigger_len))
        slices_convd += [conv_result_with_zeros]

    slices_convd_concd = np.hstack(slices_convd)
    list_blocks_all = list(chunks(slices_convd_concd, result_len))
    summable_part = list_blocks_all[:(int(np.floor(len(slices_convd_concd) / result_len)))]

    return np.sum(summable_part, axis=0)
