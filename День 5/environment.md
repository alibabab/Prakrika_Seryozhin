# Среда эксплуатации

Дата проверки: 20.11.2026
ОС и версия: Ubuntu 24.04.1 LTS
Пользователь Ubuntu: serezhin
Имя машины: seryzhin2
Версия Python: 3.12.3
Версия Git: 2.43.0
Версия git-lfs: 3.4.1
IP виртуальной машины: 10.0.2.15
Интернет: есть
Путь к проекту: /home/serezhin/projects/Prakrika_Seryozhin/UP01_Seryozhin/final_agent

Проверка системы
Команда lsb_release -a показала Ubuntu 24.04.1 LTS и код noble.
Команда whoami показала serezhin.
Команда pwd показала /home/serezhin.
Команда hostname показала seryzhin2.
Команда uname -srm показала Linux 6.8.0-149-generic x86_64.
Команда ping -c 4 github.com отправила 4 пакета и получила 4 ответа. Потерь нет.
Команда ip -br a показала адрес 10.0.2.15 на enp0s3.
Команда sudo -v пароль приняла. Права на установку есть.

Что было в репозитории
После git clone были только README.md, UP01_Seryozhin.zip и UP02_Seryozhin.zip.
Архивы были LFS указателями, потому что git-lfs не был установлен. После установки git-lfs и команды git lfs pull архивы скачались.
Папки УП01/AI-Agent нет. Агент лежит в UP01_Seryozhin/final_agent после распаковки архива.

Вывод
Среда готова. Проект перенесён. Структура папок отличается от той, что описана в задании.