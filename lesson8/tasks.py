#task_1
print('\tMashq_1')
number = float(input('Son kiriting: '))
if number > 0:
    if number.is_integer():
        print(f'{number:.0f} musbat son.')
    else:
        print(f'{number} musbat son.')
elif number < 0:
    if number.is_integer():
        print(f'{number:.0f} manfiy son.')
    else:
        print(f'{number} manfiy son.')
else:
    print(f'{number:.0f} son nolga teng.')

#task_2
print('\tMashq_2')
number = float(input('Son kiriting: '))
if number.is_integer():
    if number == 0:
        print(f'{number:.0f} son nolga teng.')
    elif number % 2 == 0:
        print(f'{number:.0f} son juft.')
    else:
        print(f'{number:.0f} son toq.')
else:
    print(f'{number} butun son emas!')

#task_3
print('\tMashq_3')
age = int(input('Yoshingizni kiriting: '))
if age >= 18:
    print('Siz balog\'atga yetkansiz.')
else:
    print('Voyaga yetmagansiz.')

#task_4
print('\tMashq_4')
number_1 = float(input('Birinchi son: '))
number_2 = float(input('Ikkinchi son: '))
if number_1 == number_2:
    print('Sonlar teng!')
elif number_1 > number_2:
    if number_1.is_integer():
        print(f'{number_1:.0f} soni maksimum.')
    else:
        print(f'{number_1} soni maksimum.')
else:
    if number_2.is_integer():
        print(f'{number_2:.0f} soni maksimum.')
    else:
        print(f'{number_2} soni maksimum.')

#task_5
print('\tMashq_5')
number_1 = float(input('Birinchi son: '))
number_2 = float(input('Ikkinchi son: '))
number_3 = float(input('Uchinchi son: '))
if number_1 >= number_2:
    if number_1 >= number_3:
        if number_1.is_integer():
            print(f'{number_1:.0f} soni maksimum.')
        else:
            print(f'{number_1} soni maksimum.')
    else:
        if number_1.is_integer():
            print(f'{number_3:.0f} soni maksimum.')
        else:
            print(f'{number_3} soni maksimum.')
elif number_2 >= number_3:
    if number_2.is_integer():
        print(f'{number_2:.0f} soni maksimum.')
    else:
        print(f'{number_2} soni maksimum.')
else:
    if number_3.is_integer():
        print(f'{number_3:.0f} soni maksimum.')
    else:
        print(f'{number_3} soni maksimum.')

#task_6
print('\tMashq_6')
ball = int(input('Balingizni kiriting: '))
if 90 <= ball <= 100:
    print('Baho: "A"')
elif 80 <= ball <= 89:
    print('Baho: "B"')
elif 70 <= ball <= 79:
    print('Baho: "C"')
elif 60 <= ball <= 69:
    print('Baho: "D"')
else:
    print('Baho: "F"')

#task_7
print('\tMashq_7')
password = input('Parolni kiriting: ')
if password == 'python123':
    print('Parol to\'g\'ri!')
else:
    print('Parol noto\'g\'ri!')

#task_8
print('\tMashq_8')
number = int(input('Sonni kiriting: '))
if number % 3 == 0 and number % 5 ==0:
    print('Son 3 ga va 5 ga bo\'linadi. ')
elif number % 3 == 0:
    print('Son 3 ga bo\'linadi.')
elif number % 5 == 0:
    print('Son 5 ga bo\'linadi.')
else:
    print('Son 3 ga ham 5 ga ham bo\'linmaydi.')

#task_9
print('\tMashq_9')
year = int(input('Yilni kiriting: '))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Kabisa yili.')
else:
    print('Kabisa yili emas.')

#task_10
print('\tMashq_10')
task = input('Misolni kiriting: ')
amal = 0
for i in range(len(task)):
    if task[i] == '+' or task[i] == '-' or task[i] == '*' or task[i] == '/':
        amal = i
if amal == 0:
    print('Amal noto\'g\'ri!')
else:
    number_1 = int(task[:amal])
    number_2 = int(task[amal+1:])
    if task[amal] == '+':
        print(number_1 + number_2)
    elif task[amal] == '-':
        print(number_1 - number_2)
    elif task[amal] == '*':
        print(number_1 * number_2)
    elif task[amal] == '/':
        print(number_1 / number_2)
    else:
        print('Qayerdadir xato ketdi!')