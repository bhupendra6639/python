"""

Create a function that accepts an array of floats and returns the sum of all
elements in the array."""

import array


def sum_of_array_element(arraysum):
    sum = 0
    for i in arraysum:
        sum = sum + i

    return sum


print(sum_of_array_element(array.array("i", [10, 20, 30, 40, 50])))
