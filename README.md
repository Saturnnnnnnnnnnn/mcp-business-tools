````markdown
# MCP Business Tools (MVP)

Версия: 0.1.0

Простой бэкенд для демонстрации автоматизации тестирования и утилит команды QA.

---

## Что делает проект

- Генерирует тест-кейсы (ручные и API) автоматически.
- Проверяет тесты на соответствие стандартам (Allure, AAA-паттерн).
- Создает события в календаре (демо).
- Отправляет письма (демо, требует настроенный SMTP).
- Возвращает тестовые данные, например курсы валют (демо).

Всё через веб-API, можно тестировать через Swagger или HTTP-запросы.

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

Создайте файл `.env` в корне проекта для подключения почты и календаря:

```
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=user@example.com
SMTP_PASSWORD=yourpassword

GOOGLE_CALENDAR_API_KEY=your_api_key
```

> Без этих настроек `send_email` и интеграция с Google Calendar будут работать только с демо-данными.

Можно оставить `.env` пустым для работы с демо-данными.

---

## Запуск

```bash
python3 -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

* API доступно: `http://127.0.0.1:8000`
* Swagger UI: `http://127.0.0.1:8000/docs`
* Health check: `http://127.0.0.1:8000/health`

---

## Примеры запросов

### 1. Проверка состояния сервера (Health Check)

```bash
curl http://127.0.0.1:8000/health
```

### 2. Получение курса валют (демо)

```bash
curl -X POST http://127.0.0.1:8000/tool/get_exchange_rate \
-H "Content-Type: application/json" \
-d '{"from_currency":"USD","to_currency":"RUB"}'
```

### 3. Отправка письма (требуется настроенный SMTP)

```bash
curl -X POST http://127.0.0.1:8000/tool/send_email \
-H "Content-Type: application/json" \
-d '{"to":"you@example.com","subject":"Test Email","body":"Hello from MCP"}'
```

### 4. Создание события в календаре (демо)

```bash
curl -X POST http://127.0.0.1:8000/tool/create_calendar_event \
-H "Content-Type: application/json" \
-d '{"title":"Demo Event","start_iso":"2025-12-06T12:00:00","end_iso":"2025-12-06T13:00:00","description":"Demo"}'
```

---

## Особенности

* Реальные внешние сервисы (почта, календарь, курсы валют) не подключены — демонстрационные данные.
* Можно подключать SMTP, Google Calendar, API валют при необходимости.
* Всё готово к демонстрации на хакатоне.

---

## Структура проекта

```
app/               # код сервера
tests/             # тесты
examples/          # примеры использования команд curl
requirements.txt   # зависимости
start.sh           # скрипт запуска
.env               # настройки внешних сервисов (SMTP, календарь)
```

---

Автор: Хамза
Проект для хакатона, версия MVP.

```

