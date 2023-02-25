a = 1
print(a)

b = a + 2
print(b)

c = a + b * 2
print(c)

c = c + c + 2
print(c)

print(a + b + c)

z = type(c)      #Узнает какой класс
print(z)

a = 11
a += 2           # a = a + 2
print(a)

a, b = 4, 'TYYYY'
print(a, b)
# Переменные должны состоять только из букв, цифр и знаков подчеркивание
# Название переменной не должно начинаться с цифры