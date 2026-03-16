from app.services.pdf_loader import load_pdf
from app.services.chunker import chunk_text
from app.services.vector_store import create_vector_store
from app.services.llm_service import get_llm
from app.config import PDF_PATH

# ---- Load & prepare once at startup ----
_pdf_text = load_pdf(PDF_PATH)
_chunks = chunk_text(_pdf_text)
_vector_store = create_vector_store(_chunks)
_llm = get_llm()

# ---- RAG Logic ----
def get_answer(query: str) -> str:
    docs = _vector_store.similarity_search(query, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer ONLY from the context below.
If the answer is not present, say "Information not available in the document".

Context:
{context}

Question:
{query}
"""
    response = _llm.invoke(prompt)
    return response.content
