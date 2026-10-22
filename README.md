# Тестирование ПО: лабораторные работы 4 и 5

Учебное приложение Flask + SQLite с REST API пользователей:

| Метод | Путь | Назначение |
|---|---|---|
| GET | /api/users | список пользователей (limit, offset) |
| POST | /api/users | создание пользователя |
| DELETE | /api/users/<id> | удаление пользователя |

* ЛР4: нагрузочное тестирование (Locust), workflow `.github/workflows/load-test.yml`.
* ЛР5: SAST (Bandit), DAST (OWASP ZAP), негативные API-тесты, workflow `.github/workflows/security.yml`.

Локальный запуск:

```
pip install -r requirements.txt
python app.py
locust -f locustfile.py --headless -u 50 -r 10 --run-time 1m --host=http://127.0.0.1:5000 --csv=load_report
```
