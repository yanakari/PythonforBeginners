# Ввод времени в минутах
n = int(input("Введите количество минут до конца поездки: "))

# Вычисление времени на сон в минутах
sleep_time_m = n // 2

# Перевод минут в часы и минуты
hours = sleep_time_m // 60
minutes = sleep_time_m % 60

# Вывод результата
print(hours, "ч ", minutes, "м")