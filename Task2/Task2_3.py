#Ввод начальной цены акции
initialPrice=int(input("Начальная цена акции "))
#Ввод процента
percentage=int(input("Процент "))
months=12
#Формула сложного процента
finalPrice=initialPrice*((1+percentage/100)**months)
print(finalPrice)