from ctypes import CDLL, Structure, c_int, c_float


class Complex(Structure):
    _fields_ = (('real', c_float), ('imag', c_float))


get_iterations = CDLL('mandelbrot.so').get_iterations
get_iterations.argtypes = [Complex, c_int, c_int]
get_iterations.restype = c_int


if __name__ == '__main__':
    print(get_iterations(Complex(1, 0), 1_000, int(1e17)))