# Convolution using Overlap-Add

Implements convolution using overlap-add (OA) method for efficient way to evaluate the discrete convolution of a very long signal. Just for fun. Probably numpy already does that.

[This link explains the overlap-add method.](https://en.wikipedia.org/wiki/Overlap%E2%80%93add_method)

This code is inefficient when compared to pure numpy.convolve ([see this example](example_timing.py)). However, I belive someday we can defeat them.
