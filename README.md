# Product Catalog API

Backend-сервис для управления каталогом товаров с системой регистрации пользователей и ограничением количества запросов (Rate Limiting). Реализована аутентификация через JWT и полнофункциональный CRUD для товаров.

### Запуск

1. Клонируйте репозиторий и перейдите в директорию проекта:
   ```bash
   git clone https://github.com/youruser/product-catalog-api.git
   cd product-catalog-api
   ```

2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Настройте `.env` файл (создайте его на основе примера) и запустите сервер:
   ```bash
   uvicorn main:app --reload
   ```

### Пример

Для работы с API используйте Swagger UI по адресу: `http://127.0.0.1:8000/docs`

Примерный сценарий:
1. `POST /auth/register` — регистрация нового пользователя.
2. `POST /auth/login` — получение JWT токена.
3. `GET /products` — получение списка товаров (с использованием токена в Header: `Authorization: Bearer <token>`).

### Тесты

Для запуска автоматических тестов используйте:
```bash
pytest -q
```
