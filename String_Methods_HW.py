#TASK 1
'''s = "У лукоморья 123 дуб зеленый 456"
print(s.find('я'), s.count('у'))
if s.isalpha():
    print(s.upper())
if len(s) > 4:
    print(s.lower())
s = s.replace('У', 'О')
print(s)'''

#TASK 2
'''usr_ans1 = input('Is it raining?\n')
if usr_ans1.lower() == 'yes':
    usr_ans2 = input('Is it windy?\n')
    if usr_ans2.lower() == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy ur day')'''

#TASK 3
#MISSING

#TASK 4
'''name = input('Enter you name, please: ')
surname = input('Enter your surname, please: ')
full_name = name + ' ' + surname
print(f"It's nice to meet you {full_name}, your full name is {len(full_name) - 1} characters long")'''

#TASK 5
'''name = input('Enter you name in lower, please: ')
surname = input('Enter your surname in lower, please: ')
full_name = name + ' ' + surname
print("It's nice to meet you", full_name.title())'''

#TASK 6
'''s = input('Enter any poem line:\n')
print(len(s))
start, stop = map(int, input("Enter the starting and stopping points: ").split())
print(s[start:stop])'''

#TASK 7
#MISSING

#TASK 8
'''name = input('Enter you name, please: ')
if len(name) < 5:
    surname = input('Enter your surname, please: ')
    full_name = name + ' ' + surname
    print(f"It's nice to meet you {full_name.upper()}")
else:
    print(f"It's nice to meet you {name.lower()}")'''


#TASK 9
'''a = 2 * float(input('Enter a decimal fraction: '))
print('%.2f' % a)'''

#TASK 10
'''import math
print('%.5f' %  math.pi)'''

#TASK 11
'''import math
a = math.sqrt(int(input('Enter a number greater than 500: ')))
print('%.2f' % a)'''

#TASK 12
'''a, b = map(int, input('Enter two numbers: ').split())
print(f'If you divide {a} by {b}, you get {a // b} with a remainder of {a % b}')'''

#TASK 13
'''print('Enter three numbers:')
s = 0
for i in range(3):
    s += int(input()) * 10 ** (2-i)
print('MaGiCCC: ', s)'''

#TASK 14
'''print('Equation: ax + b = 0')
a = int(input('Enter a: '))
b = int(input('Enter b: '))
print('x = ', -b / a)'''

#TASK 15
'''a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a > b:
    print(a)
else: print(b)'''

#TASK 16
'''max = 0
for i in range(3):
    a = int(input())
    if a > max or max == 0:
        max = a
print(max)'''

#TASK 17
#MISSING

#TASK 18
#MISSING

#TASK 19
'''day = int(input('Enter the day of your birth: '))
month = input('Enter the month of your birth: ')
if month == 'January':
    if day <= 19:
        print('Your zodiac sign: Capricornus')
    else:
        print('Your zodiac sign: Aquarius')
elif month == 'February':
    if day <= 18:
        print('Your zodiac sign: Aquarius')
    else:
        print('Your zodiac sign: Pisces')
elif month == 'March':
    if day <= 20:
        print('Your zodiac sign: Pisces')
    else:
        print('Your zodiac sign: Aries')
elif month == 'April':
    if day <= 19:
        print('Your zodiac sign: Aries')
    else:
        print('Your zodiac sign: Taurus')
elif month == 'May':
    if day <= 20:
        print('Your zodiac sign: Taurus')
    else:
        print('Your zodiac sign: Gemini')
elif month == 'June':
    if day <= 21:
        print('Your zodiac sign: Gemini')
    else:
        print('Your zodiac sign: Cancer')
elif month == 'July':
    if day <= 22:
        print('Your zodiac sign: Cancer')
    else:
        print('Your zodiac sign: Leo')
elif month == 'August':
    if day <= 22:
        print('Your zodiac sign: Leo')
    else:
        print('Your zodiac sign: Virgo')
elif month == 'September':
    if day <= 22:
        print('Your zodiac sign: Virgo')
    else:
        print('Your zodiac sign: Libra')
elif month == 'October':
    if day <= 23:
        print('Your zodiac sign: Libra')
    else:
        print('Your zodiac sign: Scorpius')
elif month == 'November':
    if day <= 21:
        print('Your zodiac sign: Scorpius')
    else:
        print('Your zodiac sign: Sagittarius')
elif month == 'December':
    if day <= 21:
        print('Your zodiac sign: Sagittarius')
    else:
        print('Your zodiac sign: Capricornus')'''


#TASK 20
#MISSING

#TASK 21
'''num = int(input("Enter your ticket's serial number: "))
num1 = num // 1000
if num % 10 + num // 10 % 10 + num // 100 % 10 == num1 % 10 + num1 // 10 % 10 + num1 // 100 % 10:
    print('Lucky one!')
else: print('Unlucky :(')'''

#TASK 22
'''import math
shape = input('Enter the shape: ')
if shape == 'Circle':
    r = int(input('Enter the radius: '))
    print("Circle's area: %.2f" % (math.pi * r ** 2))
elif shape == 'Triangle':
    a = int(input('Enter the length of side a: '))
    b = int(input('Enter the length of side b: '))
    c = int(input('Enter the length of side c: '))
    p = (a + b + c) / 2
    print("Triangle's area: %.2f" % (math.sqrt(p * (p - a) * (p - b) * (p - c))))
elif shape == 'Rectangle':
    a = int(input('Enter the length of side a: '))
    b = int(input('Enter the length of side b: '))
    print("Rectangle's area: ", a * b)'''