import pymupdf
import os

pdf_path = r"C:\Users\Thabang\Desktop\sdoabla.pdf"
print("Checking file exists:", os.path.exists(pdf_path))
print("File size:", os.path.getsize(pdf_path))

doc = pymupdf.open(pdf_path)
print('Pages:', len(doc))
for i, page in enumerate(doc):
    print(f'=== PAGE {i+1} ===')
    print(page.get_text())
    print()
