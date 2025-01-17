def use_hex():
    a = 123
    print(bin(a))
    print(hex(a))
    print(oct(a))

    b = -5

    print(bin(b))


def use_float():
    f = 1.234567891234567891
    print(f)


def use_bool():
    print(True + 1)
    print(False + 1)


def use_complex():
    c = complex(3, 4)
    print("c is %d+%dj" % (c.real, c.imag))


# use_hex()
# use_float()
# use_bool()
use_complex()
