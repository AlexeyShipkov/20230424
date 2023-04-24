'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
'''
import random
list_1 = [] # список 1
list_2 = [] # список 2
list_3 = [] # список чисел, которые встречаются в обоих наборах, могут быть повторения.
list_4 = [] # список чисел, которые встречаются в обоих наборах, без повторения.
n = int(input("Введите кол-во элементов первого списка"))
m = int(input("Введите кол-во элементов второго списка"))
for i in range(n):   # цикл заполнения 1 списка случайными числами от 1 до 20 
    list_1.append(random.randint(1, 20))
for i in range(m):   # цикл заполнения 2 списка случайными числами от 1 до 20 
    list_2.append(random.randint(1, 20))
print(list_1)
print(list_2)
for i in range(n):
    for j in range(m):
        if list_1[i] == list_2[j]:
            list_3.append(list_1[i])  # формируем список чисел, которые встречаются в обоих наборах, могут быть повторения.
for l in list_3:
    if l not in list_4:
        list_4.append(l)  # формируем список чисел, которые встречаются в обоих наборах, уже без повторения.
list_4.sort()   # сортируем
print(list_4)   # выводим результат
