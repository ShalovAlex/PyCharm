a = 'Stroka'
print(a)

a = "Drugaia Stroka"
print(a)

a = """Mnogo kovichek"""
print(a)

a = "Stroka s pere\nvodom stroki i taby\tliacia"        # \n Перенос строки     \t Одиночный пробел
print(a)

a = 'Stroka s \\n Экранированием. tak ge Экраниryem \" kovichky'        # \\n Выделяет все после слеша
print(a)

print('aaa' + 'bbb')    #Конкатенация

#print('1' + 1)  #НЕЛЬЗЯ СКЛАДЫВАТЬ РАЗНЫЕ ТИПЫ ДАННЫХ

a = 1
print(str(a) + '2')     #Преобразование в строку

a = '1'
print(int(a) + 1)   #Преобразование строки в число возможно если строка содержит число

print('sos' * 3)    #Дублирование

print(len("abcdef"))    #Длина строки

a = "Длинная строка"            #Доступ по индексу
print('Первый символ равен "' + a[0] + '"\nПятый символ равен "' + a[4] + '"\nПредпоследний символ равен "' + a[-2] + '"')

a = 'Просто_строка'         #Срезы
print(a[1:2] + '\n' + a[6:] + '\n' + a[2:-2] + '\n' + a[:] + '\n' + a[::-1])

a = 'Привет'        #%s stoki Место для перемены
b = 'Пока'
print('Сначала он сказал %s, А потом добавил %s' % (b, a))
print('Сначала он сказал %s, А потом добавил %s' % (a, b))
print('Сначала он сказал {}, А потом добавил {}'.format(b, a))          #Также вставили но по-другому
print('Сначала он сказал {1}, А потом добавил {0}'.format(b, a))        #Поставили очерёдность
print(f'Сначала он сказал {a}, А потом добавил {b}')

print(1)
#Одинарный комментарий
print(2)

print(1)
"""Многострочный комментарий"""
print(2)

input("Введите ваше имя:")          #Ввод данных
print("Hello World!")              #Вывод данных