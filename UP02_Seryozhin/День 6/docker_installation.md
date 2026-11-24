# Установка Docker

Что было до установки
Docker не был установлен. Старые пакеты docker.io, docker-compose, podman-docker, containerd и runc не найдены.

Команды установки
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

Затем я создал файл /etc/apt/sources.list.d/docker.sources с адресом https://download.docker.com/linux/ubuntu, веткой noble и компонентом stable.

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

Результат
Docker version 29.10.0, build fdd4b8e
Docker Compose version v5.8.0
Служба docker.service: active running
Служба запущена и добавлена в автозапуск.

Ошибки при установке
Были предупреждения apt про нестабильный командный интерфейс. Это не ошибка.
Были предупреждения debconf про отсутствие терминала. Установка всё равно завершилась успешно.
Других ошибок не было.

Проверка
sudo systemctl status docker --no-pager показала active running.
docker --version и docker compose version показали версии.
Команды выполнялись через sudo, как сказано в задании.