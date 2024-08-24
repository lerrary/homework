sum_int = []
def calculate_structure_sum(data_structure):
    global sum_int
    for i in data_structure:
        if isinstance(i, int) == True:
            sum_int.append(i)
        elif isinstance(i, float) == True:
            sum_int.append(i)
        elif isinstance(i, str) == True:
            sum_int.append(len(i))
        elif isinstance(i, list) == True:
            calculate_structure_sum((i))
        elif isinstance(i, tuple) == True:
            calculate_structure_sum((i))
        elif isinstance(i, set) == True:
            calculate_structure_sum((i))
        elif isinstance(i, dict) == True:
            calculate_structure_sum(list(i.values()))
            calculate_structure_sum(list(i.keys()))

    return sum(sum_int)

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
