# Тестовое задание PZ

# Описание проекта

## Используемый стек

[![Python][Python-badge]][Python-url]
[![Django][Django-badge]][Django-url]
[![DRF][DRF-badge]][DRF-url]
[![Postgres][Postgres-badge]][Postgres-url]
![Redis] [Redis-badge][Redis-url]


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


# Разворачиваем проект в контейнерах
1. Создаём `.env` файл в корневой директории проекта и заполняем его по
образцу `.env.example`

2. Поднимаем контейнеры
   ```shell
   docker compose -f infra/docker-compose.local.yml up -d
   ```

# После запуска контейнеров сервисы будут доступны по адресам:

```http://localhost:8000/api/```

# Администритрование серисов осуществляется через админ-зону:

```http://localhost:8000/admin/```

# Описание эндпоинтов:

```http://localhost:8000/swagger/```


## Администрирование развёрнутого приложения
### Создание суперпользователя

Создаем суперпользователя:
```shell
docker exec -it backend python manage.py createsuperuser
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

[Redis-badge]:(https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
[Redis-url]: https://redis.io/
