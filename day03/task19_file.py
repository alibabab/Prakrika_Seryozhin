size = float(input("Размер файла в МБ: "))
if size <= 10:
    print("Файл подходит")
elif size <= 50:
    print("Файл большой")
else:
    print("Файл слишком большой")