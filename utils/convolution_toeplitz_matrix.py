import numpy as np
from scipy.linalg import toeplitz


def conv_toeplitz(signal_1, length_signal_2):
    """Turns signal_1 into a Toeplitz matrix X to so you can compute the
    linear convolution signal * signal_2 as np.dot(X, signal_2).

    Args:
        signal_1 (array): Vector that is turned into a Toeplitz matrix used for
        convolution.
        signal_2 (array): The other member of the convolution operation.

    Returns:
        matrix: signal_1 in Toeplitz matrix form.
    """

    M = len(signal_1)
    num_out = length_signal_2 + M - 1

    rowToe = np.append(signal_1[0], np.zeros((1, num_out - M)))
    colToe = np.append(signal_1, np.zeros((num_out - M, 1)))
    return toeplitz(colToe, rowToe)
