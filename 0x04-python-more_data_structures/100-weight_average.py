#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_products = 0
    last_sum = 0

    for tple in my_list:
        sum_products += (tple[0] * tple[1])
        last_sum += tple[1]

    return sum_products / last_sum
