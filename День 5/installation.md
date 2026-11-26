# Установка инструментов

Git
Git уже был установлен. Команда git --version показала git version 2.43.0. Установка не потребовалась.
Для архивов я установил git-lfs командой sudo apt install -y git-lfs. Версия 3.4.1.

Python и venv
sudo apt update
sudo apt install -y python3-pip python3-venv unzip pciutils
python3 --version
python3 -m pip --version

Результат: Python 3.12.3 и pip 24.0.

Зависимости
В папке агента не было requirements.txt. Я создал файл и вписал две строки из отчёта за третий день: gigachat и python-dotenv.
Команды установки:
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt

Установились gigachat 0.2.4 и python-dotenv 1.2.4 вместе с зависимостями.

Результат pip check
No broken requirements found.

Ошибки и их причины
Сначала ZIP архивы были по 133 байта. Причина в том, что Git LFS не был установлен. Я исправил это установкой git-lfs и командой git lfs pull.
В папке агента не было requirements.txt, README.md и .env.example. Файлы requirements.txt и .env.example я создал. README не создавал.
В архиве был старый файл .env с ключом. Я поставил на него права 600 и не публиковал ключ.

Что удалось исправить
Поставил pip, venv, unzip, pciutils и git-lfs.
Создал новое окружение .venv под Linux.
Установил зависимости.
Команда pip check не нашла конфликтов.