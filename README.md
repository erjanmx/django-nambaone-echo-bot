# Django Namba-One Bot

[![Build Status](https://travis-ci.org/erjanmx/django-namba-one-bot.svg?branch=master)](https://travis-ci.org/erjanmx/django-namba-one-bot)

Пример бота для NambaOne написанного с использованием Django и библиотеки [python-nambaone-bot](https://github.com/erjanmx/python-nambaone-bot) для работы с BotAPI

Бот настроен для запуска на серверах Heroku.

## Запуск

Перед запуском необходимо создать бота в https://dashboard.namba1.co

#### Настройки приложения

Вне зависимости от типа запуска необходимо указать следующие переменные окружения

- SECRET_KEY
- APP_TOKEN
- NAMBA_ONE_API_TOKEN

### Heroku

1. Прочитать [документацию](https://devcenter.heroku.com/articles/git) по запуску на heroku 
2. `heroku create`
3. `git push heroku master`
4 .  указать адрес запущенного heroku приложения в настройках бота на https://dashboard.namba1.co

### Локальный запуск

1. склонировать репозиторий

`git clone https://github.com/erjanmx/django-namba-one-bot.git`

2. создать и войти в виртуальное окружение

`python -m venv venv && source venv/bin/activate`

3. установить зависимости

`pip install -r requirements.txt`

4. запустить django или cherrypy вебсервер

`python manage.py runserver` или `python serve.py`

5. указать IP адрес запущенного приложения в настройках бота на https://dashboard.namba1.co
