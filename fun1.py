from random import randint as rnd

a = (int(input("Бажана довжина списку")))
b = (int(input("Максимальне значення елеметів списку")))

def Єнотік (a, b):
    list = []
    for i in range(a):
        list.append(rnd(0,b+1))
        return list

    print(Єнотік(a, b))
