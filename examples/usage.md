# 1. Проверка состояния сервера (Health Check)
curl http://127.0.0.1:8000/health

# 2. Получение курса валют (демо, внешние сервисы не подключены)
curl -X POST http://127.0.0.1:8000/tool/get_exchange_rate \
-H "Content-Type: application/json" \
-d '{"from_currency":"USD","to_currency":"RUB"}'

# 3. Отправка письма (требуется настроенный SMTP)
curl -X POST http://127.0.0.1:8000/tool/send_email \
-H "Content-Type: application/json" \
-d '{"to":"you@example.com","subject":"Test Email","body":"Hello from MCP"}'

# 4. Создание события в календаре (демо, работает без внешних сервисов)
curl -X POST http://127.0.0.1:8000/tool/create_calendar_event \
-H "Content-Type: application/json" \
-d '{"title":"Demo Event","start_iso":"2025-12-06T12:00:00","end_iso":"2025-12-06T13:00:00","description":"Demo"}'
