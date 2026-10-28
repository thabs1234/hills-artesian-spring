import io

path = "C:/Users/Thabang/Desktop/Hills-Artesian-Spring/index.html"
html = open(path, encoding="utf-8").read()

# Replace the two-line "PRODUCT OF / SOUTH AFRICA" cards with a single clean line.
old = '''        <div style="display:flex; flex-wrap:wrap; gap:16px; margin-top:20px; padding-top:16px; border-top:1px solid var(--color-border);">
          <div style="flex:1 1 200px; min-width:140px; background: var(--color-muted); border-radius:8px; padding:12px 16px; text-align:center;">
            <p style="color:var(--color-muted-foreground); font-size:12px;">PH</p>
            <p style="font-size:18px; font-weight:700; color:var(--color-primary);">4.9</p>
          </div>
          <div style="flex:1 1 200px; min-width:140px; background: var(--color-muted); border-radius:8px; padding:12px 16px; text-align:center;">
            <p style="color:var(--color-muted-foreground); font-size:12px;">PRODUCT OF</p>
            <p style="font-size:18px; font-weight:700; color:var(--color-primary);">SOUTH AFRICA</p>
          </div>
        </div>'''

new = '''        <div style="display:flex; align-items:center; gap:16px; margin-top:20px; padding-top:16px; border-top:1px solid var(--color-border);">
          <span style="color: var(--color-muted-foreground); font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase;">PH</span>
          <span style="color: var(--color-primary); font-size:20px; font-weight:700; margin-left:6px;">4.9</span>
          <span style="color: var(--color-muted-foreground); font-size:12px; font-weight:600; letter-spacing:1px; text-transform:uppercase; margin-left:12px;">PRODUCT OF SOUTH AFRICA</span>
        </div>'''

assert html.count(old) == 1, html.count(old)
html = html.replace(old, new)

open(path, "w", encoding="utf-8").write(html)
print("patched. length:", len(html))
