#!/usr/bin/python3
def pow(a, b):
    product = 1
    if b >= 0:
        for num in range(b):
            product = product * a
    else:
        return 1 / pow(a, abs(b))
    return product
