print('Привет, я Джарвис!')
#Научим Джарвиса информировать вас о новых сообщениях, которые вы могли бы получить.
count = 8
message = 'У вас ' + str(count) +  ' новых сообщений'
print(message)
#Погода
temperature = -25
weather = 'солнечно'
print("Сегодня" , weather)
print("Температура воздуха" , temperature , "градусов")

#Друзья

friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']

# присвойте переменной index такое значение,
# чтобы из списка friends была выбрана Алина
index = 3

#Кто живет в Красноярске

print("Привет, я Анфиса!")
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']

# перед отправкой на проверку можете поменять индекс
# и посмотреть, как ведёт себя код
index = 2

# допишите свой код тут
print(friends[index], "живёт в Красноярске")

#Сколько друзей
print("Привет, я Анфиса!")
friends = ['Сергей', 'Соня', 'Дима', 'Алина', 'Егор']

# допишите свой код сюда
count = len(friends)
print("У тебя", count , "друзей" )

print('Привет, ' + friends[index] + ', я Джарвис!')

#Перечисление друзей

print("Привет, я Анфиса!")
friends = ['Серёга', 'Соня', 'Дима', 'Алина', 'Егор']
friends_string = ", " .join(friends)
print("Твои друзья:" , friends_string)


#Сообщения(циклы)
messages_count = 10
for i in reversed(range(2, messages_count + 1)):
    print('- Анфиса, есть ли новые письма?')
    print('- Непрочитанных писем: ' + str(i) + '.')
    print('Я прочитал одно, и их осталось ' + str(i - 1) + '.')
print('- Анфиса, есть ли новые письма?')
print('- Одно непрочитанное письмо.')
print('Я прочитал его. И нет больше писем!')

#Ветвления

import random  # импорт модуля random

# функция randint() генерирует случайное целое число в заданном диапазоне
messages_count = random.randint(0, 5)
if messages_count == 0:
    print('У вас нет новых сообщений ')
else:
    print('Новых сообщений: ' + str(messages_count))

###

import random  # импорт модуля random

 # фукнция randint() генерирует случайное целое число в заданном диапазоне
current_hour = random.randint(0, 23)

if  current_hour < 12:
    print('Доброе утро!')

###
import random  # импорт модуля random

 # фукнция randint() генерирует случайное целое число в заданном диапазоне
current_hour = random.randint(0, 23)

if  current_hour < 12:
    print('Доброе утро!')
else:
    print('Добрый день!')

#Множественные ветвления

for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас ' + str(messages_count) + ' новое сообщение')
    elif messages_count < 5:
        print('У вас ' + str(messages_count) + ' новых сообщения')
    else:
        if messages_count > 4:
            print('У вас ' + str(messages_count) + ' новых сообщений')
        else:
            print('У вас нет новых сообщений')


for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    if current_hour < 6:
        print("Доброй ночи!")
    elif current_hour < 12:
        print("Доброе утро!")
    elif current_hour < 18:
        print("Добрый день!")
    elif current_hour < 23:
        print("Добрый вечер!")
    else:
        print("Доброй ночи!")

#Логические выражения

for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")

    if current_hour >= 6 and current_hour <= 11:
        print('Доброе утро!')
    elif current_hour >= 12 and current_hour <= 17:
        print('Добрый день!')
    elif current_hour >= 18 and current_hour <= 22:
        print('Добрый вечер!')
    elif current_hour <= 5 or current_hour >= 23:
        print('Доброй ночи!')

###
# Добавьте новые условия в elif и else
for messages_count in range(0, 100):
    remainder = messages_count % 10
    if messages_count == 0:
        print('У вас нет новых сообщений')
        ...
    elif remainder == 0 or remainder >= 5:
        print('У вас ' + str(messages_count) + ' новых сообщений')
        ...
    elif messages_count >= 11 and messages_count <= 19:
        print('У вас ' + str(messages_count) + ' новых сообщений')

        ...

    elif remainder == 1:
        print('У вас ' + str(messages_count) + ' новое сообщение')

    else:
        print('У вас ' + str(messages_count) + ' новых сообщения')
        ...

#Составные логические выражения
