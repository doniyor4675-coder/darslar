#task3_4
print('\tTask_3_4')
names = ['sardor', 'sarvar', 'sanjar']
for i in names:
    print(f'Salom, {i.title()}! Men sizni kechki ovqatga taklif qilaman.')

#task3_5
print('\tTask_3_5')
names = ['sardor', 'sarvar', 'sanjar']
names.pop()
names.append('vali')
for i in names:
    print(f'Salom, {i.title()}! Men sizni kechki ovqatga taklif qilaman.')

#task3_6
print('\tTask_3_6')
names = ['sardor', 'sarvar', 'sanjar']
names.insert(0, 'birinchi')
names.append('oxirgi')
index = len(names) // 2
names.insert(index, 'o\'rtasi')
print(names)

#task3_7
print('\tTask_3_7')
names = ['sardor', 'sarvar', 'sanjar', 'said']
print(f'Mening ro\'yhatim: {names}')
for i in range(2, len(names)):
    x = names.pop()
    print(f'{x.title()} kechirasiz, bu safar sizni taklif qila olmayman.')
for l in range(2):
    print(f'Salom, {names[0].title()}! Men sizni kechki ovqatga taklif qilaman.')
    del names[0]
print(f'Qolgan ro\'yhat: {names}')

#task3_8
print('\tTask_3_8')
books = ['kitob_1', 'kitob_2', 'kitob_3']
for i in books:
    print(f'{i.title()} - bu mening eng yaxshi kitoblarimdan biri.')

#task3_9
print('\tTask_3_9')
books = ['kitob_1', 'kitob_2', 'kitob_3']
print(f'Eski ro\'yhat: {books}')
books.pop(1)
books.insert(1, 'yangi_kitob')
print(f'Yangi ro\'yhat: {books}')

#task3_10
print('\tTask_3_10')
books = ['kitob_1', 'kitob_2', 'kitob_3']
print(f'Eski ro\'yhat: {books}')
books.insert(0, 'kitob_boshiga')
books.append('kitob_oxiriga')
index = len(books) // 2
books.insert(index, 'kitob_o\'rtasiga')
print(f'Yangi ro\'yhat: {books}')

#task3_11
print('\tTask_3_11')
books = ['kitob_1', 'kitob_2', 'kitob_3', 'kitob_4']
print(f'Mening ro\'yhatim: {books}')
for i in range(0, len(books) - 2):
    x = books.pop(0)
    print(f'Afsus, bu safar {x.title()} ro\'yhatda qolmadi.')
for l in range(2):
    print(f'{books[0].title()} hali ham ro\'yhatda.')
    del books[0]
print(f'Qolgan ro\'yhat: {books}')

#task3_12
print('\tTask_3_12')
foods = ['taom_1', 'taom_2', 'taom_3']
for i in foods:
    print(f'{i.title()} - juda mazali!')

#task3_13
print('\tTask_3_13')
foods= ['taom_1', 'taom_2', 'taom_3']
print(f'Eski ro\'yhat: {foods}')
foods.pop(1)
foods.insert(1, 'yangi_taom')
print(f'Yangi ro\'yhat: {foods}')

#task3_14
print('\tTask_3_14')
foods = ['taom_1', 'taom_2', 'taom_3']
print(f'Eski ro\'yhat: {foods}')
foods.insert(0, 'taom_boshiga')
foods.append('taom_oxiriga')
index = len(foods) // 2
foods.insert(index, 'taom_o\'rtasiga')
print(f'Yangi ro\'yhat: {foods}')

#task3_15
print('\tTask_3_15')
foods = ['taom_1', 'taom_2', 'taom_3', 'taom_4']
print(f'Mening ro\'yhatim: {foods}')
for i in range(0, len(foods) - 2):
    x = foods.pop(0)
    print(f'Kechirasiz, {x.title()} bu safar menyuda yo\'q.')
for l in range(2):
    print(f'{foods[0].title()} menyuda qolmoqda.')
    del foods[0]
print(f'Qolgan ro\'yhat: {foods}')

#task3_16
print('\tTask_3_16')
sport = ['sport_1', 'sport_2', 'sport_3']
for i in sport:
    print(f'{i.title()} - bu juda foydali sport turi.')

#task3_17
print('\tTask_3_17')
sport = ['sport_1', 'sport_2', 'sport_3']
sport.pop(1)
sport.insert(1, 'yangi_sport')
print(f'Yangi ro\'yhat: {sport}')

sport.insert(0, 'sport_boshiga')
sport.append('sport_oxiriga')
index = len(sport) // 2
sport.insert(index, 'sport_o\'rtasiga')
print(f'Yangi ro\'yhat: {sport}')

for i in range(0, len(sport) - 2):
    x = sport.pop(0)
    print(f'{x.title()} ro\'yhatdan olib tashlandi.')
for l in range(2):
    print(f'{sport[l].title()} ro\'yhatda qolmoqda.')
print(f'Qolgan ro\'yhat: {sport}')