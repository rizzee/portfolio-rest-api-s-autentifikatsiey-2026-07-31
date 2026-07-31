# LEARN: REST API с аутентификацией

## 1. Что сделали
- Реализовали backend для каталога товаров на FastAPI
- Добавили модуль аутентификации (JWT) с регистрацией/логином
- Настроили rate-limiting для API
- Организовали структуру проекта: роутеры, модели, схемы
- Использовали SQLAlchemy для работы с БД

## 2. Что разобрать
- **FastAPI Dependency Injection** - как работает внедрение зависимостей
- **JWT-токены** - структура, срок жизни, безопасность
- **Rate Limiting алгоритмы** (токенный bucket)
- **Pydantic схемы** - валидация данных
- **Асинхронные запросы к БД**

## 3. Ссылки
- [FastAPI документация](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/14/orm/)
- [JWT RFC](https://tools.ietf.org/html/rfc7519)
- [Rate Limiting стратегии](https://cloud.google.com/architecture/rate-limiting-strategies-techniques)

## 4. Вопросы
1. Как работает механизм верификации JWT на стороне сервера?
2. Чем отличается `@app.middleware` от `@app.middleware("http")`?
3. Как организована связь между Pydantic схемами и SQLAlchemy моделями?
4. Какие уязвимости есть у JWT и как их избежать?
5. Почему rate-limiting лучше делать через middleware, а не в роутах?
6. Как тестировать API с аутентификацией?
7. Какие альтернативы JWT можно использовать?
