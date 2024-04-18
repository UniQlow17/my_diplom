## Описание
Данный проект является моей выпускной квалификационной работой.

## Как развернуть приложение
### Первый вариант
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

3. Выполните миграции и загрузите правила из файла rules.json:
   ```
   python manage.py migrate
   python manage.py loaddata rules.json
   ```

4. Создайте суперпользователя:
   ```
   python manage.py createsuperuser
   ```

5. Запустите приложение:
   ```
   python manage.py runserver
   ```

### Второй вариант
Нужно выполнить следующие шаги:

1. Скачать файл docker-compose.prod.yml из репозитория

2. Создайте файл .env:
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
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.yandex.ru
   EMAIL_HOST_USER=your_mail@yandex.ru
   EMAIL_HOST_PASSWORD=your_password
   EMAIL_PORT=465
   EMAIL_USE_SSL=True
   ```

3. Поднять сборку контейнеров:
   ```
   docker-compose up
   ```

4. Выполнить в контейнере backend следующие команды:
   * Создать суперпользователя:
     ```
     python manage.py createsuperuser
     ```
   * Загрузите правила из файла rules.json:
      ```
      python manage.py loaddata rules.json
      ```

## Стек технологий
В данном проекте использовались такие технологии как:

* Django
* python-docx

## Контакты
* Автор: Елшин Александр
* Telegram: @UniQlow21