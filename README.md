<h3>Описание:</h3>
<br>
API для Yatub представляет собой социальную сеть, в которой реализованы следующие возможности:
публиковать/изменять/удалять записи
комментировать записи
подписываться или отписываться от авторов

<h3>Стек технологий:</h3>
<ul>
<li>Python 3.7.0</li>
<li>Django 3.2.16</li>
<li>DRF</li>
<li>JWT + Djoser</li>
</ul>


<h3>Как запустить проект:</h3>

Клонировать репозиторий и перейти в него в командной строке:
<br>
git clone https://github.com/Lenger1117/api_final_yatube
<br>
cd api_final_yatube


<h3>Cоздать и активировать виртуальное окружение:</h3>

python -m venv venv - создание ВО
<br>
или python3 -m venv venv
<br>
venv\Scripts\activate.bat - для Windows
<br>
source venv/bin/activate - для Linux и MacOS
<br>

<h3>Установить зависимости из файла requirements.txt:</h3>

python -m pip install --upgrade pip
<br>
или python3 -m pip install --upgrade pip
<br>
pip install -r requirements.txt


<h3>Выполнить миграции:</h3>

python manage.py migrate
<br>
или python3 manage.py migrate


<h3>Создать суперпользователя:</h3>

python manage.py createsuperuser
<br>
или python3 manage.py createsuperuser


<h3>Запустить проект:</h3>

python manage.py runserver
<br>
или python3 manage.py runserver


<h3>Примеры запросов к API:</h3>

Получить список всех постов (GET):
http://127.0.0.1:8000/api/v1/posts/

<table style="text-align:right">
  <tr>
    <th>Ответ</th>
  </tr>
  <tr>
    <td>
      200 OK
      <br><br>
      [
      <br>
    {
      <br>
        "id": 1,
      <br>
        "author": "lady",
      <br>
        "text": "string",
      <br>
        "pub_date": "2023-05-16T15:42:11.134539Z",
      <br>
        "image": null,
      <br>
        "group": null
      <br>
    },
      <br>
    {
      <br>
        "id": 2,
      <br>
        "author": "lady",
      <br>
        "text": "string2",
      <br>
        "pub_date": "2023-05-16T15:50:17.318555Z",
      <br>
        "image": null,
      <br>
        "group": null
      <br>
    }
      <br>
]
    </td>
  </tr>
</table>

Получить определенный пост (GET):
http://127.0.0.1:8000/api/v1/posts/1/

Получить коментарии определенного поста (GET):
http://127.0.0.1:8000/api/v1/posts/1/comments/

Получить список всех групп (GET):
http://127.0.0.1:8000/api/v1/groups/

Создать новый пост (POST)(требуется аутентификация):
http://127.0.0.1:8000/api/v1/posts/
<table style="text-align:right">
  <tr>
    <th>Запрос</th>
    <th>Ответ</th>
  </tr>
  <tr>
    <td>
      {
      <br>
      "text": "string"
      <br>
      }
    </td>
    <td>
      201 Created
      <br><br>
      {
      <br>
    "id": 1,
      <br>
    "author": "author",
      <br>
    "text": "string",
      <br>
    "pub_date": "2023-05-16T15:42:11.134539Z",
      <br>
    "image": null,
      <br>
    "group": null
      <br>
      }
    </td>
  </tr>
</table>
