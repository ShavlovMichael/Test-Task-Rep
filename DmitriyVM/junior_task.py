# ЗАДАНИЕ: Простое математическое приложение (Калькулятор)
# Напишите программу, которая выполняет базовые математические операции:
# +, -, *, /
# Программа должна запрашивать у пользователя два числа и операцию, а затем выводить результат.

x = 0
y = 0
o = ''

def err():
	print('Ошибка ввода  данных')
	exit()
	
try:
	print('Введите первое число:')
	x = input()
	x = float(x)
except:
	err()

try:
	print('Введите операцию(+, -, *, /):')
	o = input()
	if o == '+' or o == '-' or o == '*' or o == '/':
		print('Знак  операции введен верно')
	else:
		err()
except:
	err()

try:
	print('Введите второе число:')
	y = input()
	y = float(y)
except:
	err()

if o == '+':
	print(x + y)
elif o == '-':
	print(x - y)
elif o == '*':
	print(x * y)
else:
	if y == 0 or x == 0:
		print('Делить на ноль нельзя')
	else:
		print(x / y)
