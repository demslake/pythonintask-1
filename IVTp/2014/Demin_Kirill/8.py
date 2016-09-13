# Задача 8. Вариант 5.

# 1-50. Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к
# каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у
# него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки,
# отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.

# Дёмин К.А.
# 12.09.2016

import random
words = ("питон","анаграмма","простая","сложная","ответ","подстаканник")
word=random.choice(words)
correct=word
score=10;
i=0
jumble=""
while word:
    position=random.randrange(len(word))
    jumble+=word[position]
    word=word[:position]+word[(position+1):]
print("""
    Добро пожаловать в игру 'Анаграммы'!
    Надо перемтавитьбуквы так, чтобы получилось осмысленное слово.
    Для вызова подсказки напишите: подсказка.
    (Для выхода нажмите Enter,не вводя своей версии.)
""")
print("Вот анаграмма: ", jumble)
guess=input("Попробуйте отгадать исходное слово: ")
if guess=="подсказка":
    score-=1
    print(str(i+1),"буква: ",correct[i])
    i+=1
while guess !=correct and guess!="":
        guess=input("Попробуйте отгадать исходное слово: ")
        if guess=="подсказка":
            if i==len(correct):
                print("Все буквы уже выведены.")
                continue
            score-=1
            print(str(i+1),"буква: ",correct[i])
            i+=1
            continue
if guess==correct:
    print("Да. Именно так! Вы отгадали! Вы зарабботали ",score," очков!")
else:
    print("К сожалению, Вы неправы.")
print("Спасибо за игру.")
input("\n\nНажмите Enter, чтобы выйти")
