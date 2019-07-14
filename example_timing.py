from utils.timing import lets_time_it, time_pure_numpy

# Comparing the different modes
lets_time_it(which='toeplitz')
lets_time_it(which='scipy_auto')
lets_time_it(which='scipy_direct')
lets_time_it(which='scipy_fft')

# Comparing pure numpy with our implementation
lets_time_it(which='numpy_convolve')
time_pure_numpy()
