tools = ["VS Code", "Git", "Docker", "Linux"]
answer = input("Введите инструмент: ")
if answer in tools:
    print("Такой инструмент есть")
else:
    tools.append(answer)
    print("Добавлено")
    print(tools)