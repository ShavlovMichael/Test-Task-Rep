# ЗАДАНИЕ: Простое математическое приложение (Калькулятор)
# Напишите программу, которая выполняет базовые математические операции:
# +, -, *, /
# Программа должна запрашивать у пользователя два числа и операцию, а затем выводить результат.
num1 = input('Введите число:')
sign = input('Введите операцию (+, -, *, /):')
num2 = input('Введите число:')

# проверка корректности ввода
def correct(a, b, c):
    try:
        a = float(a)
        c = float(c)
    except ValueError:
        raise ValueError('Введите корректное число')

    if b not in ['+', '-', '*', '/']:
        raise ValueError('Вы ввели недопустимую операцию. Введите корректную операцию (+, -, *, /)')

    return a, b, c

# выполнения операции
def calculate(a, sign, c):
    if sign == '+':
        return a + c
    elif sign == '-':
        return a - c
    elif sign == '*':
        return a * c
    elif sign == '/':
        if c == 0:
            raise ValueError('Деление на ноль невозможно')
        return a / c

try:
    a, sign, c = correct(num1, sign, num2)
    result = calculate(a, sign, c)
    print(f'{num1}{sign}{num2}={result}')
except ValueError as e:
    print(e)
