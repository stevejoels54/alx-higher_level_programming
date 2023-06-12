#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    delete_list = my_list.copy()
    del delete_list[idx]

    return delete_list
