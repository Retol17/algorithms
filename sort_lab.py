from random import randint
from time import time

def generation():
    # count_list = 5
    print(" N:\n 1 - 1000\n 2 - 5000\n 3 - 10000\n 4 - 50000\n 5 - 100000\n Выберете необходимый размер массива по его номеру: ")
    a = int(input())
    if a == 1:
        count_list = 1000
    elif a == 2:
        count_list = 5000
    elif a == 3:
        count_list = 10000
    elif a == 4:
        count_list = 50000
    elif a == 5:
        count_list = 100000
    else:
        print("Вы ввели не правильное число")
    try:
        with open(r"input.txt","w",encoding="utf-8") as file:
            while count_list != 0:
                file.write(str(randint(-25000,25000))+" ")
                count_list = count_list - 1
    finally:
        file.close()


def read_file():
    generation()
    try:
        with open(r"input.txt","r",encoding="utf-8") as file:
            massiv=[int(i) for i in file.read().split()]
    finally:
        file.close()
    print('Список для сортировки готов')
    return massiv

def bubble_method(list):
    count_permutation = 0
    t0 = time()
    lenght = len(list)
    while lenght != 0:
        max_index = 0
        for i in range(1, len(list)):
            if list[i - 1] > list[i]:
                count_permutation=count_permutation+1
                s = list[i - 1]
                list[i - 1] = list[i]
                list[i] = s
                max_index = i
        lenght = max_index
    t1 = t0 - time()
    print(f"Отсортированный список:\n{list}\nВремя потраченое на его сортировку: {t1}\nКоличество перестановок:{count_permutation}")
    try:
        file = open("time.txt",'a',encoding="utf-8")
        file.write(f"Метод пузырька({len(list)} элементов) Время:{t1} Количество перестановок:{count_permutation}\n")
    finally:
        file.close()

def casual_method(list):
    count_permutation = 0
    t0 = time()
    for i in range(0, len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        if min_index != i:
            temp = list[min_index]
            list[min_index] = list[i]
            list[i] = temp
            count_permutation=count_permutation+1
    t1 = t0 - time()
    print(f"Отсортированный список:\n{list}\nВремя потраченое на его сортировку: {t1}\nКоличество перестановок:{count_permutation}")
    try:
        file = open("time.txt",'a',encoding="utf-8")
        file.write(f"Метод простого выбора({len(list)} элементов) В  ремя:{t1} Количество перестановок:{count_permutation}\n")
    finally:
        file.close()

def fast_method(list):
    lower = []
    upper = []
    middle = []
    if len(list) > 1:
        elem = list[0]
        for i in list:
            if i < elem:
                lower.append(i)
            elif i == elem:
                middle.append(i)
            elif i > elem:
                upper.append(i)
        return fast_method(lower) + middle + fast_method(upper)
    return list

def hairbrush_method(list):
    count_permutation = 0
    t0 = time()
    step = len(list) - 1
    while step > 0:
        for i in range(0, len(list) - step):
            if (list[i] > list[i + step]):
                list[i], list[i + step] = list[i + step], list[i]
                count_permutation=count_permutation+1
        step = int(step // 1.25)
    t1 = t0 - time()
    print(f"Отсортированный список:\n{list}\nВремя потраченое на его сортировку: {t1}\nКоличество перестановок:{count_permutation}")
    try:
        file = open("time.txt", 'a', encoding="utf-8")
        file.write(f"Метод расчески({len(list)} элементов) Время:{t1} Количество перестановок:{count_permutation}\n")
    finally:
        file.close()



def main():
    print(" Методы:\n 1 - Обычная сортировка\n 2 - Метод пузырька \n 3 - метод расчески \n 4 - метод быстрой сортировки\n выберите желаемый метод сортировки по его номеру:")
    choice = int(input())
    list_number = read_file()
    if choice == 1:
        casual_method(list_number)
    elif choice == 2:
        bubble_method(list_number)
    elif choice == 3:
        hairbrush_method(list_number)
    elif choice == 4:
        t0 = time()
        spisok = fast_method(list_number)
        t1 = t0 - time()
        print(f"Отсортированный список:\n{spisok}\nВремя потраченое на его сортировку: {t1}, а вот здесь кол перестановок нету, потому что рекурсия")
        try:
            file = open("time.txt", 'a', encoding="utf-8")
            file.write(
                f"Метод быстрой сортировки({len(list_number)} элементов) Время:{t1}\n ")
        finally:
            file.close()
    else:
        print("Вы ввели не верное число")

main()



