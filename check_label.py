import sys
from html.parser import HTMLParser

path = "C:/Users/Thabang/Desktop/Hills-Artesian-Spring/index.html"
html = open(path, encoding="utf-8").read()

VOID = {"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}

class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append("closing </%s> with empty stack at %s" % (tag, self.getpos()))
            return
        open_tag, pos = self.stack.pop()
        if open_tag != tag:
            self.errors.append("mismatch: opened <%s> at %s, closed </%s> at %s" % (open_tag, pos, tag, self.getpos()))

c = Checker()
c.feed(html)
# report unclosed tags, newest first
if c.stack:
    print("UNCLOSED:")
    for tag, pos in reversed(c.stack):
        print("  <%s> opened at %s" % (tag, pos))
if c.errors:
    print("ERRORS:")
    for e in c.errors:
        print(" ", e)
if not c.stack and not c.errors:
    print("PASS: all tags balanced")

# required data checks in the new label section
need = [
    "Label &amp; Nutrition", "#label", "Front Label", "Back Label &mdash; 1 litre",
    "6 009900 553047", "RECYCLE &nbsp;|&nbsp; PET 1 &nbsp;&middot;&nbsp; 1 L",
    "Back Label &mdash; 500 ml", "6 009900 553030", "500 ml",
    "Filtered In (mg/Litre)", "Calcium as Ca", "1.3", "Magnesium as Mg", "1.4",
    "Sodium as Na", "5.0", "Potassium as K", "0.43", "TDS", "Chloride Cl", "&lt;20",
    "pH", "4.9", "Sulphate SO4", "&lt;0.15", "Alkalinity as CaCO3", "&lt;20",
    "Nitrate as N", "0.02", "Fluoride as F", "0.1",
    "Bottled at source:", "Serenity Mountain and Forest Lodge, Malelane 1320",
    "Specially bottled for:", "Hills Beverages, 917 Morkels Close, Midrand, Johannesburg, 1685",
    "www.hillsbeverages.co.za", "Info@hillsbeverages.co.za", "PRODUCT OF SOUTH AFRICA", "4.9",
]
missing = [k for k in need if k not in html]
print("missing required strings:", missing if missing else "NONE")
