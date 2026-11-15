"""Rebuilds index.html from src/template.html and src/data.json.
Edit questions in src/data.json (or the page layout in src/template.html), then run:
    python3 build.py
"""
import pathlib
root = pathlib.Path(__file__).parent
template = (root / "src" / "template.html").read_text(encoding="utf-8")
data = (root / "src" / "data.json").read_text(encoding="utf-8")
(root / "index.html").write_text(template.replace("/*DATA*/null", data), encoding="utf-8")
print("index.html written")
