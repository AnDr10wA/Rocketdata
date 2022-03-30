# Rocketdata

Для реализации сервиса используется следующие библиотеки Python:
Django 
Scrapy 
PorstgreSQL - база данных 

Работа сервиса:
 Django запускает поука Scrapy, который собирает данные. Полученная 
информация сохраняется в базу данных PostgreSQL.
Для изменения исходной ссылки для поука необходимо изменить значения переменной
start_urls в файле scraper/scraper/spiders/userdata


Запуск проекта:

1. Клонировать проект из github
2. Выполнить команду pip install -r requirements.txt
3. Перейти в директорию с файлом manage.py 
4. Сделать миграции: ./manage.py makemigrations
./manage.py migrate
5. Для запуска поука выполнить команду ./manage.py crawl
6. Создать админа ./manage.py createsuperuser
7. Запустить django проект ./manage.py runserver
8. В браузере для получения API перейти по следующим ссылкам:

localhost:8000/gitlink/project - апи получения ссылок на страницы пользователей
localhost:8000/gitlink/repos/<str:project> - апи получения репозиториев пользователя
localhost:8000/gitlink/stats/celery - апи получения общей статистики
localhost:8000/gitlink/statsone/<str:project> -апи получения статистики по одному пользователю
Вместо <str:project> - указать имя проекта