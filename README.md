# Кейс-задача № 3 — Приветствие на Django

Учебная практика. Направление 02.03.03, профиль «Разработка ПО (Full-stack)».

## Что делает

Вводишь имя в поле на главной странице и нажимаешь «Отправить» — имя
сохраняется в базу данных, и страница показывает персональное приветствие.
Если поле пустое (или в нём только пробелы) — выводится ошибка, ничего
не сохраняется.

## Стек

Python 3.12, Django 6.1, SQLite.

## Как запустить

Нужен Python 3.12 или новее — Django 6 на более старых версиях не работает.
Проверить: `python3 -V`

Создаём виртуальное окружение и ставим Django:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Создаём базу данных и запускаем сервер:

```bash
python manage.py migrate
python manage.py runserver
```

Открыть в браузере: `http://127.0.0.1:8000/`

Остановить сервер — `Ctrl+C`, выйти из окружения — `deactivate`.
При следующем запуске окружение нужно активировать снова:
`source .venv/bin/activate`.

## Как запустить тесты

```bash
python manage.py test greeter -v 2
```

## Что реализовано

- Форма с полем «имя» и кнопкой «Отправить»
- Модель `Visitor` с одним полем `name`
- Имя сохраняется в базу и выводится приветствие
- Обработка пустого поля (и поля из одних пробелов)
- Стилизация через CSS
- Защита от CSRF (стандартный `CsrfViewMiddleware` + `{% csrf_token %}` в форме)

## Структура проекта

```
.
├── manage.py
├── requirements.txt
├── greeter_project/       # настройки проекта
│   ├── settings.py
│   └── urls.py
└── greeter/                # приложение
    ├── models.py            # модель Visitor
    ├── views.py              # обработка формы
    ├── urls.py
    ├── admin.py
    ├── tests.py
    ├── templates/greeter/home.html
    └── static/greeter/style.css
```
