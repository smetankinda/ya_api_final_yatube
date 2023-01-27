# api_final_yatube - (доработанный проект api_yatube) REST API для проекта Yatube

## Автор:
Сметанкин Дмитрий [smetankinda](https://github.com/smetankinda)

## Описание:
api_final_yatube - это REST API для блог-платформы Yatube. Реализована возможность просматривать и создавать посты, просматривать группы, подписываться на авторов других постов.

Технологии:
- Python 3.9, 
- Django 3, 
- Django REST Framework 3,
- Simple JWT. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/smetankinda/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Описание проекта

При запуске проекта, по адресу http://ip:port/redoc/ доступна документация в формате Redoc для API Yatube.

Для аутентифицированный пользователя доступно изменение и удаление своего контента, для гостевого пользователя предоставлено чтение. При попытке изменить чужие записи возвращается 403 Forbidden.

## Примеры запросов:

### Пример запроса на создание нового пользователя:
```
### Запрос: POST http://ip:port/api/v1/users/
{
    "username": "newuser",
    "password": "Newpassword123"
}
```
### Ответ:
```
{
    "email": "",
    "username": "newuser",
    "id": 2
}
```
### Пример запроса токена зарегестрированного пользователя:
### Запрос POST http://ip:port/api/v1/jwt/create/
```
{
    "username": "newuser",
    "password": "Newpassword123"
}
```
### Ответ:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDg0OTUyMCwianRpIjoiOGJhYzA1MDkyOTA5NDJmY2FjYTZkZTI4ZGQ4OTlmODEiLCJ1c2VyX2lkIjoyfQ.w.....",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0ODQ5NTIwLCJqdGkiOiI2YzhjMDM3NTU0Njg0NjdmOWViOTU0MWUzYjg3YmZiMiIsInVzZXJfaWQiOjJ9.1....."
}
```
### Пример создания поста авторизованным пользователем:
### Запрос POST http://ip:port/api/v1/posts/
```
{
    "text": "Тестовый пост 1",
    "group": "1"
}
```
### Ответ:
```
{
    "id": 1,
    "author": "newuser",
    "text": "Тестовый пост 1",
    "pub_date": "2023-01-27T15:30:38.460901Z",
    "image": null,
    "group": 1
}
```
### Пример просмотра списка постов:
### Запрос GET http://ip:port/api/v1/posts/
### Ответ:
```
[
    {
        "id": 1,
        "author": "newuser",
        "text": "Тестовый пост 1",
        "pub_date": "2023-01-27T15:30:18.759679Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "newuser",
        "text": "Тестовый пост 2",
        "pub_date": "2023-01-27T15:30:38.460901Z",
        "image": null,
        "group": 1
    }
]
```
### Пример просмотра списка групп:
### Запрос GET http://ip:port/api/v1/groups/
### Ответ:
```
[
    {
        "id": 1,
        "title": "Group 1",
        "slug": "Group1",
        "description": "Тестовая группа 1"
    },
    {
        "id": 2,
        "title": "Group 2",
        "slug": "Group2",
        "description": "Тестовая группа 2"
    }
]
```
