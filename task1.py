# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def task1():
    my_list = (1, 2, 3)
    sum_of_list = sum(my_list)
    print(f"Сумма чисел:", sum_of_list)


def task01():
    n = int(input('Введите три числа: '))
    print(f"Сумма чисел равна: ", sum((n//100, n//10 % 10, n % 10)))


# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа
# сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

def task2():
    num = int(input(" Сколько всего сделали?")) // 3
    print(f"Петя: {num // 2} Катя: {num * 2} Сережа: {num // 2}")


# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет
# с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

def task3():
    n = (input("Введите 6 цифр: "))
    s1 = int(n[0]) + int(n[1]) + int(n[2])
    s2 = int(n[3]) + int(n[4]) + int(n[5])
    if s1 == s2:
        print("Счастливый")
    else:
        print("Не повезло")


task3()

#  Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#  если разрешается сделать один разлом по прямой между дольками
#  (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


def task4():
    n = int(input("Введите размер шоколадки n: "))
    m = int(input("Введите размер шоколадки m: "))
    k = int(input("Введите количество долек k:3 "))

    if k < m * n and (k % m == 0 or k % n == 0):
        print('Можно')
    else:
        print('Нельзя')