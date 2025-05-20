def announce_prime(func):
    def wrapper(args, kwargs):
        for num in func(*args, **kwargs):
            print("Prime Number:", num)
            yield num

    return wrapper


@announce_prime
def prime_generator(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


for prime in prime_generator(20):
    pass
