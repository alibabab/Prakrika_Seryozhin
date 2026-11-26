score = int(input("Баллы из 20: "))
if score >= 18:
    print("Отличный результат")
elif score >= 14:
    print("Хороший результат")
elif score >= 10:
    print("Зачёт")
else:
    print("Незачёт")