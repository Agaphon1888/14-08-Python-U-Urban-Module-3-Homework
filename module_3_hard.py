# Дополнительное практическое задание по модулю: "Подробнее о функциях."
# Задание "Раз, два, три, четыре, пять .... Это не всё?"

def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)
            sum += calculate_structure_sum(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum += calculate_structure_sum(item)
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
    elif isinstance(data_structure, str):
        sum += len(data_structure)
    return sum


data_structure = [
    ['apple', 'gloub', 1, [3, 4], 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
