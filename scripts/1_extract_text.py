import fitz  # PyMuPDF

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    text = extract_text("data\Deep Learning with Python.pdf")
    with open("scripts/full_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("✅ تم استخراج النص بنجاح")
