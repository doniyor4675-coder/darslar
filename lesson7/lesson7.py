list_1 = []
list_2 = []
i = 0
while i < 1:
    student = input('Talabaning ismi: ')
    list_1.append(student)
    a = input('Davom etishni xohlaysizmi:')
    if a == 'yo\'q' or a == 'Yo\'q' or a == 'YO\'Q':
        i += 1
print(list_1)