age = int(input("Возраст: "))
pass_card = input("Есть пропуск? да/нет: ")
escort = input("Есть сопровождение? да/нет: ")
if age >= 18 and pass_card == "да":
    print("Доступ разрешён")
elif escort == "да":
    print("Доступ разрешён")
else:
    print("Доступ запрещён")