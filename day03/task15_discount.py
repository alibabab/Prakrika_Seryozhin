total = float(input("Сумма покупки: "))
if total >= 5000:
    discount = total * 0.10
    total = total - discount
print("Итоговая стоимость:", total)