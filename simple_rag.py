from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA


# load documents
loader = PyPDFLoader("data/englisch_stag.pdf")
documents = loader.load()

# create embeddings
embeddings = OllamaEmbeddings(model="nomic-embed-text")  # or use SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# combine documents with embeddings to create vectorstore
# embeddings are used to calculate similarity, documents are used to retrieve relevant text
vectorstore  = Chroma.from_documents(documents, embeddings)

# Set up the local LLM via Ollama
llm = OllamaLLM(model="gemma3:4b")

# create QA chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

# Query your RAG app
query = "What are the conditions to get German citizenship?"
result = rag_chain.invoke(query)
print(result['result'])