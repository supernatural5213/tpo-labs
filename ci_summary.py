"""Публикация ключевых результатов CI: аннотации ::notice и сводка шага (GITHUB_STEP_SUMMARY)."""
import csv, json, os, re

lines = []
if os.path.exists("load_report_stats.csv"):
    for r in csv.DictReader(open("load_report_stats.csv")):
        lines.append(f"LOCUST {r['Type'] or '-'} {r['Name']}: reqs={r['Request Count']} fails={r['Failure Count']} "
                     f"avg={float(r['Average Response Time']):.1f}ms med={r['Median Response Time']} p95={r['95%']} "
                     f"p99={r['99%']} max={float(r['Max Response Time']):.0f} rps={float(r['Requests/s']):.2f}")
if os.path.exists("check_load.txt"):
    lines += ["CHECK " + l for l in open("check_load.txt", encoding="utf-8").read().splitlines()]
if os.path.exists("bandit_report.txt"):
    t = open("bandit_report.txt", encoding="utf-8").read()
    for m in re.finditer(r"Issue: \[(B\d+):\w+\] (.*?)\n\s+Severity: (\w+)\s+Confidence: (\w+).*?Location: (\S+)", t, re.S):
        lines.append(f"BANDIT {m.group(1)} {m.group(3)}/{m.group(4)} {m.group(5)}: {m.group(2)[:90]}")
    tot = re.search(r"Total issues \(by severity\):\s+Undefined: \d+\s+Low: (\d+)\s+Medium: (\d+)\s+High: (\d+)", t)
    if tot:
        lines.append(f"BANDIT TOTAL Low={tot.group(1)} Medium={tot.group(2)} High={tot.group(3)}")
if os.path.exists("pytest_report.xml"):
    x = open("pytest_report.xml", encoding="utf-8").read()
    m = re.search(r'<testsuite [^>]*', x)
    attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(0))) if m else {}
    lines.append(f"PYTEST tests={attrs.get('tests')} failures={attrs.get('failures')} errors={attrs.get('errors')}")
    for tc in re.finditer(r'<testcase ([^>]*?)(/>|>(.*?)</testcase>)', x, re.S):
        name = re.search(r'\bname="([^"]+)"', tc.group(1)).group(1)
        body = tc.group(3) or ""
        st = "FAILED" if ("<failure" in body or "<error" in body) else "PASSED"
        lines.append(f"PYTEST {st} {name}")
if os.path.exists("zap_report.json"):
    z = json.load(open("zap_report.json"))
    cnt = {}
    for site in z.get("site", []):
        for a in site.get("alerts", []):
            risk = a.get("riskdesc", "").split(" ")[0]
            cnt[risk] = cnt.get(risk, 0) + 1
            lines.append(f"ZAP {a.get('riskdesc')} [{a.get('pluginid')}] {a.get('name')} (instances={len(a.get('instances', []))})")
    lines.append("ZAP TOTAL " + ", ".join(f"{k}={v}" for k, v in sorted(cnt.items())) if cnt else "ZAP TOTAL no alerts")

if os.path.exists("zap_console.txt"):
    tail = open("zap_console.txt", encoding="utf-8", errors="replace").read().splitlines()
    lines += ["ZAPLOG " + l for l in tail if l.startswith(("FAIL", "WARN", "PASS:", "INFO")) or "ERROR" in l][-40:]

for l in lines:
    print(f"::notice title=result::{l}")
if os.environ.get("GITHUB_STEP_SUMMARY"):
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as f:
        f.write("```\n" + "\n".join(lines) + "\n```\n")
