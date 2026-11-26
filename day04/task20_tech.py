title = input("Название проекта: ")
author = input("Автор: ")
members = int(input("Количество участников: "))
status = input("Статус: ")
project = {
    "title": title,
    "author": author,
    "members": members,
    "status": status,
    "technologies": ["Python", "Git", "SQL"]
}
print(project["title"])
print(project["technologies"])
print(project["technologies"][0])