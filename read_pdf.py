import pymupdf
doc = pymupdf.open('/c/Users/Thabang/Downloads/sdodla/Hills Artesian Spring Trade Presenter.pdf')
print('Pages:', len(doc))
for i, page in enumerate(doc):
    print(f'=== PAGE {i+1} ===')
    print(page.get_text())
    print()
