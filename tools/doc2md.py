"""convert the google docs html export to plain text keeping **bold**, ==highlight==, tables and image markers.
usage: python -I doc2md.py notes.html out.md
"""
import re, sys
from html.parser import HTMLParser

src, out = sys.argv[1], sys.argv[2]
h = open(src, encoding="utf-8").read()
css = re.search(r"<style[^>]*>(.*?)</style>", h, re.S).group(1)
bold, hi = set(), set()
for cls, body in re.findall(r"\.(c\d+)\{([^}]*)\}", css):
    if "font-weight:700" in body:
        bold.add(cls)
    m = re.search(r"background-color:(#[0-9a-f]{6})", body)
    if m and m.group(1) not in ("#ffffff",) and "border" not in body:
        hi.add(cls)


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.stack, self.cell, self.row, self.intable = [], [], None, None, 0
        self.list_depth = 0

    def emit(self, s):
        if self.cell is not None:
            self.cell.append(s)
        else:
            self.out.append(s)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = set((a.get("class") or "").split())
        if tag == "span":
            b, hl = bool(cls & bold), bool(cls & hi)
            self.stack.append((b, hl))
            if hl: self.emit("==")
            if b: self.emit("**")
        elif tag in ("p", "h1", "h2", "h3", "h4", "h5", "h6"):
            if self.cell is not None:
                if self.cell: self.cell.append(" / ")
            else:
                self.out.append("\n")
                if tag[0] == "h": self.out.append("#" * int(tag[1]) + " ")
        elif tag == "li":
            self.emit("\n" + "  " * max(0, self.list_depth - 1) + "- ") if self.cell is None else self.emit(" • ")
        elif tag in ("ul", "ol"):
            self.list_depth += 1
        elif tag == "table":
            self.intable += 1; self.out.append("\n[TABLE]")
        elif tag == "tr":
            self.row = []
        elif tag == "td":
            self.cell = []
        elif tag == "img":
            self.emit(" [IMG] ")
        elif tag == "br":
            self.emit(" / " if self.cell is not None else "\n")

    def handle_endtag(self, tag):
        if tag == "span" and self.stack:
            b, hl = self.stack.pop()
            if b: self.emit("**")
            if hl: self.emit("==")
        elif tag in ("ul", "ol"):
            self.list_depth -= 1
        elif tag == "td":
            self.row.append(re.sub(r"\s+", " ", "".join(self.cell)).strip(" /"))
            self.cell = None
        elif tag == "tr":
            self.out.append("\n| " + " | ".join(self.row) + " |")
            self.row = None
        elif tag == "table":
            self.intable -= 1; self.out.append("\n[/TABLE]\n")

    def handle_data(self, d):
        self.emit(d)


p = P()
p.feed(h[h.find("<body"):])
t = "".join(p.out)
t = t.replace(" ", " ")
t = re.sub(r"\*\*(\s*)\*\*", r"\1", t)
t = re.sub(r"==(\s*)==", r"\1", t)
t = re.sub(r"[ \t]+\n", "\n", t)
t = re.sub(r"\n{3,}", "\n\n", t)
open(out, "w", encoding="utf-8", newline="\n").write(t)
print(len(t), "chars;", len(bold), "bold classes;", len(hi), "highlight classes")
