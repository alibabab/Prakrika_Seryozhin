score = int(input("Балл: "))
if score < 0 or score > 100:
    print("Некорректный балл")
elif score >= 90:
    print("Отлично")
elif score >= 70:
    print("Хорошо")
else:
    print("Нужно доработать")