#!/usr/bin/python3
"""
0-0-pascal_triangle
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle
"""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal's triangle of n
    """
    if n <= 0:
        return []

    n_list = []
    for i in range(n):
        inner_list = [1 for _ in range(i + 1)]

        if len(n_list) <= 1:
            n_list.append(inner_list)
        else:
            temp_list = n_list[i - 1]

            for j in range(i + 1):

                # check if j is out of range of temp_list
                if j < (len(temp_list) - 1):
                    inner_list[j + 1] = temp_list[j] + temp_list[j + 1]

            n_list.append(inner_list)

    return n_list


if __name__ == "__main__":
    print(pascal_triangle(10))
