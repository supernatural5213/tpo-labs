"""Учебное веб-приложение: REST API пользователей (Flask + SQLite).
Версия после устранения уязвимостей, найденных в ЛР5."""
import hmac
import os
import re
import sqlite3

from flask import Flask, request, jsonify, send_file
from markupsafe import escape
from werkzeug.serving import WSGIRequestHandler

DB = "users.db"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")
app = Flask(__name__)


def get_db():
    # timeout: ожидание снятия блокировки вместо мгновенной ошибки "database is locked"
    conn = sqlite3.connect(DB, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("PRAGMA journal_mode=WAL")   # читатели не блокируют писателя
        conn.execute("CREATE TABLE IF NOT EXISTS users ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)")


def error(message, status):
    return jsonify({"error": message}), status


def authorized():
    """A01: удаление разрешено только с ключом доступа из переменной окружения API_TOKEN."""
    token = os.environ.get("API_TOKEN", "")
    given = request.headers.get("X-API-Key", "")
    return bool(token) and hmac.compare_digest(given, token)


@app.after_request
def security_headers(resp):
    """A05: защитные заголовки HTTP."""
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'; form-action 'none'; base-uri 'none'"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    resp.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    resp.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    resp.headers["Permissions-Policy"] = "geolocation=(), camera=(), microphone=()"
    return resp


@app.errorhandler(404)
def not_found(e):
    return error("not found", 404)


@app.errorhandler(405)
def not_allowed(e):
    return error("method not allowed", 405)


@app.errorhandler(500)
def server_error(e):
    return error("internal error", 500)   # без трассировки и деталей реализации


@app.route("/api/users", methods=["GET"])
def list_users():
    name = request.args.get("name")
    limit = min(max(request.args.get("limit", 50, type=int), 1), 100)   # постраничная выдача
    offset = max(request.args.get("offset", 0, type=int), 0)
    conn = get_db()
    if name:
        # A03: параметризованный запрос вместо подстановки строки
        rows = conn.execute("SELECT * FROM users WHERE name = ? LIMIT ?", (name, limit)).fetchall()
    else:
        rows = conn.execute("SELECT * FROM users ORDER BY id DESC LIMIT ? OFFSET ?", (limit, offset)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return error("JSON body required", 400)
    name, email = data.get("name"), data.get("email")
    # A04: проверка входных данных
    if not isinstance(name, str) or not 1 <= len(name.strip()) <= 100:
        return error("name: string 1..100 chars", 400)
    if not isinstance(email, str) or len(email) > 254 or not EMAIL_RE.match(email):
        return error("email: invalid format", 400)
    conn = get_db()
    cur = conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name.strip(), email))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return jsonify({"id": user_id, "name": name.strip(), "email": email}), 201


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not authorized():
        return error("unauthorized", 401)
    conn = get_db()
    cur = conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        return error("not found", 404)
    return jsonify({"deleted": user_id})


@app.route("/users")
def users_page():
    conn = get_db()
    rows = conn.execute("SELECT * FROM users ORDER BY id DESC LIMIT 100").fetchall()
    conn.close()
    # A03 (XSS): экранирование пользовательских данных перед вставкой в HTML
    items = "".join(f"<li>{escape(r['name'])} ({escape(r['email'])})</li>" for r in rows)
    return f"<html><body><h1>Пользователи</h1><ul>{items}</ul></body></html>"


@app.route("/openapi.json")
def openapi():
    return send_file("openapi.json", mimetype="application/json")


if __name__ == "__main__":
    init_db()
    WSGIRequestHandler.server_version = "app"   # не раскрывать версию Werkzeug/Python
    WSGIRequestHandler.sys_version = ""
    # A05: отладка выключена по умолчанию, адрес задаётся окружением (по умолчанию только localhost)
    app.run(host=os.environ.get("HOST", "127.0.0.1"), port=5000,
            debug=os.environ.get("FLASK_DEBUG") == "1")
