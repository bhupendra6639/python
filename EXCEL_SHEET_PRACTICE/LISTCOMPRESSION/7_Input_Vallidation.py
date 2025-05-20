def validate_age(age):
    assert 18 <= age <= 60, "Invalid Age"
    return "Valid age"


print(validate_age(25))
print(validate_age(10))
