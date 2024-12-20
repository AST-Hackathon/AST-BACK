# Backend сайта для ACT

<details>
<summary>

## Описание проекта

</summary>

### Требования

***Создать промо-сайта для книжной серии Самая удивительная книга с объемными картинками.<br>
Создание промо-сайта для книжной серии «Самая удивительная книга с объемными картинками», который будет способствовать 
продвижению и популяризации этих книг среди целевой аудитории – родителей и детей. 
<br>Сайт должен быть привлекательным, информативным и интерактивным, чтобы привлечь внимание и заинтересовать 
потенциальных покупателей.***

</details>

<details>
<summary>

### Целевая аудитория

</summary>

___


*Родители и их дети, в основном мамы.*


</details>

___
<details>
<summary>

## Члены Команды»

</summary>

| №  | ФИО                    | Должность            | Никнейм в телеграмме | Ссылка на проекты             |
|----|------------------------|----------------------|----------------------|-------------------------------|
| 1  | Екатерина Попова       | Тимлид               |                      |                               |
| 2  | Кочеткова Даниэла      | UX/UI дизайнер       | @                    |                               |
| 3  | Щербакова Марина       | UX/UI дизайнер       | @                    |                               |
| 4  | Нуретдинова Мариам     | UX/UI дизайнер       | @                    |                               |
| 5  | Кузьменко Максим       | UX/UI дизайнер       | @                    |                               |
| 6  | Ефаров Никита          | UX/UI дизайнер       | @                    |                               |
| 7  | Корышева Юлия          | UX/UI дизайнер       | @                    |                               |
| 8  | Полякова Юлия          | Графический дизайнер | @                    |                               |
| 9  | Захарова Анастасия     | Графический дизайнер | @                    |                               |
| 10 | Касимова Алина         | Графический дизайнер | @                    |                               |
| 11 | Жильникова Дарья       | Графический дизайнер | @                    |                               |
| 12 | Турскова Надежда       | Графический дизайнер | @                    |                               |
| 13 | Шитова Алена           | Графический дизайнер | @                    |                               |
| 14 | Болат Мирас            | 3D дизайнер          | @                    |                               |
| 15 | Раевских Валерия       | Motion design        | @                    |                               |
| 16 | Ромашко Алена          | Motion design        | @                    |                               |
| 17 | Акбатыров Александр    | Тестировщик          | @                    |                               |
| 18 | Ломакиина Марина       | Тестировщик          | @                    |                               |
| 19 | Бандарюк Екатерина     | Frontend разработчик | @                    |                               |
| 20 | Салмина София          | Frontend разработчик | @                    |                               |
| 21 | Адель Давлетшин        | Backend разработчик  | @                    |                               |
| 22 | Александрова Екатерина | Backend разработчик  | @                    |                               |
| 23 | Антон Зайцев           | Backend разработчик  | @BlackMarvel         | https://github.com/Hashtagich |

</details>

___

<details>
<summary>

## Запуск проекта

</summary>

___

### 1. Клонирование репозиторий

```bash
git clone https://github.com/AST-Hackathon/AST-BACK.git
```

### 2. Установка переменных окружения

***В корне проекта, на одном уровне с папкой backend, заполняем файл env.template и переименовываем его в .env или 
просто создаём файл .env и заполняем его***

 ```bash
    #redis
    REDIS_ENDPOINT=redis://localhost:6379
    REDIS__PORT = 6379
    
    # database protocol.py
    DB__HOST=postgres
    DB__PORT=5432
    DB__NAME=postgres
    DB__USER=postgres
    DB__PASS=postgres
    DB__DB_POOL_SIZE=5
    DB__DB_MAX_OVERFLOW=10
    DB__DB_URL=postgres
    DB__DB_PORT=5432

    #src protocol.py
    BACKEND_SERVER__PORT=8080
    BACKEND_SERVER__HOST=0.0.0.0
    BACKEND_SERVER__WORKERS=1
    BACKEND_SERVER__DEBUG=False
    BACKEND_SERVER__HOST_PORT=8080
    BACKEND_SERVER__SERVER_PORT=8080
    BACKEND_SERVER__SECRET_KEY=32198
    BACKEND_SERVER__SAVE_PATH=research_data
    BACKEND_SERVER__METHODS=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"]
    BACKEND_SERVER__HEADERS=["*"]
    BACKEND_SERVER__ALGORITHM="HS256"
    BACKEND_SERVER__SERVER_HOST="localhost"
    BACKEND_SERVER__REFRESH_TOKEN_EXPIRE_DAYS=30
    BACKEND_SERVER__ACCESS_TOKEN_EXPIRE_MINUTES=60
    
    #api protocol.py
    APP_PREFIX=/api
 ```

### 3. Сборка и запуск контейнеров
***Для запуска на прод-сервере используем следующую команду.***
```bash
docker-compose up --build -d
```

***Для запуска на стадии разработки используем следующую команду.***
```bash
docker-compose -f debug.yml up -d
```

### 4. Запуск backend
***Перейти в папку backend***
```bash
cd backend
```

***Запускаем backend***
```bash
python run.py  
```

</details>

___

### API

***URL***

http://localhost:8080

***Страница Админ панели***

<code>{{URL}}/admin/</code>

***Страница с документацией по API***

<code>{{URL}}/swagger/</code>

***API Книг***
<details>
<summary><code>GET/api/book/all/</code></summary>

*Получение списка всех книг кроме текущего, на странице которого находимся. Надо передать её id.
<br>Пример запроса http://localhost:8080/api/book/all/?id=1
<br>Если необходимо получить список всех книг без исключения, то достаточно передать несуществующий id т.е. свободный.*

```
[
  {
    "id": 0,
    "title": "string",
    "photo_preview": "string"
  }
]
```

</details>
<details>
<summary><code>GET/api/book/{id}/</code></summary>

*Получение конкретной книги по её id.
<br>Пример запроса http://localhost:8080/api/book/2*

```
{
  "id": 0,
  "title": "string",
  "description": "string",
  "avatar": "string",
  "url": "https://example.com/",
  "fotos": [
    {
      "foto": "string"
    }
  ],
  "authors": [
    {
      "title": "string",
      "foto": "string"
    }
  ]
}
```

</details>


***API Отзывов***

<details>
<summary><code>GET/api/feedback/all/</code></summary>

*Получение списка всех отзывов.*

```
[
  {
    "author": "string",
    "text": "string"
  }
]
```

</details>
<details>
<summary><code>POST/api/feedback/</code></summary>

*Создание отзыва пользователем.*

```
{
  "author": "string",
  "text": "string"
}
```

</details>


***API Темы главной страницы***

<details>
<summary><code>GET/api/theme_page/</code></summary>

*Получение первой активной темы для главной страницы. Возвращается первая тема, где статус is_active = True*

```
{
  "title": "string",
  "header": "string",
  "foto_1": "string",
  "foto_2": "string",
  "foto_3": "string",
  "foto_4": "string",
  "foto_5": "string",
  "foto_6": "string",
  "foto_7": "string",
  "foto_8": "string",
  "foto_9": "string",
  "foto_10": "string",
  "foto_11": "string",
  "footer_bg": "string",
  "footer_logo": "string"
}
```

</details>

___

<details>
<summary>

## Дополнительная информация

</summary>

+ ***Дизайн на биханс — .***

</details>