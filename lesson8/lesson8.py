# ozgarmas = ('olma', 'nok', 'uzum') #ozgarmas ro'yhat
# print(ozgarmas)
# ozgarmas_list = list(ozgarmas) #oddiy ro'yhat
# print(ozgarmas_list)
# ozgarmas_list.append('shaftoli')
# ozgarmas = tuple(ozgarmas_list)
# print(ozgarmas)

# fruits = ('olma', 'nok', 'uzum')
# for i in fruits:
#     print(f'Salom! {i.title()} bu meva o\'zgarmas ro\'yhatdan olindi.')

# for i in range(1, 10, 2):
#     print(i)

#################################################
# parol = 'admin'
# if parol == 'admin':
#     print('Salom admin xush kelibsiz!')
# else:
#     print('Parol noto\'g\'ri!')
##################################################

# tugilgan_yil = int(input('Tugilgan yilingizni yozing: '))
# if tugilgan_yil == 2000:
#     print('Sizning muchalingiz baliq!')
# else:
#     print('Muchalingiz baliq emas')

###################################################
# user_1 = int(input('1-foydalanuvchi son tanlang: '))
# user_2 = int(input('2-foydalanuvchi son tanlang: '))
# if user_1 <= 5 and user_1 >= 1 and user_2 <= 5 and user_2 >= 1:
#     if user_1 == user_2:
#         print('Ajoyib tasodif')
#     else:
#         print('Afsus o\'xshamadi')
# else:
#     print('Kimdir [1, 5] oraliqdan tashqari son kiritding!')

####################################################
# cost = int(input('Yoshingizni kiriting: '))
# if cost <= 9:
#     print('Siz uchun bilet narxi 1000 so\'m')
# elif cost > 9 and cost <= 18:
#     print('Siz uchun bilet narxi 5000 so\'m')
# elif cost > 18 and cost <= 80:
#     print('Siz uchun bilet narxi 8000 so\'m')
# else:
#     print('Siz uchun bepul')

###################################################
time = int(input('Soat nechchi bo\'ldi: '))
if time > 1 and time <= 6:
    print('Hayrli tong!')
elif time > 6 and time <= 12:
    print('Hayrli kun!')
elif time > 12 and time <= 22:
    print('Hayrli kech!')
elif time > 22 and time < 24:
    print('Hayrli tun')
else:
    print('Bunaqa vaqt yo\'q!')