#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def add_tuple(tuple_a=(), tuple_b=()):
        a = tuple_a + (0, 0)
        b = tuple_b + (0, 0)
        first_sum = a[:2][0] + b[:2][0]
        second_sum = a[:2][1] + b[:2][1]
        return (first_sum, second_sum)
