def calculate_structure_sum(initial_data):
    sum = 0
    if isinstance(initial_data, (list, tuple, set)):
        for item in initial_data:
            sum += calculate_structure_sum(item)
    elif isinstance(initial_data, dict):
        for key, value in initial_data.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
    elif isinstance(initial_data, int):
        sum += initial_data
    elif isinstance(initial_data, str):
        sum += len(initial_data)
    return sum

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
                  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)