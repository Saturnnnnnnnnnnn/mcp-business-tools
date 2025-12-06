````markdown
# MCP Business Tools (MVP)

Версия: 0.1.0дав

Бэкенд для демонстрации автоматизации тестирования и утилит команды QA с интеграцией AI (LLM).

---

## Что делает проект

- Генерирует тест-кейсы (ручные и API) автоматически через LLM.
- Проверяет тесты на соответствие стандартам (Allure, AAA-паттерн).
- Создает события в календаре (демо или через Google Calendar).
- Отправляет письма (демо, требует SMTP).
- Возвращает тестовые данные, например курсы валют (демо).

Всё доступно через веб-API. Можно тестировать через Swagger UI или HTTP-запросы.

---

## Требования

- Python 3.10+
- pip
- venv (рекомендовано)

---

## Установка

```bash
git clone https://github.com/Saturnnnnnnnnnnn/mcp-business-tools.git
cd mcp-ready-project-full
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## Настройки внешних сервисов

Файл `.env` уже включён в корень проекта как `.env.example`. Пример содержимого:

```dotenv
# Сервер
HOST=0.0.0.0
PORT=8000
REQUEST_TIMEOUT=15

# SMTP (если нужно)
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=user@example.com
SMTP_PASSWORD=yourpassword
FROM_EMAIL=user@example.com

# LLM для генерации тестов
EVOLUTION_API_TOKEN=ваш_ключ
EVOLUTION_API_URL=https://foundation-models.api.cloud.ru/v1

# Google Calendar (если нужно)
GOOGLE_CALENDAR_API_KEY=ваш_ключ
GOOGLE_CALENDAR_CALENDAR_ID=primary
```

> Без LLM-токена генерация тестов через AI работать не будет. SMTP и календарь можно оставить пустыми для демонстрации.

---

## Запуск

```bash
python3 -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

* API: `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`
* Health check: `http://127.0.0.1:8000/health`

---

## Примеры запросов

### 1. Генерация ручных тестов через AI

```bash
curl -X POST http://127.0.0.1:8000/generate/manual-tests \
-H "Content-Type: application/json" \
-d '{"product_description":"Demo product","owner":"QA Team","feature":"Login","count":3}'
```

### 2. Генерация API-тестов по OpenAPI

```bash
curl -X POST http://127.0.0.1:8000/generate/api-tests \
-H "Content-Type: application/json" \
-d '{"openapi_url":"https://demo.openapi.url/spec.json"}'
```

### 3. Проверка кода на соответствие стандартам

```bash
curl -X POST http://127.0.0.1:8000/validate/code \
-H "Content-Type: application/json" \
-d '{"code":"@allure.manual\nwith allure.step(\"Arrange\"):\n    pass"}'
```

### 4. Получение курса валют (демо)

```bash
curl -X POST http://127.0.0.1:8000/tool/get_exchange_rate \
-H "Content-Type: application/json" \
-d '{"from_currency":"USD","to_currency":"RUB"}'
```

### 5. Отправка письма (требуется SMTP)

```bash
curl -X POST http://127.0.0.1:8000/tool/send_email \
-H "Content-Type: application/json" \
-d '{"to":"you@example.com","subject":"Test Email","body":"Hello from MCP"}'
```

### 6. Создание события в календаре (демо или Google Calendar)

```bash
curl -X POST http://127.0.0.1:8000/tool/create_calendar_event \
-H "Content-Type: application/json" \
-d '{"title":"Demo Event","start_iso":"2025-12-06T12:00:00","end_iso":"2025-12-06T13:00:00","description":"Demo"}'
```

---

## Особенности

* Генерация тестов и проверка кода работают через AI (LLM) при наличии токена.
* Реальные внешние сервисы (почта, календарь, курсы валют) работают только при настройке.
* Можно подключать SMTP, Google Calendar, API валют при необходимости.
* Всё готово к демонстрации на хакатоне.

---

## Структура проекта

```
app/               # сервер, LLM-клиент и utils
tests/             # тесты
examples/          # примеры запросов и output
requirements.txt
start.sh
.env               # настройки внешних сервисов и LLM
```

---

Автор: Хамза
Проект для хакатона, версия MVP.

```
```
