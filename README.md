Описание:
API для Yatub представляет собой социальную сеть, в которой реализованы следующие возможности:
публиковать/изменять/удалять записи
комментировать записи
подписываться или отписываться от авторов


Стек технологий:
Python 3.7.0
Django 3.2.16
DRF
JWT + Djoser


Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:
git clone https://github.com/Lenger1117/api_final_yatube
cd api_final_yatube


Cоздать и активировать виртуальное окружение:

python -m venv venv - создание ВО
или python3 -m venv venv
venv\Scripts\activate.bat - для Windows
source venv/bin/activate - для Linux и MacOS

Установить зависимости из файла requirements.txt:

python -m pip install --upgrade pip
или python3 -m pip install --upgrade pip
pip install -r requirements.txt


Выполнить миграции:

python manage.py migrate
или python3 manage.py migrate


Создать суперпользователя:

python manage.py createsuperuser
или python3 manage.py createsuperuser


Запустить проект:

python manage.py runserver
или python3 manage.py runserver


Примеры запросов к API:
Получить список всех постов (GET):

http://127.0.0.1:8000/api/v1/posts/
Получить определенный пост (GET):

http://127.0.0.1:8000/api/v1/posts/1/
Получить коментарии определенного поста (GET):

http://127.0.0.1:8000/api/v1/posts/1/comments/
Получить список всех групп (GET):

http://127.0.0.1:8000/api/v1/groups/
Создать новый пост (POST):

(Требуется аутентификация)

http://127.0.0.1:8000/api/v1/posts/
в body

{
"text": "string",
"image": "string",
"group": 0
}
