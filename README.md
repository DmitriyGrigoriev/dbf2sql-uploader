# Проект пот переносу данных из электронных копий документов в формате DBF в единое хранилище данных MSSQL.

Скачать описание формата можно на https://www.tks.ru/2007/formats/ 


## Environment Variables
#### Django
DEBUG=False
SECRET_KEY=pw+*a^45y7s_f(im2923ot2222m1h7zed4w+$03_trf4)0)!l!
DOMAIN=localhost
ALLOWED_HOSTS=192.168.89.168
SHOW_DEBUG_TOOLBAR=False
#### REDIS
REDIS_HOST=127.0.0.1

REDIS_PORT=6379
#### ETL
SHIFT_MONTHS=-1
#### EMAIL
DJANGO_ADMINS=admin:admin@localhost.ru

EMAIL_HOST=mx1.localhost.ru
SERVER_EMAIL=exchange@localhost.ru
DEFAULT_FROM_EMAIL=exchange@localhost.ru

EMAIL_HOST_USER=exchange

EMAIL_HOST_PASSWORD=ExHfusse!er

EMAIL_SUBJECT_PREFIX='[DBF to MSSQL Service] '


## Documentation

1. Для корректной работы загрузчика данных на сервере необходимо установить Advantage ODBC Driver [инструкция по установке](https://support.ispirer.com/knowledge-base/database-migration/setup-and-troubleshooting/advantage/odbc-driver-installation)

2. Обеспечить совместный доступ к каталогам с данными для импорта (файлы DBF)

3. Установить на сервер Redis

4. Прописать подключения для Advantage Database Driver (подключение формируется для каждого таможенного поста)

4.1 Прописываем путь до каталога с файлами формата обмена DBF
![Список подключений](static/images/Snapshot-06.jpg?raw=true "connection_list")

4.2 Прописываем строку соединения для Advantage Database Driver
![Строка подключения](static/images/Snapshot-07.jpg?raw=true "connection_edit")


5. Прописать подключения для MSSQL Driver

6. Прописать на сервере запуск Dramatiq для выполнения Tasks (run_dramatiq.ps1)
![Task Sheduler](static/images/Snapshot-08.jpg?raw=true "task_sheduler")

7. Прописать запуск Sheduler для загрузки данных Dramatiq по расписанию (run_sheduler.ps1)
## Настройка экспорта / импорта данных

1. Прописать Pipeline для загрузки каталог DBF -> MSSQL
![Pipeline](static/images/Snapshot-02.jpg?raw=true "pipeline")

![Pipeline](static/images/Snapshot-03.jpg?raw=true "pipeline_edit")

2. Прописать таблицы с данными для загрузки из каталога файлов DBF
![Tables](static/images/Snapshot-09.jpg?raw=true "pipe_tables")

## Ручное управление загрузкой данных в MSSQL
1. Можно просматривать статусы загрузки данных из web интерфейса в реальном времени
![Running](static/images/Snapshot-04.jpg?raw=true "running")

2. Запустить принудительную загрузку всех файлов из каталога формата обмена 
![Running](static/images/Snapshot-10.jpg?raw=true "running_all")