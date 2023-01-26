# api_final_yatube - (доработанный проект api_yatube) REST API для проекта Yatube

Стек: Python 3.9, Django 3, Django REST Framework 3

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

API доступен только аутентифицированным пользователям. В проекте аутентификация осуществляется по токену TokenAuthentication (Реализована аутентификация по JWT-токену).

При запуске проекта, по адресу http://127.0.0.1:8000/redoc/ доступна документация в формате Redoc для API Yatube.

Для аутентифицированный пользователя доступно изменение и удаление своего контента, для гостевого пользователя предоставлено чтение. При попытке изменить чужие записи возвращается 403 Forbidden.

В проекте доступны эндпоинты:
	- api/v1/api-token-auth/ (POST): передаём логин и пароль, получаем токен.
	- api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
	- api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по его идентификатору.
	- api/v1/groups/ (GET): получаем список всех групп.
	- api/v1/groups/{group_id}/ (GET): получаем информацию о группе по её идентификатору.
	- api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с идентификатором post_id или создаём новый, указав идентификатор поста, который необходимо прокомментировать.
	- api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по его идентификатору у поста с идентификатором post_id.

В ответ на запросы POST, PUT и PATCH ваш API возвращает объект, который был добавлен или изменён.
