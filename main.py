import random

n = int(input('Введите число n: '))  # количество строк
m = int(input('Введите число m: '))  # количество столбцов
arr = []
for i in range(n):
    arr_2 = []
    for j in range(m):
        arr_2.append(random.randint(-10, 10))
    arr.append(arr_2)
print(arr)
positive_list = [] #все положительные значения
negative_list = [] #все отрицательные числа
