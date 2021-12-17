#TASK 1
L = [3, 6, 7, 4, -5, 4, 3, -1]
if sum(L) > 2:
    print(len(L))
if abs(max(L)-min(L)) > 10:
    print(L.sort(reverse=True))
else: print("Разность меньше 10")

#TASK 2
favorites = [3, 7, 11, 23, 18, 48, 81]
user_number = int(input("Введите своё число"))
if user_number in L:
    print("Мое самое любимое число!")
else: print("Эх, ну почему?")

#TASK 3
import statistics

my_list = [1, 2.3, 2.1, 2.7, 5.25, 3.75]
print(statistics.stdev(my_list))


#TASK 4
line = ["Автово", "Кировский завод", "Нарвская", "Балтийская",  "Технологический институт 1", "Пушкинская", "Владимирская", "Площадь Восстания"]
user_station = input("Введите текущую станцию:")
print("Следующая станция:", line[line.index(user_station)+1])

#TASK 5
import random

list_of_words = ['самовар', 'весна', 'лето']
chosen_word = random.choice(list_of_words)
chosen_letter = random.choice(chosen_word)
print(chosen_word.replace(chosen_letter, '?'))
user_letter = input('Введите букву: ')
if user_letter == chosen_letter:
    print('Победа!\nСлово:', chosen_word)
else:
    print('Увы! Попробуйте в другой раз\nСлово:', chosen_word)


#TASK 6
phone_number = input('Enter your phone number: ')
print(phone_number[0].replace('-', ''))

#TASK 7
text = """В тот год осенняя погода
Стояла долго на дворе
Зимы ждала ждала природа
Снег выпал только в январе
На третье в ночь Проснувшись рано
В окно увидела Татьяна
Поутру побелевший двор
Куртины, кровли и забор
На стеклах легкие узоры
Деревья в зимнем серебре
Сорок веселых на дворе
И мягко устланные горы
Зимы блистательным ковром
Все ярко, все бело кругом"""
text_list = list(text)
text_list = "".join(text_list)
print("Amount of lines:", text_list.count("\n") + 1,"\nAmount of words:", text_list.count(" ") + text_list.count("\n") + 1 )

#TASK 8
import requests

response = requests.get("http://dfedorov.spb.ru/python3/src/romeo.txt")
lst = response.text.split()
print("Number of words in the text:", len(lst) + 1)

#TASK 9
L = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]],
     [[21, 22, 23, 24, 25, 26, 27, 28, 29, 30], [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]],
     [[41, 42, 43, 44, 45], [46, [47, 48], 49, 50], [51, 52, 53, 54, 55], [56, 57, 58, 59, 60]],
     [61, 62, 63, [64, 65, 66, 67, 68, 69, 70, 71], 72, 73, 74, [75, [76, 77, 78], 79], 80],
     [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]]
print(L[0][0][6])
print(L[2][1][2])
print(L[3][7][1][2])
print(L[-1][-2])