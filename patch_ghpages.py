path = "index.html"
html = open(path, encoding="utf-8").read()

# 1) Add Label nav link after the Pricing link
old_nav = '<a href="#pricing">Pricing</a>\n      <a href="#contact" class="header-cta">Trade Enquiry</a>'
new_nav = '<a href="#pricing">Pricing</a>\n      <a href="#label">Label</a>\n      <a href="#contact">Trade Enquiry</a>'
assert html.count(old_nav) == 1, ("nav count", html.count(old_nav))
html = html.replace(old_nav, new_nav)

# 2) Insert the Label & Nutrition section before the Contact comment
label_section = """<!-- Label & Nutrition -->
<section class="section label" id="label" style="background: linear-gradient(180deg, rgba(28,25,23,.92), rgba(28,25,23,.85)); position: relative; overflow: hidden; padding: 100px 0;">
  <div class="container">
    <div class="reveal">
      <span class="section-label">Label &amp; Nutrition</span>
      <h2 class="section-title">Label &amp; Nutrition</h2>
      <p class="section-subtitle">Full front and back label content for the Hills Artesian Spring Water range, plus the filtered-in analysis per litre.</p>
    </div>
    <div style="display:grid; grid-template-columns: 1.45fr 1fr; gap: 64px; align-items: start;">
      <!-- Front label -->
      <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 32px;">
        <h3 style="font-family: var(--font-heading); font-size: 22px; color: var(--color-primary); margin: 0 0 12px;">Front Label</h3>
        <p style="color: var(--color-accent); font-size: 13px; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; margin: 0 0 16px;">Artesian Spring Water</p>
        <p style="font-size: 15px; line-height: 1.75; color: var(--color-foreground); margin: 0 0 20px;">This bottle of Natural Artesian water was bottled at its source on the foothills of one of the oldest mountain ranges in the world. Naturally filtered over many years through the mineral enriched layers of volcanic rock. Hill's Artesian Spring Water has the perfect blend of minerals which ensures a smooth natural taste.</p>
        <p style="font-size: 14px; line-height: 1.7; color: var(--color-foreground); margin: 0 0 8px;"><strong style="color: var(--color-primary);">Bottled at source:</strong> Serenity Mountain and Forest Lodge, Malelane 1320</p>
        <p style="font-size: 14px; line-height: 1.7; color: var(--color-foreground); margin: 0 0 8px;"><strong style="color: var(--color-primary);">Specially bottled for:</strong> Hills Beverages, 917 Morkels Close, Midrand, Johannesburg, 1685</p>
        <p style="font-size: 14px; line-height: 1.7; color: var(--color-foreground); margin: 0 0 8px;"><strong style="color: var(--color-primary);">Consumer information:</strong> Info@hillsbeverages.co.za &nbsp;|&nbsp; <a href="https://www.hillsbeverages.co.za" style="color: var(--color-accent);">www.hillsbeverages.co.za</a></p>
        <div style="display:flex; flex-wrap:wrap; gap:16px; margin-top:20px; padding-top:16px; border-top:1px solid var(--color-border);">
          <div style="flex:1 1 200px; min-width:140px; background: var(--color-muted); border-radius:8px; padding:12px 16px; text-align:center;">
            <p style="color:var(--color-muted-foreground); font-size:12px;">PH</p>
            <p style="font-size:18px; font-weight:700; color:var(--color-primary);">4.9</p>
          </div>
          <div style="flex:1 1 200px; min-width:140px; background: var(--color-muted); border-radius:8px; padding:12px 16px; text-align:center;">
            <p style="color:var(--color-muted-foreground); font-size:12px;">PRODUCT OF</p>
            <p style="font-size:18px; font-weight:700; color:var(--color-primary);">SOUTH AFRICA</p>
          </div>
        </div>
      </div>
      <!-- Back labels + analysis -->
      <div style="display:flex; flex-direction:column; gap:24px;">
        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
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
        </div>
        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
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
        </div>
        <div style="background: var(--color-card); border: 1px solid var(--color-border); border-radius: var(--radius); padding: 24px;">
          <h3 style="font-size:18px; color:var(--color-primary); margin:0 0 12px;">Filtered IN MG/LITRE</h3>
          <div style="overflow-x:auto;">
            <table style="width:100%; border-collapse:collapse; font-size:14px;">
              <thead>
                <tr style="background:var(--color-muted);">
                  <th style="color:var(--color-muted-foreground); text-align:left; padding:8px 10px; font-size:12px; letter-spacing:1px; text-transform:uppercase;">Analyte</th>
                  <th style="color:var(--color-muted-foreground); text-align:left; padding:8px 10px; font-size:12px; letter-spacing:1px; text-transform:uppercase;">Result</th>
                </tr>
              </thead>
              <tbody>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Calcium as Ca</td><td style="padding:8px 10px; font-weight:600;">1.3</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Magnesium as Mg</td><td style="padding:8px 10px; font-weight:600;">1.4</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Sodium as Na</td><td style="padding:8px 10px; font-weight:600;">5.0</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Potassium as K</td><td style="padding:8px 10px; font-weight:600;">0.43</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">TDS</td><td style="padding:8px 10px; font-weight:600;">50</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Chloride Cl</td><td style="padding:8px 10px;">&lt;20</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">pH</td><td style="padding:8px 10px; font-weight:600;">4.9</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Sulphate SO4</td><td style="padding:8px 10px;">&lt;0.15</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Alkalinity as CaCO3</td><td style="padding:8px 10px;">&lt;20</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Nitrate as N</td><td style="padding:8px 10px;">0.02</td></tr>
                <tr style="border-bottom:1px solid var(--color-border);"><td style="padding:8px 10px;">Fluoride as F</td><td style="padding:8px 10px;">0.1</td></tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

anchor = "<!-- Contact -->"
assert html.count(anchor) == 1, ("contact count", html.count(anchor))
html = html.replace(anchor, label_section + "\n" + anchor)

# normalize line endings to LF (repo convention)
html = html.replace("\r\n", "\n").replace("\r", "\n")

open(path, "w", encoding="utf-8", newline="\n").write(html)
print("patched. length:", len(html))
