from datetime import timedelta
from time import time

import numpy as np

from convolution_overlap_add import conv_overlap_add


def time_measure(f):
    def timed(*args, **kw):
        t0 = time()
        result = f(*args, **kw)
        diff = int(time() - t0)
        diff = timedelta(seconds=diff)
        diff_str = str(diff).split(':')
        return {'return': result, 'time_processing': diff_str}

    return timed


def lets_time_it(which='toeplitz'):
    @time_measure
    def timing_func():
        number_loop = int(10e3)
        for i in range(number_loop):
            signal_1 = np.random.ranf(size=500)
            signal_2 = np.random.ranf(size=5)
            conv_overlap_add(signal_1, signal_2, mode=which)

        return number_loop

    timing_result = timing_func()
    number_loop = int(timing_result['return'])
    time_elapsed = timing_result['time_processing']
    time_elapsed = [float(x) for x in time_elapsed]

    total_time = time_elapsed[0] * 60 * 60 + time_elapsed[1] * 60 + time_elapsed[0]
    time_per_iteration = total_time / number_loop

    print(f"{which} -- Time elapsed: { time_elapsed[1]} minutes, { time_elapsed[2]} seconds")
    print(f'{which} -- Time per loop: {time_per_iteration}')


def time_pure_numpy():
    @time_measure
    def timing_func():
        number_loop = int(10e3)
        for i in range(number_loop):
            signal_1 = np.random.ranf(size=500)
            signal_2 = np.random.ranf(size=5)
            np.convolve(signal_1, signal_2)

        return number_loop

    timing_result = timing_func()
    number_loop = int(timing_result['return'])
    time_elapsed = timing_result['time_processing']
    time_elapsed = [float(x) for x in time_elapsed]

    total_time = time_elapsed[0] * 60 * 60 + time_elapsed[1] * 60 + time_elapsed[0]
    time_per_iteration = total_time / number_loop

    print(f"pure numpy -- Time elapsed: { time_elapsed[1]} minutes, { time_elapsed[2]} seconds")
    print(f'pure numpy -- Time per loop: {time_per_iteration}')
