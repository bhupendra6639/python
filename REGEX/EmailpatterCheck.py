import re


def validate_email(email):
    # pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    # pattern = r"^[\w\.-]+@[\w\.-]{2,}\.\w{2,}$"
    pattern = r"^[\w\.-]+@[\w\.-]\.\w{2,}$"

    if re.fullmatch(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"


# find three specific character range(.com)
print(validate_email("test_1@example.c"))
print(validate_email("invalid-email.com"))


# sql query


