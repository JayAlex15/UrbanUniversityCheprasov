def is_prime(func):
    def wrapper(*args):
        num = func(*args)
        prime_flag = True
        for i in range(2, num):
            if num % i == 0:
                prime_flag = False
                break
        if prime_flag:
            print("Простое")
        else:
            print("Составное")
        return num
    return wrapper



@is_prime
def sum_three(*args):
    list = args
    result = sum(list)
    return result

result = sum_three(2, 3, 6)
print(result)