"""Учебное веб-приложение: REST API пользователей (Flask + SQLite)."""
import sqlite3
from flask import Flask, request, jsonify

DB = "users.db"
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


@app.route("/api/users", methods=["GET"])
def list_users():
    name = request.args.get("name")
    limit = min(request.args.get("limit", 50, type=int), 100)   # постраничная выдача
    offset = request.args.get("offset", 0, type=int)
    conn = get_db()
    if name:
        rows = conn.execute(f"SELECT * FROM users WHERE name = '{name}'").fetchall()
    else:
        rows = conn.execute("SELECT * FROM users ORDER BY id DESC LIMIT ? OFFSET ?", (limit, offset)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    conn = get_db()
    cur = conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (data["name"], data["email"]))
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return jsonify({"id": user_id, "name": data["name"], "email": data["email"]}), 201


@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    conn = get_db()
    conn.execute(f"DELETE FROM users WHERE id = {user_id}")
    conn.commit()
    conn.close()
    return jsonify({"deleted": user_id})


@app.route("/users")
def users_page():
    conn = get_db()
    rows = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    items = "".join(f"<li>{r['name']} ({r['email']})</li>" for r in rows)
    return f"<html><body><h1>Пользователи</h1><ul>{items}</ul></body></html>"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
