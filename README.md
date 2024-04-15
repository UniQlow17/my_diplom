## Описание
Данный проект является моей выпускной квалификационной работой.

## Как запустить
Нужно выполнить следующие шаги:

1. Склонируйте репозиторий:
   ```
   git clone https://github.com/UniQlow17/my_diplom.git
   ```

2. Создайте виртуальное окружение и установите зависимости:
   ```
   cd my_diplom/backend
   python3.9 -m venv venv
   source venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Создайте файл .env:
   ```
   touch .env
   nano .env
   ```
   ```
   #.env.example
   POSTGRES_ENGINE=django.db.backends.postgresql
   POSTGRES_DB=postgres_db
   POSTGRES_USER=user
   POSTGRES_PASSWORD=password
   DB_HOST=db
   DB_PORT=5432
   SECRET_KEY=secret_key
   DEBUG=False
   ALLOWED_HOSTS=127.0.0.1, localhost
   ```

4. Выполните миграции и загрузите правила из файла rules.json:
   ```
   python manage.py migrate
   python manage.py loaddata rules.json
   ```

5. Создайте суперпользователя:
   ```
   python manage.py createsuperuser
   ```

6. запустите приложение:
   ```
   python manage.py runserver
   ```

## Стек технологий
В данном проекте использовались такие технологии как:

* Django
* python-docx

## Контакты
* Автор: Елшин Александр
* Telegram: @UniQlow21