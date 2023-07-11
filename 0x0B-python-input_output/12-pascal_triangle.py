#!/usr/bin/python3
"""Pascal's Triangle generating function"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """

    if n <= 0:
        return []

    pascal_tri = [[1]]

    for x in range(1, n):
        row = [1]
        prev_row = pascal_tri[x - 1]

        for y in range(1, x):
            row.append(prev_row[y - 1] + prev_row[y])

        row.append(1)
        pascal_tri.append(row)

    return pascal_tri
