def apply_all_func(int_list, *functions):
    results = {}
    for j in int_list:
        if isinstance(j, int) == False:
            print('введите спиок из чисел')
            return
    for i in functions:
        results.update({i.__name__: i(int_list)})
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
