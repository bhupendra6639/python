"""
8. Basic Assert Check:
- Write a function `check_positive(num)` that uses an `assert` statement to ensure the
number is positive. Test it with both positive and negative values.
"""


def positiveAssert(number):

    assert number > 0, "The number must be positive"
    return "number is Posive"


print(positiveAssert(10))
print(positiveAssert(-5))
