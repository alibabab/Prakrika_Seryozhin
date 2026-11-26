allowed = [".txt", ".csv", ".json"]
ext = input("Введите расширение: ")
if ext in allowed:
    print("Разрешено")
else:
    print("Не разрешено")