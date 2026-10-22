"""Проверка критериев тест-кейсов ЛР4 по файлу load_report_stats.csv."""
import csv, sys

rows = {r["Name"]: r for r in csv.DictReader(open("load_report_stats.csv"))}
get, post, agg = None, None, rows["Aggregated"]
for r in csv.DictReader(open("load_report_stats.csv")):
    if r["Type"] == "GET": get = r
    if r["Type"] == "POST": post = r

def f(r, k): return float(r[k])
fail_rate = 100 * f(agg, "Failure Count") / max(f(agg, "Request Count"), 1)
checks = [
    ("TC-01 GET /api/users: среднее < 200 мс", f(get, "Average Response Time"), 200),
    ("TC-02 POST /api/users: среднее < 300 мс", f(post, "Average Response Time"), 300),
    ("TC-03 50 users: ошибки < 1 %", fail_rate, 1),
]
ok = True
for name, val, lim in checks:
    res = val < lim
    ok &= res
    print(f"{'PASS' if res else 'FAIL'}  {name}: {val:.2f}")
print(f"RPS (TPS): {f(agg, 'Requests/s'):.2f}; p95: {agg['95%']} мс; p99: {agg['99%']} мс")
sys.exit(0 if ok else 1)
