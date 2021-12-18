#TASKS 1-3
import random


def rand_pass():
    pas_a = [chr(random.randint(33, 126)) for i in range(random.randint(7, 10))]
    password = ''.join(pas_a)
    return(password)


def pass_check(seq):
    lbl_dig = lbl_low = lbl_up = 0
    if len(seq) >= 8:
        for i in seq:
            if i.isdigit() and lbl_dig == 0:
                lbl_dig = 1
            if i.islower() and lbl_low == 0:
                lbl_low = 1
            elif i.isupper() and lbl_up == 0:
                lbl_up = 1
            if lbl_dig == 1 and lbl_up == 1 and lbl_low == 1:
                return True
    return False


usr_input = input("If you want to check your pas, press 'c'\n"
                  "If you want to check a randomly generated one, press 'r'\n")
if usr_input == 'c':
    usr_pass = [input().split()]
    if pass_check(usr_pass) is True:
        print("Your password is strong enough.")
    else: print("Try another password please.")
elif usr_input == 'r':
    count = 1
    while True:
        passw = rand_pass()
        if pass_check(passw) is False:
            count += 1
        else: break
    print(f"An appropriate password {passw} was found in {count} tries")

#TASK 4
user = int(input())
k = 1
f = c = s = 0
f1 = user % 10
user //= 10
while user > 0:
    k += 1
    c = user % 10
    if k % 2 == 0:
        c *= 2
        if c >= 10:
            s += c % 10 + c // 10
        else:
            s += c
    else:
        s += c
    user //= 10
    s %= 10
    f = (10 - s % 10)

print(f)
if f1 == f:
    print('ok')
else:
    print('ne ok')