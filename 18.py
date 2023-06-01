# Задача 18: 
# Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

count = int(input('Кол-во: '))
some_list = []
for _ in range(count):
    number = int(input())
    some_list.append(number)

x = int(input('Заданное число: '))
find_number = some_list[0]
for number in some_list:
    if abs(x - number) < abs(x - find_number):
        find_number = number
print(find_number)
