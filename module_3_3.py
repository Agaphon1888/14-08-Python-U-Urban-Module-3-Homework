# Самостоятельная работа по уроку "Распаковка позиционных параметров".

def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(3, 6, 9)
print_params(a=3)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['Алексей', True, 3.14]
values_dict = {'a': True, 'b': 'Алексей', 'c': 3.14}

print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]

print()
print_params(*values_list_2, 42)
