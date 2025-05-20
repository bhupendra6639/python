import time


def log_time(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Executed in {end - start:.2f} seconds")

    return wrapper


@log_time
def my_function():
    time.sleep(1)
    print("Task done!")


my_function()
