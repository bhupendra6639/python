"""9. Input Validation using Assert:
- Write a function `validate_age(age)` that asserts the age is between `18` and `60`. If not,
raise an assertion error with the message `&quot;Invalid Age&quot;`.
"""


def input_Vallidation(age):
    assert 18 <= age <= 60, "Invalid Age"
    return "valid age"


print(input_Vallidation(20))
print(input_Vallidation(15))
