# Задача 6. Вариант 5.

# Создайте игру, в которой компьютер загадывает один из трех цветов светофора, а игрок должен его угадать.

# Дёмин К.А.
# 12.09.2016

import random

print('Программа случайным образом загадывает один из трех цветов светофора, а игрок должен его угадать.')

colors = ['Красный', 'Жёлтый', 'Зелёный']
a = random.randint(0,2)
b = colors[a]
c = input('Назовите цвет, который, по вашему мнению, загадал компьютер: ')

if b == c :
    print('\nВы угадали!')
else :
    print('\nВы не угадали!')
    print('Правильный ответ: '+b)

input('\n\nНажмите Enter для выхода.')
