import numpy as np

from utils.chunks_func import chunks
from utils.convolution_toeplitz_matrix import conv_toeplitz


def conv_overlap_add(signal_1, signal_2):
    """Executes the convolution between signal_1 and signal_2 by dividing the
    larger signal into blocks with the same length as the smaller one.

    Args:
        signal_1 (array) and signal_2 (array): arrays used on the linear convolution.

    Returns:
        array: convolution (signal_1 * signal_2), where * indicates the linear
        convolution operator.
    """
    # TODO: implement convolution options(FFT, Toeplitz, np.convolve, etc)
    # TODO: option to divide the bigger signal into a block with N elements

    # x is always the bigger vector
    if len(signal_1) > len(signal_2):
        x = signal_1
        h = signal_2
    else:
        x = signal_2
        h = signal_1

    tam_x = len(x)
    tam_bloco = len(h)
    tam_result = tam_x + tam_bloco - 1

    qtd_bloco = tam_x / tam_bloco

    lista_blocos = list(chunks(x, tam_bloco))

    conv_blocos = []
    for i in range(int(qtd_bloco)):
        conv_matrix = conv_toeplitz(lista_blocos[i], len(h))
        conv_result = np.dot(conv_matrix, h)
        conv_result_with_zeros = np.append(conv_result, np.zeros(tam_x))
        conv_blocos += [conv_result_with_zeros]

    all_conv_blocks = np.hstack(conv_blocos)
    lista_blocks_all = list(chunks(all_conv_blocks, tam_result))
    lista_blocks_only_usable = lista_blocks_all[:(int(np.floor(len(all_conv_blocks) / tam_result)))]
    res = np.sum(lista_blocks_only_usable, axis=0)

    return res
