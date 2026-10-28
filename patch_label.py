import io

path = "C:/Users/Thabang/Desktop/Hills-Artesian-Spring/index.html"
html = open(path, encoding="utf-8").read()
orig = html

def replace_once(old, new, label):
    global html
    c = html.count(old)
    assert c == 1, "%s: found %d" % (label, c)
    html = html.replace(old, new)
    print("replaced:", label)

# 1) 1-litre back label: add "Discover us here" QR
old_1l = '''        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
          <h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Back Label &mdash; 1 litre</h3>
          <p style="margin:0 0 12px;"><span style="color:var(--color-muted-foreground); font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">Barcode</span><br>
            <span style="font-family:var(--font-heading); font-size:18px; color:var(--color-foreground);">6 009900 553047 &gt;</span></p>
          <p style="margin:0; font-size:12px; color:var(--color-muted-foreground);">RECYCLE &nbsp;|&nbsp; PET 1 &nbsp;&middot;&nbsp; 1 L</p>
        </div>'''
new_1l = '''        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
          <h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Back Label &mdash; 1 litre</h3>
          <p style="margin:0 0 12px;"><span style="color:var(--color-muted-foreground); font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">Barcode</span><br>
            <span style="font-family:var(--font-heading); font-size:18px; color:var(--color-foreground);">6 009900 553047 &gt;</span></p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:12px;">
            <a href="https://www.hillsbeverages.co.za" target="_blank" rel="noopener">
              <img src="assets/qr-discover.svg" alt="Scan to discover Hills" style="width:34px; height:34px; display:block;">
            </a>
            <span style="font-size:12px; color:var(--color-accent); font-weight:600;">Discover us here</span>
          </div>
          <p style="margin:0; font-size:12px; color:var(--color-muted-foreground);">RECYCLE &nbsp;|&nbsp; PET 1 &nbsp;&middot;&nbsp; 1 L</p>
        </div>'''
replace_once(old_1l, new_1l, "1-litre back label")

# 2) 500 ml back label: add "Discover us here" QR
old_500 = '''        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
          <h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Back Label &mdash; 500 ml</h3>
          <p style="margin:0 0 12px;"><span style="color:var(--color-muted-foreground); font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">Barcode</span><br>
            <span style="font-family:var(--font-heading); font-size:18px; color:var(--color-foreground);">6 009900 553030 &gt;</span></p>
          <p style="margin:0; font-size:12px; color:var(--color-muted-foreground);">RECYCLE &nbsp;|&nbsp; PET 1 &nbsp;&middot;&nbsp; 500 ml</p>
        </div>'''
new_500 = '''        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
          <h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Back Label &mdash; 500 ml</h3>
          <p style="margin:0 0 12px;"><span style="color:var(--color-muted-foreground); font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">Barcode</span><br>
            <span style="font-family:var(--font-heading); font-size:18px; color:var(--color-foreground);">6 009900 553030 &gt;</span></p>
          <div style="display:flex; align-items:center; gap:10px; margin-top:12px;">
            <a href="https://www.hillsbeverages.co.za" target="_blank" rel="noopener">
              <img src="assets/qr-discover.svg" alt="Scan to discover Hills" style="width:34px; height:34px; display:block;">
            </a>
            <span style="font-size:12px; color:var(--color-accent); font-weight:600;">Discover us here</span>
          </div>
          <p style="margin:0; font-size:12px; color:var(--color-muted-foreground);">RECYCLE &nbsp;|&nbsp; PET 1 &nbsp;&middot;&nbsp; 500 ml</p>
        </div>'''
replace_once(old_500, new_500, "500ml back label")

# 3) heading "Filtered In (mg/Litre)" -> "Filtered IN MG/LITRE"
replace_once('<h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Filtered In (mg/Litre)</h3>',
            '<h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Filtered IN MG/LITRE</h3>',
            "mg/litre heading")

# 4) apostrophe in Hill's
replace_once("Hill's Artesian Spring Water", "Hill\u2019s Artesian Spring Water", "apostrophe")

print("length", len(html))
open(path, "w", encoding="utf-8").write(html)
print("saved.")
