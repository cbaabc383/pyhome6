# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Enter the 1st element: "))
d = int(input("Enter the step: "))
n = int(input("Enter the number of elements: "))
array = [0] * n

for n in range(n):
    array[n] = a1 + n * d
print(*array)
