from html.parser import HTMLParser
from pathlib import Path
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Parser(HTMLParser):
    pass

for html_file in ["index.html", "404.html"]:
    Parser().feed((ROOT / html_file).read_text(encoding="utf-8"))
    print(f"{html_file}: HTML parsed successfully")

json.loads((ROOT / "site.webmanifest").read_text(encoding="utf-8"))
print("site.webmanifest: JSON parsed successfully")

ET.parse(ROOT / "sitemap.xml")
print("sitemap.xml: XML parsed successfully")

for required in ["vercel.json", "robots.txt", "README.md", "CONTRIBUTING.md"]:
    if not (ROOT / required).exists():
        raise SystemExit(f"Missing required file: {required}")
    print(f"{required}: present")
