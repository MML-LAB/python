
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
print(dict(enumerate(lsts)))
---------------------------------------------
from random import randint
print("Угадайте число от 1 до 20")
guess = 1
rnumber = randint(1, 3)
while guess<=5:
    num = int(input("введите число: "))
    guess +=1
    if num > rnumber:
        print("Слишком много ")
    elif num < rnumber:
        print("Слишком мало ")
    elif num == rnumber:
        break
    print("Попытка", guess," Не угадали! попробуйте еще раз!")
if num == rnumber:
    print("Класс! Вы угадали", num, "=", rnumber)
else:
    print("Все, вы не выиграли. Игра завершилась.", "Загадано число -",rnumber)
------------------------------------------------------------

text = input("Введите 7 значное количество символов ")
dlinna = len(text)
if (dlinna % 2) == 0:
    print("четное количество символов")
else:
    print(text[2:5])


-------------------------------------------------
n = 0
a = "Aidana"
b = "Adilet"
while n < len(a) and n<len(b):
    print(a[n]+b[n])
    n+=1
