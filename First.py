s1 = input()
s2 = input()

print('длина первой строки: ' + str(len(s1)), 'Длина второй строки: ' + str(len(s2)))     # Показывает длину введенных строк

# a1 = s1[0]     # Показывает первый и последний символ первой строки
# a2 = s1[-1]
# print(a1, a2)

# b1 = s2[0]     #Показывает первый и последний символ второй строки
# b2 = s2[-1]
# print(b1, b2)

print(s1 == s2)     # Сравнивает обе строки

if s1 in s2:      # Определяет наличие первой строки во второй
    print('Строка s1 содержит строку s2')
else:
    print('Не содержит')

print(s2 in s1)
