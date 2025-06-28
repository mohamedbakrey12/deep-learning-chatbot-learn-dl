from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_text(text)

if __name__ == "__main__":
    with open("scripts/full_text.txt", encoding="utf-8") as f:
        text = f.read()
    
    chunks = chunk_text(text)

    with open("scripts/chunks.txt", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n\n---\n\n")

    print(f"✅ تم إنشاء {len(chunks)} جزء (chunk)")
