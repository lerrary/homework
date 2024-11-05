def is_prime(func):
    def wrapper(a, b, c):
        res_ = func(a, b, c)
        pr_ = True
        for i in range(res_):
            if i == 1:
                continue
            for j in range(2, i):
                if i % j == 0:
                    pr_ = False
                    break
        if not pr_:
            print('Простое')
        else:
            print('Составное')
        return res_
    return wrapper
@is_prime
def sum_three(a, b, c):
    sum_ = a+b+c
    return sum_

result = sum_three(2, 3, 6)
print(result)
