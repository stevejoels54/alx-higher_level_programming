#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    quotient_list = []
    if list_length <= 0:
        print("out of range")
        return quotient_list
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (TypeError, ValueError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            quotient_list.append(result)
    return quotient_list
