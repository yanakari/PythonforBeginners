# Ввод данных
pricePerGoose = int(input("Введите цену за одного гуся: "))
numberOfGeese = int(input("Введите количество гусей: "))

# Рассчитываем финальную цену с учетом скидок
if numberOfGeese > 10:
    totalPrice = int(pricePerGoose * numberOfGeese * 0.5)  # Скидка 50%
elif numberOfGeese > 5:
    totalPrice = int(pricePerGoose * numberOfGeese * 0.75)  # Скидка 25%
else:
    totalPrice = pricePerGoose * numberOfGeese  # Без скидки

# Вывод результата
print(totalPrice)