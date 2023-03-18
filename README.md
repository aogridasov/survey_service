# Сервис для опросов

### Команда наполняет БД тестовыми опросами:
Парсит созданный ChatGPT файл с опросами (csv)
```
python manage.py populate
``` 
 


### Библиотеки
Подробнее в requirements.txt
```
Django==2.2
django-nested-inline==0.4.6
``` 

### Деплой
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:aogridasov/survey_service.git
``` 
Установить и активировать виртуальное окружение:
``` 
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
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
Создать администратора:
```
python3 manage.py createsuperuser
```
