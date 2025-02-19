# Genetic_test_api

Genetic_test_api — это RESTful API для сохранения данных генетических тестов животных и вычисления агрегированной статистики. API поддерживает добавление данных, просмотр записей и вычисление статистики по видам животных.

## Требования
* Python 3.12
* Django 5.0
* PostgreSQL
* Docker and Docker Compose (для запуска через Docker Compose)

## Запуск проекта
1. Клонируйте репозиторий.
2. Установите зависимости: `pip install -r requirements.txt`.
3. Настройте базу данных в `settings.py`.
4. Настройте переменные окружения:

Создайте файл .env в корневой директории проекта и добавьте следующие переменные:
```
SECRET_KEY=your_secret_key
POSTGRES_DB=your_database
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=db
POSTGRES_PORT=5433
```

5. Примените миграции: `python manage.py migrate` или `make migrate`
6. Запустите сервер: `python manage.py runserver` или `make dev`

Приложение будет доступно по адресу http://127.0.0.1:8000/.

## Установка и запуск проекта через Docker Compose

1. Клонируйте репозиторий.
2. Создайте файл .env как указано выше.
3. Запустите Docker Compose:
```
docker-compose up --build
```
4. Выполните миграции внутри контейнера:
```
docker-compose run --rm web-app sh -c "python manage.py migrate"
```
Docker Compose создаст и запустит контейнеры для приложения и базы данных. Приложение будет доступно по адресу http://127.0.0.1:8000


## Эндпоинты
1. **POST /tests**: Добавить тест.
2. **GET /tests?species={species}**: Получить записи по виду животного.
3. **GET /statistics**: Получить статистику.

## Примеры запросов
### POST /tests
```json
{
  "animal_name": "Буренка",
  "species": "корова",
  "test_date": "2023-11-18",
  "milk_yield": 28.5,
  "health_status": "good"
}
```

### GET /tests
```json
[
  {
    "id": 1,
    "animal_name": "Буренка",
    "species": "корова",
    "test_date": "2023-11-18",
    "milk_yield": 28.5,
    "health_status": "good"
  }
]
```

### GET /statistics
```json
{
  "statistics": [
    {
      "species": "корова",
      "total_tests": 1,
      "avg_milk_yield": 28.5,
      "max_milk_yield": 28.5,
      "good_health_percentage": 100
    }
  ]
}
```
