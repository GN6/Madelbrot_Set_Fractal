typedef struct Complex Complex;

struct Complex {
    float real;
    float imag;
};

float abs2(Complex x) {
    float real2 = x.real * x.real;
    float imag2 = x.imag * x.imag;
    return real2 + imag2;
}

Complex add_complex(Complex s1, Complex s2) {
    float real = s1.real + s2.real;
    float imag = s1.imag + s2.imag;
    return (Complex) {real, imag};
}

Complex mul_complex(Complex s1, Complex s2) {
    float real = s1.real * s2.real - s1.imag * s2.imag;
    float imag = s1.real * s2.imag + s1.imag * s2.real;
    return (Complex) {real, imag};
}


int get_iterations(Complex c, int max_iters, int fidelity) {
    Complex z = {0, 0};
    for (int n = 0; 1; n++) {
        z = mul_complex(z, z);
        z = add_complex(z, c);
        if (n == max_iters || abs2(z) > fidelity * fidelity)
            return n;
    }
}
