# api_final_yatube - (доработанный проект api_yatube) REST API для проекта Yatube

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

При запуске проекта, по адресу http://127.0.0.1:8000/redoc/ доступна документация в формате Redoc для API Yatube.

Для аутентифицированный пользователя доступно изменение и удаление своего контента, для гостевого пользователя предоставлено чтение. При попытке изменить чужие записи возвращается 403 Forbidden.

Примеры запросов:

Пример запроса на создание нового пользователя:
Запрос: POST http://127.0.0.1:8000/api/v1/users/
{
    "username": "newuser",
    "password": "Password1"
}
Ответ:
{
    "email": "",
    "username": "newuser",
    "id": 2
}

Пример запроса токена зарегестрированного пользователя:
Запрос POST http://127.0.0.1:8000/api/v1/jwt/create/
{
    "username": "newuser",
    "password": "Password1"
}
Ответ:
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NDg0OTUyMCwianRpIjoiOGJhYzA1MDkyOTA5NDJmY2FjYTZkZTI4ZGQ4OTlmODEiLCJ1c2VyX2lkIjoyfQ.w.....",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0ODQ5NTIwLCJqdGkiOiI2YzhjMDM3NTU0Njg0NjdmOWViOTU0MWUzYjg3YmZiMiIsInVzZXJfaWQiOjJ9.1....."
}