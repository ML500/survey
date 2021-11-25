## Survey
### Техническое задание
**Задача:** Cпроектировать и разработать API для системы опросов пользователей.

#### Функционал для администратора системы:

- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

#### Функционал для пользователей системы:

- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

**Использовать следующие технологии:** Django 2.2.10, Django REST framework.

### В проекте использованны
- Django==2.2.10
- djangorestframework==3.12.4
- djangorestframework-simplejwt==5.0.0

### Установка
1. Создайте и зайдите в папку где будете разворачивать приложение
2. Склонируйте приложение с 
  - https://github.com/ML500/survey
3. Создайте в вирутальное окружение 
  - python3 -m virtualenv -p python3 venv
4. Активируйте вирутальное окружение 
  - . venv/bin/activate
5. Установите зависимости
  - pip install -r requirements.txt
6. Сделайте миграции
  - python manage.py migrate
### API Документация
- **Авторизация (получение access и refresh токенов)**
   - Path: [http://localhost:8000/api/token/](http://localhost:8000/api/token/)
   - Method: GET
   - Body
      - username: text
      - password: text
- **Получение access токена**
   - Path: [http://localhost:8000/api/token/refresh/](http://localhost:8000/api/token/refresh/)
   - Method: POST
   - Body
      - access: token
- **Список опросов**
   - Path: [http://localhost:8000/api/v1/survey/get](http://localhost:8000/api/v1/survey/get)
   - Method: GET
   - Header(Autorization): Access Token
- **Один опрос**
   - Path: [http://localhost:8000/api/survey/[survey_id]](http://localhost:8000/api/survey/[survey_id])
   - Method: GET
   - Header(Autorization): Access Token
   - URL Parameters: survey_id
- **Создание опроса**
   - Path: [http://localhost:8000/api/survey/post](http://localhost:8000/api/survey/post)
   - Method: POST
   - Header(Autorization): Access Token
   - Body
      - title: text
      - describe: text
      - start_date: date(YYYY-MM-DD)
      - end_date: date(YYYY-MM-DD)
- **Изменение опроса**
   - Path: [http://localhost:8000/api/survey/patch/[survey_id]](http://localhost:8000/api/survey/patch/[survey_id])
   - Method: PATCH
   - Header(Autorization): Access Token
   - URL Parameters: survey_id
   - Body
      - title: text
      - describe: text
      - start_date: date(YYYY-MM-DD)
      - end_date  : date(YYYY-MM-DD)
- **Удаление опроса**
   - Path: [http://localhost:8000/api/survey/delete/[survey_id]](http://localhost:8000/api/survey/delete/[survey_id])
   - Method: DELETE
   - Header(Autorization): Access Token
   - URL Parameters: survey_id
- **Список активных опросов**
   - Path: [http://localhost:8000/api/v1/survey/get_active](http://localhost:8000/api/v1/survey/get_active)
   - Method: GET
   - Header(Autorization): Access Token
- **Создание вопроса**
   - Path: [http://localhost:8000/api/question/post](http://localhost:8000/api/question/post)
   - Method: POST
   - Header(Autorization): Access Token
   - Body
      - text: text
      - type (text, one_option, plural_option)
      - survey: id
- **Изменение вопроса**
   - Path: [http://localhost:8000/api/question/patch/[question_id]](http://localhost:8000/api/question/patch/[question_id])
   - Method: PATCH
   - Header(Autorization): Access Token
   - URL Parameters: survey_id
   - Body
      - text: text
      - type (text, one_option, plural_option)
      - survey: id 
- **Удаление вопроса**
   - Path: [http://localhost:8000/api/question/delete/[question_id]](http://localhost:8000/api/question/delete/[question_id])
   - Method: DELETE
   - Header(Autorization): Access Token
   - URL Parameters: question_id
- **Создание варианта вопроса**
   - Path: [http://localhost:8000/api/option/post](http://localhost:8000/api/option/post)
   - Method: POST
   - Header(Autorization): Access Token
   - Body
      - text: text
      - question: id
- **Изменение варианта вопроса**
   - Path: [http://localhost:8000/api/option/patch/[question_id]](http://localhost:8000/api/option/patch/[option_id])
   - Method: PATCH
   - Header(Autorization): Access Token
   - URL Parameters: survey_id
   - Body
      - text: text
      - question: id
- **Удаление варианта вопроса**
   - Path: [http://localhost:8000/api/option/delete/[option_id]](http://localhost:8000/api/option/delete/[option_id])
   - Method: DELETE
   - Header(Autorization): Access Token
   - URL Parameters: option_id
- **Ответ на вопрос**
   - Path: [http://localhost:8000/api/answer/post](http://localhost:8000/api/answer/post)
   - Method: POST
   - Header(Autorization): Access Token
   - Body
      - user: id
      - text: text
      - survey: id
      - question: id
      - option: id
- **Детальный список ответов по определенному пользователю**
   - Path: [http://localhost:8000/api/get_user_answer/[answer_id]](http://localhost:8000/api/answer/[answer_id])
   - Method: GET
   - Header(Autorization): Access Token
   - URL Parameters: answer_id
