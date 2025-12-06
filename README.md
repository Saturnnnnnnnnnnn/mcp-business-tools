````markdown
# MCP Business Tools (MVP)

Версия: 0.1.0

Простой бэкенд для демонстрации автоматизации тестирования и утилит команды QA.

---

## Что делает проект

- Генерирует тест-кейсы (ручные и API) автоматически.
- Проверяет тесты на соответствие стандартам (Allure, AAA-паттерн).
- Создает события в календаре (демо).
- Отправляет письма (демо).
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
git clone
cd mcp-ready-project-full
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

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

### Проверка здоровья сервера

```bash
curl http://127.0.0.1:8000/health
```

### Создание календарного события

```bash
curl -X POST http://127.0.0.1:8000/tool/create_calendar_event \
-H "Content-Type: application/json" \
-d '{"title":"Test Event","start_iso":"2025-12-06T12:00:00","end_iso":"2025-12-06T13:00:00","description":"Demo"}'
```

### Получение курса валют (демо)

```bash
curl -X POST http://127.0.0.1:8000/tool/get_exchange_rate \
-H "Content-Type: application/json" \
-d '{"from_currency":"USD","to_currency":"RUB"}'
```

---

## Особенности

* Реальные внешние сервисы (почта, календарь, курсы валют) не подключены — демонстрационные данные.
* Всё готово к демонстрации на хакатоне.

---

## Структура проекта

```
app/               # код сервера
tests/             # тесты
examples/          # примеры использования
requirements.txt   # зависимости
start.sh           # скрипт запуска
```

---

Автор: Saturn
Проект для хакатона, версия MVP.

```