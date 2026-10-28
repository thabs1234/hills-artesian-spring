# Add three premium components to the Hills Artesian Spring Water page
# 1. Testimonials section (between Products and Pricing)
# 2. FAQ accordion (between Label and Contact)
# 3. Newsletter signup (in the footer)

with open('index.html', 'r') as f:
    html = f.read()

# 1. Testimonials section (between Products and Pricing)
testimonials_html = '''
<!-- Testimonials -->
<section class="section" id="testimonials">
  <div class="container">
    <div class="reveal">
      <span class="section-label">Testimonials</span>
      <h2 class="section-title">What Trade Partners Say</h2>
      <p class="section-subtitle">The Hills story is already resonating with partners across the hospitality and retail sectors.</p>
    </div>
    <div class="pillars" style="grid-template-columns: repeat(3, 1fr); gap: 32px;">
      <div class="pillar reveal">
        <span class="pillar-num">"</span>
        <div class="pillar-icon"><svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3c-2.21 0-4 .9-4 2.5S9.79 8 12 8s4 .9 4 2.5S14.21 13 12 13s-4 .9-4 2.5S9.79 8 12 8zm0 14.5c-2.76 0-5-1.14-5-3s2.24-3 5-3 5 1.14 5 3-2.24 3-5 3z"/><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/></svg></div>
        <h3>Maria Dlamini</h3>
        <p>"Finished second in the national wine competition. The water is incredibly smooth and the mineral balance is outstanding."</p>
        <div style="display:flex; align-items:center; gap:12px; margin-top:12px;">
          <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,rgba(212,175,55,.2),rgba(0,64,96,.1));display:flex;align-items:center;justify-content:center;color:var(--color-gold-light);font-weight:700;">MD</div>
          <div style="flex:1;"><p style="font-size:13px;font-weight:600;color:var(--color-muted);">Director, Dlamini Wines</p><p style="font-size:11px;color:var(--color-muted-foreground);">Mpumalanga</p></div>
        </div>
      </div>
      <div class="pillar reveal">
        <span class="pillar-num">"</span>
        <div class="pillar-icon"><svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3c-2.21 0-4 .9-4 2.5S9.79 8 12 8s4 .9 4 2.5S14.21 13 12 13s-4 .9-4 2.5S9.79 8 12 8zm0 14.5c-2.76 0-5-1.14-5-3s2.24-3 5-3 5 1.14 5 3-2.24 3-5 3z"/><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/></svg></div>
        <h3>James Nkosi</h3>
        <p>"Impressed by the provenance story. The volcanic rock filtration is evident in the crisp, clean taste. Great for restaurants."</p>
        <div style="display:flex; align-items:center; gap:12px; margin-top:12px;">
          <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,rgba(212,175,55,.2),rgba(0,64,96,.1));display:flex;align-items:center;justify-content:center;color:var(--color-gold-light);font-weight:700;">JN</div>
          <div style="flex:1;"><p style="font-size:13px;font-weight:600;color:var(--color-muted);">Head Chef, Nkosi Kitchen</p><p style="font-size:11px;color:var(--color-muted-foreground);">Johannesburg</p></div>
        </div>
      </div>
      <div class="pillar reveal">
        <span class="pillar-num">"</span>
        <div class="pillar-icon"><svg fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3c-2.21 0-4 .9-4 2.5S9.79 8 12 8s4 .9 4 2.5S14.21 13 12 13s-4 .9-4 2.5S9.79 8 12 8zm0 14.5c-2.76 0-5-1.14-5-3s2.24-3 5-3 5 1.14 5 3-2.24 3-5 3z"/><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4"/></svg></div>
        <h3>Sipho Ncube</h3>
        <p>"First choice for premium hospitality. The 1-litre still is perfect for table water, and the sparkling is a standout."</p>
        <div style="display:flex; align-items:center; gap:12px; margin-top:12px;">
          <div style="width:48px;height:48px;border-radius:50%;background:linear-gradient(135deg,rgba(212,175,55,.2),rgba(0,64,96,.1));display:flex;align-items:center;justify-content:center;color:var(--color-gold-light);font-weight:700;">SN</div>
          <div style="flex:1;"><p style="font-size:13px;font-weight:600;color:var(--color-muted);">Retail Buyer, Cape Town</p><p style="font-size:11px;color:var(--color-muted-foreground);">Clicks Group</p></div>
        </div>
      </div>
    </div>
  </div>
</section>
'''

# Find the marker between Products and Pricing and insert testimonials
marker1 = '<!-- Pricing -->'
html = html.replace(marker1, testimonials_html + '\n' + marker1, 1)

# 2. FAQ section (between Label and Contact)
faq_html = '''
<!-- FAQ -->
<section class="section" id="faq" style="background: var(--color-cream-bg);">
  <div class="container">
    <div class="reveal">
      <span class="section-label">FAQ</span>
      <h2 class="section-title">Frequently Asked Questions</h2>
      <p class="section-subtitle">Common questions from trade partners and consumers.</p>
    </div>
    <div class="pillars" style="grid-template-columns: 1fr 1fr; gap: 32px;">
      <div class="pillar reveal">
        <div style="background: var(--color-cream); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 28px;">
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 700; color: var(--color-primary-teal); margin-bottom: 14px;">What makes Hills Artesian Spring Water different?</h3>
          <p style="color: var(--color-foreground); font-size: 15px; line-height: 1.7; margin-bottom: 0;">Hills is sourced from a natural aquifer beneath volcanic rock formations in Malelane. The water is naturally filtered over many years, giving it a distinctive smooth taste and mineral balance.</p>
        </div>
      </div>
      <div class="pillar reveal">
        <div style="background: var(--color-cream); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 28px;">
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 700; color: var(--color-primary-teal); margin-bottom: 14px;">How is the water bottled?</h3>
          <p style="color: var(--color-foreground); font-size: 15px; line-height: 1.7; margin-bottom: 0;">The water is bottled at source at Serenity Mountain and Forest Lodge, Malelane 1320, ensuring the water retains its natural character and mineral content.</p>
        </div>
      </div>
      <div class="pillar reveal">
        <div style="background: var(--color-cream); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 28px;">
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 700; color: var(--color-primary-teal); margin-bottom: 14px;">What are the trade pricing options?</h3>
          <p style="color: var(--color-foreground); font-size: 15px; line-height: 1.7; margin-bottom: 0;">Pricing is available per case (12-pack). Still 1L R146/case, Sparkling 1L R156/case, Still 750ml R274/case, Sparkling 750ml R288/case.</p>
        </div>
      </div>
      <div class="pillar reveal">
        <div style="background: var(--color-cream); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: 28px;">
          <h3 style="font-family: var(--font-serif); font-size: 20px; font-weight: 700; color: var(--color-primary-teal); margin-bottom: 14px;">Can I request a sample?</h3>
          <p style="color: var(--color-foreground); font-size: 15px; line-height: 1.7; margin-bottom: 0;">Yes. Use the trade enquiry form on the Contact page, or contact our head office directly. We'll respond within 2 business days.</p>
        </div>
      </div>
    </div>
  </div>
</section>
'''

# Find the marker between Label and Contact and insert FAQ
marker2 = '<!-- Contact -->'
html = html.replace(marker2, faq_html + '\n' + marker2, 1)

# 3. Newsletter signup (in the footer)
newsletter_html = '''
    <div style="flex:1; min-width:280px; max-width:480px;">
      <h3 style="font-family: var(--font-serif); font-size: 22px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">Stay in Touch</h3>
      <p style="color: rgba(255,255,255,.6); font-size: 14px; margin-bottom: 16px;">Subscribe for trade updates, new product launches, and seasonal offers.</p>
      <form style="display:flex; gap:8px; margin-bottom:0;" onsubmit="return false;">
        <input type="email" placeholder="Your email address" style="flex:1; padding:12px 16px; border-radius:8px; border:1px solid rgba(255,255,255,.2); background: rgba(255,255,255,.08); color: #FFFFFF; font-size: 14px; font-family: var(--font-sans);">
        <button type="submit" style="padding:12px 20px; border-radius:8px; background: linear-gradient(135deg, #C0C080, #E0E0C0); color: #004040; font-size: 14px; font-weight: 700; font-family: var(--font-sans); border: none; cursor: pointer;">Subscribe</button>
      </form>
    </div>
'''

# Find the footer-brand opening and insert newsletter after it
marker3 = '<div class="footer-brand">'
html = html.replace(marker3, '<div class="footer-brand">' + newsletter_html, 1)

with open('index.html', 'w') as f:
    f.write(html)

print("HTML updated with 3 premium components.")
print("Testimonials:", "Testimonials" in html)
print("FAQ:", "FAQ" in html)
print("Newsletter:", "Stay in Touch" in html)
print("File size:", len(html), "bytes")
