title = input("Название проекта: ")
author = input("Имя автора: ")
group = input("Группа: ")
members = int(input("Количество участников: "))
status = input("Статус проекта: ")
technologies = ["Python", "Git", "AI"]
project = {
    "title": title,
    "author": author,
    "group": group,
    "members": members,
    "status": status,
    "technologies": technologies
}
print("=" * 40)
print("Название:", project["title"])
print("Автор:", project["author"])
print("Участников:", project["members"])
print("Технологии:", project["technologies"])
print("Первая технология:", project["technologies"][0])
print("Последняя технология:", project["technologies"][-1])
print("Количество технологий:", len(project["technologies"]))
new_tech = input("Добавить технологию: ")
project["technologies"].append(new_tech)
print("Обновлённый список:", project["technologies"])
check = input("Проверить технологию: ")
if check in project["technologies"]:
    print("Такая технология есть")
else:
    print("Такой технологии нет")
new_status = input("Новый статус: ")
project["status"] = new_status
print("=" * 40)
print("Итоговый проект:")
print(project)
print("=" * 40)