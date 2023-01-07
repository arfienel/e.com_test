Запуск и тестирование
1. Скачать сам проект 
2. Перейти в директорию проекта
3. ```sudo docker-compose up --build```
4. После того как запустится, узнать id контейнера app c помощью команды ```docker ps```
5. ```docker exec -it {id того контейнера} bash```
6. запустить тесты ```python manage.py test forms_validator```
