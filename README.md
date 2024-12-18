# test_api

API для управления данными генетических тестов животных.

## Запуск проекта
1. Установите зависимости: `pip install -r requirements.txt`.
2. Настройте базу данных в `settings.py`.
3. Примените миграции: `python manage.py migrate`.
4. Запустите сервер: `python manage.py runserver`.

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