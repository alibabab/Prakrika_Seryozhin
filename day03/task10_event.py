age = int(input("Введите возраст: "))
reg = input("Есть регистрация? да/нет: ")
if age >= 16 and reg == "да":
    print("Доступ разрешён")
else:
    print("Доступ запрещён")