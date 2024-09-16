# Тестовое задание PZ

# Описание проекта

## Используемый стек

[![Python][Python-badge]][Python-url]
[![Django][Django-badge]][Django-url]
[![DRF][DRF-badge]][DRF-url]
[![Postgres][Postgres-badge]][Postgres-url]
[![Redis][Redis-badge]][Redis-url]


## Архитектура проекта

| Директория    | Описание                                                |
|---------------|---------------------------------------------------------|
| `infra`       | Файлы для запуска с помощью Docker, настройки Nginx     |
| `src/backend` | Код Django приложения                                   |
| `requirements` | Папка с зависимостями приложения                                  |


# Подготовка

## Требования

1. **Python 3.12**

2. **Docker**


## Разворачиваем проект в контейнерах
1. Создаём `.env` файл в корневой директории проекта и заполняем его по
образцу `.env.example`

2. Поднимаем контейнеры

   ```shell
   cd factory_manager
   ```
   ```shell
   docker compose -f infra/docker-compose.local.yml up -d
   ```


## Администрирование развёрнутого приложения
### Создание суперпользователя

```shell
docker exec -it backend python manage.py createsuperuser
```

### Для наполнения базы данных тетсовыми данными можно выполнить команду:
```shell
docker exec -it backend python manage.py make_data
```
## После запуска контейнеров сервисы будут доступны по адресам:

```shell
http://localhost:8000/api/
```

### Администрирование серисов осуществляется через админ-зону:

```shell
http://localhost:8000/admin/
```

### Описание эндпоинтов в формате OpenAPI:

```shell
http://localhost:8000/swagger/
```

### Основной эндпоинт для возрата родительских/дочерних объектов:
```shell
http://localhost:8000/api/tree/
```
<!-- MARKDOWN LINKS & BADGES -->

[Python-url]: https://www.python.org/

[Python-badge]: https://img.shields.io/badge/Python-376f9f?style=for-the-badge&logo=python&logoColor=white

[Django-url]: https://github.com/django/django

[Django-badge]: https://img.shields.io/badge/Django-0c4b33?style=for-the-badge&logo=django&logoColor=white

[DRF-url]: https://github.com/encode/django-rest-framework

[DRF-badge]: https://img.shields.io/badge/DRF-a30000?style=for-the-badge


[Postgres-url]: https://www.postgresql.org/

[Postgres-badge]: https://img.shields.io/badge/postgres-306189?style=for-the-badge&logo=postgresql&logoColor=white

[Redis-badge]:https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white
[Redis-url]: https://redis.io/
