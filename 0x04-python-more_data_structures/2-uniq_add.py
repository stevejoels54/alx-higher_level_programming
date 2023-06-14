#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    unique_nums = set(my_list)
    for unique_num in unique_nums:
        sum += unique_num
    return sum
