name = input("Имя: ")
group = input("Группа: ")
age = int(input("Возраст: "))
speciality = input("Специальность: ")
student = {
    "name": name,
    "group": group,
    "age": age,
    "speciality": speciality
}
new_group = input("Новая группа: ")
student["group"] = new_group
print(student)