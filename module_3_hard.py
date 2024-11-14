data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum = 0

def calculate_structure_sum(data_structure):
    global sum

    for user_item in data_structure:
        if isinstance(user_item, int):
            sum += user_item
        elif isinstance(user_item, str):
            sum += len(user_item)
        elif isinstance(user_item, dict):
            for key in user_item.keys():
                sum += len(key)
            for value in user_item.values():
                if isinstance(value, int):
                    sum += value
                else:
                    calculate_structure_sum(value)
        else:
            calculate_structure_sum(user_item)

    return sum


result = calculate_structure_sum(data_structure)
print(result)