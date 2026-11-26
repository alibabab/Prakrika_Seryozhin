title = input("Название проекта: ")
author = input("Автор: ")
members = int(input("Количество участников: "))
status = input("Статус: ")
project = {
    "title": title,
    "author": author,
    "members": members,
    "status": status
}
print(project["title"])
print(project["author"])
print(project["members"])
print(project["status"])