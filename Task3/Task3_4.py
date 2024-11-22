# Ввод данных
firstThree = int(input("Введите первые три цифры номера билета: "))
lastThree = int(input("Введите последние три цифры номера билета: "))

# Сумма цифр первых трех чисел
sumFirst = (firstThree // 100) + (firstThree // 10 % 10) + (firstThree % 10)

# Сумма цифр последних трех чисел
sumLast = (lastThree // 100) + (lastThree // 10 % 10) + (lastThree % 10)

# Проверяем, счастливый ли билет
if sumFirst == sumLast:
    # Если билет счастливый, увеличиваем последние три цифры на 1
    lastThree += 1
    if lastThree == 1000:  # Если стало 1000, нужно сделать 000
        lastThree = 0

# Формируем первые три цифры с ведущими нулями
if firstThree < 10:
    firstThreeStr = "00" + str(firstThree)
elif firstThree < 100:
    firstThreeStr = "0" + str(firstThree)
else:
    firstThreeStr = str(firstThree)

# Формируем последние три цифры с ведущими нулями
if lastThree < 10:
    lastThreeStr = "00" + str(lastThree)
elif lastThree < 100:
    last_threeStr = "0" + str(lastThree)
else:
    lastThreeStr = str(lastThree)

# Объединяем части
newTicketNumber = firstThreeStr + lastThreeStr

# Вывод результата
print(newTicketNumber)