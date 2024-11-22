whiteLetter=input("Буква координаты белой ладьи ")
whiteNumber=int (input("Цифра координаты белой ладьи "))
blackLetter=input("Буква координаты черной ладьи ")
blackNumber=int (input("Цифра координаты черной ладьи "))

# Проверяем, бьют ли ладьи друг друга
if whiteLetter == blackLetter:  # Одна колонка
    print("Yes")
elif whiteNumber == blackNumber:  # Одна строка
    print("Yes")
else:
    print("No")