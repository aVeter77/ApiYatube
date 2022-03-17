# Проект: Cоциальная сеть 
## _API для публикации личных дневников и подписок на второв_

![Yandex Practicum](https://i.ibb.co/3F7pPBj/logo.png)

![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master) ![License](https://img.shields.io/apm/l/vim-mode)

Социальная сеть с возможность создать учетную запись, публиковать записи, подписываться на любимых авторов и отмечать понравившиеся записи.

## Технологии

- Python 3.7
- Django 2.2.19

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/aVeter77/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
cd yatube_api
python3 manage.py runserver
```

### Вывод всех эндпоинтов:
```
[GET] /api/v1/
```
```
{
    "posts": "http://127.0.0.1:8000/api/v1/posts/",
    "follow": "http://127.0.0.1:8000/api/v1/follow/",
    "groups": "http://127.0.0.1:8000/api/v1/groups/"
}
```
### Примеры команд:

#### Вывод всех постов
```
[GET] /api/v1/posts/
```
#### Пример ответа
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
#### Добавить новый пост
```
[POST] /api/v1/posts/
```
#### Пример ответа
```
{

    "text": "string",
    "image": "string",
    "group": 0

}
```

### Автор:
```
Александр Николаев
```
