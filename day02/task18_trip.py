ticket = float(input("Стоимость билета: "))
people = int(input("Количество человек: "))
service = float(input("Доп услуга на человека: "))
tickets_total = ticket * people
services_total = service * people
total = tickets_total + services_total
print("Стоимость билетов:", tickets_total)
print("Стоимость услуг:", services_total)
print("Общая сумма:", total)