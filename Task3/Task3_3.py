type=int (input("Тип перевода "))
rubToGoldRate=int (input("Курс рубля к золоту "))
usdToGoldRate=int (input("Курс доллара к золоту "))
amount=int (input("Число валюты, которую нужно перевести "))

# Выполняем перевод в зависимости от типа
if type == 1:
    # Перевод из рублей в доллары
    goldAmount = amount * rubToGoldRate  # Рубли в золото
    usdAmount = goldAmount / usdToGoldRate  # Золото в доллары
    print(amount, " Руб это ", usdAmount, " $ ")
elif type == 2:
    # Перевод из долларов в рубли
    goldAmount = amount * usdToGoldRate  # Доллары в золото
    rubAmount = goldAmount / rubToGoldRate # Золото в рубли
    print(amount, " $ это ", rubAmount, " Руб")
else:
    print("Неверный тип перевода")