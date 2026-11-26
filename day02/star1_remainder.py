files = int(input("Количество файлов: "))
group = int(input("Размер группы: "))
print("Полных групп:", files // group)
print("Осталось файлов:", files % group)