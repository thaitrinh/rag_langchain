# Simple RAG with LangChain, Ollama, and Chroma

This project demonstrates a simple Retrieval-Augmented Generation (RAG) pipeline using [LangChain](https://python.langchain.com/), [Ollama](https://ollama.com/), and [Chroma](https://www.trychroma.com/). It loads a PDF, creates embeddings, stores them in a vector database, and answers questions using a local LLM via Ollama.

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com/) (for running local LLMs)
- The packages listed in [requirements.txt](requirements.txt)

## Setup

1. **Clone this repository and navigate to the project folder:**

   ```sh
   git clone <your-repo-url>
   cd rag_langchain
   ```

2. **Install Python dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Install Ollama:**

   - Follow the instructions for your OS at [https://ollama.com/download](https://ollama.com/download)
   - Start Ollama by running:
     ```sh
     ollama serve
     ```

4. **Pull the required models:**

   - For embeddings:
     ```sh
     ollama pull nomic-embed-text
     ```
   - For LLM (e.g., gemma3:4b):
     ```sh
     ollama pull gemma3:4b
     ```

5. **Add your PDF file:**

   - Place your PDF (e.g., `englisch_stag.pdf`) in the `data/` directory.

## Usage

Run the script:

```sh
python simple_rag.py
```

This will load the PDF, create embeddings, and answer the sample query:
> What are the conditions to get German citizenship?

## File Structure

- `simple_rag.py` — Main script for RAG pipeline
- `requirements.txt` — Python dependencies
- `data/englisch_stag.pdf` — Example PDF document

## Notes

- Make sure Ollama is running before executing the script.
- You can change the query in `simple_rag.py` to ask different questions.

## References

- [LangChain Documentation](https://python.langchain.com/)
- [Ollama Documentation](https://ollama.com/docs)
- [Chroma Documentation](https://docs.trychroma.com/)