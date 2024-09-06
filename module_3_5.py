# Самостоятельная работа по уроку "Рекурсия"
# Задача "Рекурсивное умножение цифр"

number = input('Введите любое целое число: ')

while (int(number) < 0):
    number = int(input('Введённое число меньше 0, введите заново: '))


def get_multiplied_digits(number):
    str_number = str(number)
    if int(str_number[0]) != 0:
        first = int(str_number[0])
    else:
        first = 1
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(number)
print(f'Произведение цифр введённого числа без учёта "0": {result}')
