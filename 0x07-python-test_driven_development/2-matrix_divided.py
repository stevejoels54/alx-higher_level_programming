#!/usr/bin/python3
"""Function for dividing matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists representing the matrix.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by the given number.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or each row of the matrix does not have the same size,
                   or div is not a number.
        ZeroDivisionError: div is equal to 0.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []
    for row in matrix:
        divided_row = [round(element / div, 2) for element in row]
        divided_matrix.append(divided_row)

    return divided_matrix
