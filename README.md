# API: Yatube Cоциальная сеть 

![example workflow](https://github.com/aVeter77/api_final_yatube/actions/workflows/main.yml/badge.svg)

Социальная сеть с возможность создать учетную запись, публиковать записи, подписываться на любимых авторов, комментировать и отмечать понравившиеся записи.

Полное описание API [http://api.yatube.aveter77.site/redoc/](http://api.yatube.aveter77.site/redoc/)

Все эндпоинты [http://api.yatube.aveter77.site/api/v1/](http://api.yatube.aveter77.site/api/v1/)

Образ на [Dockerhub](https://hub.docker.com/r/aveter77/yatube_api/tags)

## Алгоритм регистрации пользователей
Пользователь отправляет POST-запрос на эндпоинт `/api/v1/jwt/create/` с параметрами
```
{
  "username": "string",
  "password": "string"
}
```
В ответе на запрос приходит:
- `refresh` для обновления токена. Для этого отправьте POST-запрос на `/auth/jwt/create/`, в теле запроса в поле `refresh` передайте refresh-токен;
- `access` токен, который надо будет передавать в заголовке каждого запроса, в поле `Authorization`. Перед самим токеном должно стоять ключевое слово `Bearer` и пробел.

## Технологии
- [Python 3.7](https://www.python.org/)
- [Django 2.2.16](https://www.djangoproject.com/)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/)
- [gunicorn 20.0.4](https://pypi.org/project/)
- [nginx 1.21.3](https://nginx.org/ru/)
- [Docker 20.10.17](https://www.docker.com/)
- [Docker Compose 2.9](https://docs.docker.com/compose/)

## Запуск

Установите переменные среды, как в `.env.example`.
### Docker
```
cd infra/
docker-compose up -d
```
После запуска выполните команды:
```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

## Заполнение базы начальными данными
```
cd infra/
cat fixtures.json | docker-compose exec -T web python manage.py loaddata --format=json -
```

## Примеры запросов:

**Получение всех публикаций**
```
[GET] /api/v1/posts/
```
```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": 
    [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
**Создать публикацию**
```
[POST] /api/v1/posts/
```
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

**Получение комментариев**
```
[GET] /api/v1/posts/{post_id}/comments/
```
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

**Добавление комментария**
```
[POST] /api/v1/posts/{post_id}/comments/
```
```
{
  "text": "string"
}
```
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

## Автор
Александр Николаев

## Лицензия
MIT
