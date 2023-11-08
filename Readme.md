Дипломный проект. Сайт медицинской компании

Клонировать репозиторий

Для запуска приложения необходимо настроить виртуальное окружение и установить все необходимые зависимости с помощью команд:
Команда для Windows: 
1- python -m venv venv 
2- venv\Scripts\activate.bat 
3- pip install -r requirement.txt


Создать БД:
1- Выполнить вход sudo -U postgres psql 
2- Создать базу данных с помощью следующей команды: CREATE DATABASE bd_name; 
3- Выйти \q

Применить миграции: 
1- python manage.py makemigrations 
2- python manage.py migrate

Для работы с переменными окружениями необходимо заполнить файл .env на основе .env.sample

Для создания администратора (createsuperuser)

заполните поля email, PASSWORD. users/management/commands/ccsu.py 

Команда для Windows - python manage.py ccsu
python manage.py loaddata db.json - для загрузки информации для базы данных

Для запуска приложения: Команда для Windows:

python manage.py runserver

Доступ к сайту осуществляется по IP-адресу: http://127.0.0.1:8000/

Доступ к административной панели: http://127.0.0.1:8000/admin/