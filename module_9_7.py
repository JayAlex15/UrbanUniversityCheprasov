def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        for i in range(2, num):
            if num % i == 0:
                return f'Составное\n{num}'
            else:
                return f'Простое\n{num}'
    return wrapper



@is_prime
def sum_three(*args):
    list = args
    result = sum(list)
    return result

result = sum_three(2, 3, 6)
print(result)