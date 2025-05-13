"""
10. Assert in a Function:
- Create a function `divide(a, b)` that asserts the divisor `b` is not zero before performing
the division. If `b` is zero, raise an `AssertionError` with the message `&quot;Division by zero
error&quot;`.

"""


def Asser_Division_zero(a, b):
    assert b != 0, "please give valid value for f'{b}not give in b"
    return a // b


print("division is:-", Asser_Division_zero(10, 2))
print("division is:-", Asser_Division_zero(10, 2))
