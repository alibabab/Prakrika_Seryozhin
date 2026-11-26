login = "student"
password = "12345"
user_login = input("Логин: ")
user_password = input("Пароль: ")
if user_login == login and user_password == password:
    print("Доступ разрешён")
else:
    print("Неверный логин или пароль")