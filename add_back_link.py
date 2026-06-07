from pathlib import Path

NAV = '<div style="margin-bottom:1.2em;"><a href="index.html" style="color:#005499;font-size:0.92em;text-decoration:none;">&#8592; Back to Overview</a></div>\n'

for f in sorted(Path(__file__).parent.glob("*.html")):
    if f.name == "index.html":
        continue
    txt = f.read_text(encoding="utf-8")
    if "Back to Overview" in txt:
        print(f"-- {f.name}")
        continue
    f.write_text(txt.replace("<body>", "<body>\n" + NAV, 1), encoding="utf-8")
    print(f"OK {f.name}")
