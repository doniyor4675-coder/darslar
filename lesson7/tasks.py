#task_1
print('\tMashq_1')
list = ['andijon', 'namangan', 'farg\'ona', 'toshkent', 'sirdaryo']
print(list)
print(sorted(list))
print(list)

#sorted(.., reverse) metodi
print('\tRo\'yhatni teskari alifbo tartibida chiqarish (sorted()):')
print(sorted(list, reverse=True))
print(list)

#reverse() metodi
print('\tRo\'yhatni teskari alifbo tartibida chiqarish (reverse()):')
list.reverse()
print(f'reverse_1: {list}')
list.reverse()
print(f'reverse_2: {list}')

#sort() metodi
print('\tsort() metodi')
list.sort()
print(f'sort_1: {list}')
list.sort(reverse=True)
print(f'sort_2: {list}')

#task_3_9
print('\tMashq_3_9')
mehmon = ['mehmon_1', 'mehmon_2', 'mehmon_3']
print(f'Mehmonlar: {mehmon}')
print(f'Men, {len(mehmon)} ta mehmon taklif qilyapman.')

#task_3_10
print('\tMashq_3_10')
list = ['andijon', 'namangan', 'farg\'ona', 'toshkent', 'sirdaryo']
print(f'Ro\'yhat: {list}')

#uzunligi
print(f'Uzunligi: {len(list)}')

#vaqtinchalik tartib alifbo
print(f'Vaqtinchalik tartib alifbo: {sorted(list)}')

#vaqtinchalik teskari tartib alifbo
print(f'Vaqtinchalik teskari tartib alifbo: {sorted(list, reverse=True)}')

#doimiy teskari tartib
list.reverse()
print(f'Doimiy teskari tartib: {list}')

#doimiy tartib alifbo
list.sort()
print(f'Doimiy tartib alifbo: {list}')

#doimiy teskari tartib alifbo
list.sort(reverse=True)
print(f'Doimiy teskari tartib alifbo: {list}')