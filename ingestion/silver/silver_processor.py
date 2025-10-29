from langchain_text_splitters import RecursiveCharacterTextSplitter

class SilverProcessor:
    def process_chunks(self, docs):
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = splitter.split_documents(docs)
        print(f"⚪ Silver: {len(chunks)} chunks gerados")
        return chunks
