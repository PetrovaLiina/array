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
zero_list = [] #нули
for i in arr:
    for j in i:
        if j > 1:
            positive_list.append(j)
        if j < 1:
            negative_list.append(j)
        if j == 0:
            zero_list.append(j)
print('Количество положительных чисел: ', len(positive_list), 'Количество отрицательных чисел: ', len(negative_list))