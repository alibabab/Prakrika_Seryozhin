name = input("Имя участника: ")
age = int(input("Возраст: "))
course = input("Курс: ")
consent = input("Согласие на участие да/нет: ")
score = int(input("Тестовый балл от 0 до 100: "))
print("=" * 40)
print("Имя:", name)
print("Курс:", course)
print("Балл:", score)
if age < 16:
    print("Результат: Возраст не подходит")
    print("Заявка отклонена")
elif consent != "да":
    print("Результат: Нет согласия на участие")
    print("Заявка отклонена")
else:
    if score >= 90:
        result = "Высокий результат"
    elif score >= 70:
        result = "Хороший результат"
    elif score >= 50:
        result = "Допустимый результат"
    else:
        result = "Результат недостаточен"
    print("Результат:", result)
    print("Заявка обработана")
print("=" * 40)