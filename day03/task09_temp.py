temp = float(input("Введите температуру: "))
if temp > 25:
    print("Жарко")
elif temp >= 15:
    print("Тепло")
elif temp >= 0:
    print("Прохладно")
else:
    print("Холодно")