#TASK 1
a = [int(i) for i in input().split()]
num = int(input('Enter a number: '))
min = -1
for x in a:
    if abs(num - x) < min or min == -1:
        min = abs(num - x)
        res = x
print(f'The closest number to {num} in {a} is {res}')

#TASK 2
countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

print("Countries' average temperature:\n")
for country in countries_temperature:
        print(country[0], ' - %.1f C' % ((sum(country[1]) / len(country[1]) - 32) / 1.8))


#TASK 3
import random
import statistics

a = [random.randint(-100, 100) for i in range(100)]
print(statistics.median(a))

#TASK 4
import random

a = [random.randint(100, 200) for i in range(1000)]
count = 0
sum = 0
for i in a:
    if i > 170 and i < 195:
        sum += i
        count += 1
print(f"The number of elements greater than 170 and lesser than 195\n"
      f"in the list is {count} and their sum equals {sum}")

#TASK 5
import math

def my_log(mas):
    log_lst = []
    for i in mas:
        if i > 0:
            log_lst.append(math.log(i))
        else:
            log_lst.append('None')
    return log_lst

a = [float (i) for i in input('Enter a list of numbers:\n').split()]
print(my_log(a))