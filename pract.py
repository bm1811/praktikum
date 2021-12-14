steps_today = 6783
steps_yesterday = 8452

steps_sum = steps_today + steps_yesterday

print('Сколько шагов сделал Геннадий за два дня?')
print(steps_sum)


# Переименуйте переменные правильно
name = 'Данил'
family_name = 'Марков'
print('Меня зовут ' + name + ' ' + family_name + '.')


speed_kmh = 1079252848.8

# переменную speed_kms сделайте типа int
speed_kms = speed_kmh / 3600

print('Скорость света равна', int(speed_kms), 'км/с')



snake = '38.2'
length = 6.5

result = length * float(snake)

print('В вагоне можно поставить в ряд', int(result), 'попугаев')

#маршрут, в котором все станции перечислены через дефис

stations = ['Москва', 'Серп и Молот', 'Карачарово', 'Чухлинка', 'Кусково', 'Новогиреево', 'Реутово', 'Никольское', 'Салтыковская', 'Кучино', 'Железнодорожная', 'Чёрное', 'Купавна', '33-й километр', 'Электроугли', '43-й километр', 'Храпуново', 'Есино', 'Фрязево', '61-й километр', '65-й километр', 'Павлово-Посад', 'Назарьево', 'Дрезна', '85-й километр', 'Орехово-Зуево', 'Крутое', 'Воиново', 'Усад', '105-й километр', 'Покров', '113-й километр', 'Омутище', 'Леоново', 'Петушки']
print(" - " .join(stations)) # напишите свой код здесь

#Циклы

bunny_counter = ''

for i in range(1, 6):
    # На каждой итерации цикла в переменную bunny_counter дописывается очередное число
    # и запятая с пробелом, чтобы числа в строке не слиплись
    bunny_counter += str(i) + ', '

print(bunny_counter + 'вышел зайчик погулять!')

# Запустите этот код в тренажёре,
# и искусственный почти-разум напишет своё первое стихотворение

#обратный цыкл

for i in reversed(range(1, 13)):
    print(i, 'бомм!')
print('C новым годом!')



months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

for m in reversed(months):
    print(m)



print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2, 11):
    # Здесь вместо многоточий:
    # вставьте номер текущего этажа;
    # вычислите и вставьте номер предыдущего этажа
    print('А это', i , 'этаж, он на один выше, чем этаж', i-1 )

#Ветвления

beaufort = 0

if beaufort == 2:
    print('Штиль')
else:
    print('Есть ветер')

#Множественные ветвления

if beaufort == 0:
    print('Штиль')
else:
    if beaufort == 1:
        print('Тихий ветер')
    else:
        if beaufort == 2:
            print('Лёгкий ветер')
        else:
            if beaufort == 3:
                print('Слабый ветер')
            else:
                if beaufort == 4:
                    print('Умеренный ветер')
                else:
                    if beaufort == 5:
                        print('Свежий ветер')
                    else:
                        if beaufort == 6:
                            print('Сильный ветер')
                        else:
                            print('Шторм')

#упрощенный предыдущий код

if beaufort == 0:
    print('Штиль')
elif beaufort == 1:
    print('Тихий ветер')
elif beaufort == 2:
    print('Лёгкий ветер')
elif beaufort == 3:
    print('Слабый ветер')
elif beaufort == 4:
    print('Умеренный ветер')
elif beaufort == 5:
    print('Свежий ветер')
elif beaufort == 6:
    print('Сильный ветер')
else:
    # Если не сработало ни одно условие в предыдущем коде - выполняется код в блоке else
    print('Шторм')

#Логические выражения

# Если ветер в 7 или 8 баллов, то он называется крепким
if beaufort == 0:
    print('Штиль')
elif beaufort == 1:
    print('Тихий ветер')
elif beaufort == 2:
    print('Лёгкий ветер')
elif beaufort == 3:
    print('Слабый ветер')
elif beaufort == 4:
    print('Умеренный ветер')
elif beaufort == 5:
    print('Свежий ветер')
elif beaufort == 6:
    print('Сильный ветер')
elif beaufort == 7 or beaufort == 8:
    print('Крепкий ветер')

###
# если ветер от 9 до 11 баллов, то это шторм (различной силы)
if beaufort == 0:
    print('Штиль')
elif beaufort == 1:
    print('Тихий ветер')
elif beaufort == 2:
    print('Лёгкий ветер')
elif beaufort == 3:
    print('Слабый ветер')
elif beaufort == 4:
    print('Умеренный ветер')
elif beaufort == 5:
    print('Свежий ветер')
elif beaufort == 6:
    print('Сильный')
elif beaufort == 7 or beaufort == 8:
    print('Крепкий ветер')
elif beaufort >= 9 and beaufort <= 11:
    print('Шторм')
elif beaufort == 12:
    print('Ураган')
else:  # else тоже может быть в конце, после цепочки elif
    print('Неизвестное значение')

#Составные логические выражения
good_boy = True  # мальчик-то неплохой

if not good_boy:
    print('Этот в грязь полез')
    print('и рад,')
    print('что грязна рубаха.')
    print('Про такого говорят:')
    print('он плохой, неряха.')
else:
    print('Этот чистит валенки,')
    print('моет сам галоши.')
    print('Он хотя и маленький,')
    print('но вполне хороший.')

###
milk = True
cereals = False
eggs = not False

if milk and cereals or eggs:
    if eggs:
        if milk:
            breakfast = '- омлет'
        else:
            breakfast = '- яичница'
    else:
        breakfast = '- хлопья с молоком'
else:
    if milk:
        breakfast = '- стакан молока'
    elif cereals:
        breakfast = 'можно погрызть сухих хлопьев'
    else:
        breakfast = 'ничего не будет: разгрузочный день'

print('Сегодня на завтрак', breakfast)

###

# Объявление функции
def hello(name):
    print(name + ', приветствую тебя!')

# Вызов функции hello() с аргументом 'Стас Басов'
hello('Стас Басов')

def print_friends_count(friends_count):

    remainder = friends_count % 10
    if friends_count == 0:
        print('У тебя нет друзей')
    elif remainder == 0 or remainder >= 5 or (10 <= friends_count <= 19):
        print('У тебя', friends_count, 'друзей')
    elif remainder == 1:
        print('У тебя', friends_count, 'друг')
    else:
        print('У тебя', friends_count, 'друга')

print_friends_count(3)


