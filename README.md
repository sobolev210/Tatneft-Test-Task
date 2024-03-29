# Структура репозитория

В директории task1 находится ответ на Задание 1

В директории task2 находится ответ на Задание 2

Ответ на Задание 3 представлен ниже


# Задание 3


## 1. Схема API для Сервера-посредника для взаимодействия с клиентами

Схема API в .yaml формате представлена здесь:

[.yaml-схема](https://github.com/sobolev210/Tatneft-Test-Task/blob/master/task3/api_schema_v1.yaml)

Можно открыть ее в онлайн-редакторе, например:

https://editor.swagger.io/

Скриншот части схемы:

[Cкриншот.png](https://github.com/sobolev210/Tatneft-Test-Task/blob/master/task3/api_schema_v1_screenshot.png)

## 2. Схема работы Сервера-посредника. Список необходимых инструментов/библиотек

Визуальная схема работы Сервера-посредника представлена здесь:
 - [схема в формате .png](https://github.com/sobolev210/Tatneft-Test-Task/blob/master/task3/architecture_schema.png)
 - [.drawio файл](https://github.com/sobolev210/Tatneft-Test-Task/blob/master/task3/architecture_schema.drawio)


### Взаимодействие с Источниками:

Получение данных из обоих источников происходит в celery-задачах. Задачи выполняются по расписанию при помощи celery beat.
В каждой задаче происходит запрос данных из Источника1/Источника2. Затем происходит создание новых/обновление существующих данных в БД.
Данные создаются и обновляются в одной транзакции, чтобы избежать ситуации, когда часть данных уже обновлена, а часть - нет.

Для Источника 1 (в котором информация "меняется примерно раз в два дня") задача запускается раз в день.

Для Источника 2 (в котором информация "меняется примерно два-три раза в сутки в произвольное время") задача запускается раз в 5 минут.
Периодичность задачи можно менять в настройках в зависимости от того, насколько критично Клиентам получать самые "свежие" данные от Сервера-посредника, и насколько часто Клиенты обращаются в Сервер-посредник за данными



### Взаимодействие с Клиентами:
1. Клиент должен получить от Сервера-посредника токен. Этот токен Клиент будет использовать при запросе данных из Сервера-посредника.
2. Клиент отправляет HTTP-запрос в Сервер-посредник для получения данных.
3. Сервер достает уже сохраненные данные из БД, сериализует их и возвращает обратно клиенту.



### Список необходимых инструментов и библиотек:

Инструменты:

- PostgreSQL - хранение данных на Сервере-посреднике
- Redis - брокер сообщений для celery
- Docker - запуск Сервера-посредника

Версия Python: 3.11

Библиотеки:

- Django (в качестве основного фреймворка выбран Django, т.к. нужно реализовать административный интерфейс)
- Django REST Framework
- celery
- redis (для работы с Redis)
- pillow (для работы с изображениями)
- psycopg2 (для работы с PostgreSQL)
- requests (для выполнения запросов в Источник1/Источник2 в celery-задачах)
- drf-spectacular (для генерации документации к API)
- djangorestframework-simplejwt (для jwt-аутентификации)

### Дополнительно:

Также при желании в директории task3 можно найти имплементацию Сервера-посредника, и простую имплементацию Источников 1 и 2.

Для запуска нужно находиться в директории task3 и выполнить команду:

`docker compose --env-file server/.env.example up -d --build
`

Для входа в панель администратора нужно создать суперпользователя внутри контейнера
