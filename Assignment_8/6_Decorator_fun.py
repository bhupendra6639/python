def check_user_type(func):
    def wrapper(*args, **kwargs):
        if kwargs.get("user_type") == "admin":
            print("Access Granted")
            return func(*args, **kwargs)
        else:
            print("Access Denied")

    return wrapper


@check_user_type
def view_dashboard(user_type=None):
    print("Welcome to the admin dashboard.")


# Test cases
view_dashboard(user_type="admin")  #  Access granted
view_dashboard(user_type="guest")  #  Access denied
