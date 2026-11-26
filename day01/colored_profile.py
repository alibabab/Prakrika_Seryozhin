from colorama import Fore, Style
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
group = input("Введите группу: ")
print(Fore.CYAN + "=== КАРТОЧКА ===")
print(Fore.GREEN + "Имя:", name)
print(Fore.GREEN + "Фамилия:", surname)
print(Fore.GREEN + "Группа:", group)
print(Style.RESET_ALL)