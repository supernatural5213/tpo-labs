"""Негативные API-тесты безопасности (OWASP Top 10): TC-03, TC-04 и дополнительные."""
import os
import pytest
import app as app_module

TOKEN = "test-token"


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(app_module, "DB", str(tmp_path / "test.db"))
    monkeypatch.setenv("API_TOKEN", TOKEN)
    app_module.init_db()
    app_module.app.config["TESTING"] = True
    c = app_module.app.test_client()
    c.post("/api/users", json={"name": "alice", "email": "alice@test.com"})
    c.post("/api/users", json={"name": "bob", "email": "bob@test.com"})
    return c


def count(client):
    return len(client.get("/api/users").get_json())


# TC-03: SQL Injection (A03 Injection)
def test_tc03_sqli_in_query_param_does_not_leak_rows(client):
    r = client.get("/api/users", query_string={"name": "' OR '1'='1"})
    assert r.status_code in (200, 400)
    if r.status_code == 200:
        assert r.get_json() == [], "инъекция вернула все записи"


def test_tc03_sqli_in_path_does_not_delete_all(client):
    r = client.delete("/api/users/1 OR 1=1", headers={"X-API-Key": TOKEN})
    assert r.status_code in (400, 404)
    assert count(client) == 2, "инъекция удалила записи"


# TC-04: XSS (A03 Injection, межсайтовый скриптинг)
def test_tc04_stored_xss_is_escaped_on_html_page(client):
    payload = "<script>alert(1)</script>"
    client.post("/api/users", json={"name": payload, "email": "x@test.com"})
    html = client.get("/users").get_data(as_text=True)
    assert payload not in html
    assert "&lt;script&gt;" in html


def test_tc04_api_returns_json_content_type(client):
    r = client.post("/api/users", json={"name": "<img src=x onerror=alert(1)>", "email": "y@test.com"})
    assert r.headers["Content-Type"].startswith("application/json")


# A01 Broken Access Control: удаление без ключа доступа
def test_delete_without_api_key_is_rejected(client):
    r = client.delete("/api/users/1")
    assert r.status_code == 401
    assert count(client) == 2


def test_delete_with_wrong_api_key_is_rejected(client):
    r = client.delete("/api/users/1", headers={"X-API-Key": "wrong"})
    assert r.status_code == 401


def test_delete_with_valid_key_works(client):
    r = client.delete("/api/users/1", headers={"X-API-Key": TOKEN})
    assert r.status_code == 200
    assert count(client) == 1


# A04/A05: проверка входных данных, отсутствие 500 на некорректный ввод
@pytest.mark.parametrize("body", [{}, {"name": "x"}, {"name": "", "email": "a@b.c"},
                                  {"name": "x", "email": "not-an-email"}, {"name": "x" * 500, "email": "a@b.c"}])
def test_invalid_user_data_returns_400(client, body):
    assert client.post("/api/users", json=body).status_code == 400


def test_non_json_body_returns_400(client):
    r = client.post("/api/users", data="name=x", content_type="text/plain")
    assert r.status_code in (400, 415)


# A05 Security Misconfiguration: защитные заголовки
def test_security_headers_present(client):
    h = client.get("/api/users").headers
    assert h.get("X-Content-Type-Options") == "nosniff"
    assert h.get("X-Frame-Options") == "DENY"
    assert "Content-Security-Policy" in h
