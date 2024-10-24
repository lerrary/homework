def apply_all_func(int_list, *functions):
    results = {}
    for j in int_list:
        if isinstance(j, int) == False:
            print('введите спиок из чисел')
            return
    for i in functions:
        results.update({i.__name__: i(int_list)})
    return results

def __min__(int_list):
    return min(int_list)

def __max__(int_list):
    return max(int_list)

def __len__(int_list):
    return len(int_list)

def __sum__(int_list):
    return sum(int_list)

def __sorted__(int_list):
    return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
