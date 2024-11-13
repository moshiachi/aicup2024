# 2024 玉山人工智慧公開挑戰賽 - 初賽資格審查

This repository contains the code required to reproduce the preliminary results for the 2024 玉山人工智慧公開挑戰賽. The repository is structured as follows:

## Directory Structure

- `Preprocess/`
  - `data_preprocess.py`: Handles data loading and text extraction from PDF files, including OCR for image-based text.
- `Model/`
  - `retrieval.py`: Implements the retrieval logic using the Voyage model.
- `main.py`: Main script that combines preprocessing and retrieval to output results.
- `requirements.txt`: Lists Python libraries and versions required to run the code.
- `README.md`: Explains the structure and usage of the repository.

## Setup

Python version: 3.10.12

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
    ```
2. **Set Environment Variable**:
    Ensure VOYAGE_API_KEY is set in the environment variables:
    ```bash
    export VOYAGE_API_KEY="<your secret key>"
    ```

## Usage
Run the retrieval process by specifying paths to the questions, source documents, and output file:

```bash
python3 main.py --question_path path/to/questions.json --source_path path/to/source_documents --output_path path/to/output.
```
---

#### Model and API Setup

- **API Provider**: Voyage AI
- **Embedding Model**: `voyage-3` – Used to embed document texts for semantic matching.
- **Reranking Model**: `rerank-2` – Used to rerank documents based on similarity to the query.
- **API Key**: Accessed via `VOYAGE_API_KEY` environment variable for secure authentication.

#### Hyperparameters and Configurations

- **top_k**: Set to `1` in `rerank` function to retrieve the single most relevant document for each query.

#### Environment

- **Libraries**: 
  - `pdfplumber` – for text extraction from PDFs.
  - `pdf2image` and `pytesseract` – for OCR processing on image-based PDFs.
  - `voyageai` – for interaction with the Voyage AI API.
  - `tqdm` and `jieba` – for progress indication and Chinese word segmentation.

#### Official Documents about Voyage AI:

- **API Key and Python Client**: 
https://docs.voyageai.com/docs/api-key-and-installation

- **Text Embeddings**: 
https://docs.voyageai.com/docs/embeddings

- **Rerankers**: 
https://docs.voyageai.com/docs/reranker

---