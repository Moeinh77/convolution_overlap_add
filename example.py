import numpy as np

from convolution_overlap_add import conv_overlap_add

signal_2 = [1, 2.2, 3, 4, 5, 7]
signal_1 = [1, 2, 0]

# Calling my function
resp = conv_overlap_add(signal_1, signal_2, mode='numpy_convolve')
print(resp)

# Sanity check
resp_numpy = np.convolve(signal_1, signal_2)
print(resp_numpy)

# Comparing results
print(np.all(resp == resp_numpy))
