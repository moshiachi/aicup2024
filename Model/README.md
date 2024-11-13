# Model

This directory contains the `retrieval.py` script, which implements the retrieval logic using the Voyage AI model. The retrieval process leverages embeddings and reranking to match user queries with the most relevant documents.

## Files

- **retrieval.py**: Contains the `voyage_retrieve` function, responsible for embedding and reranking documents to find the best match for a given query.

## Functions

### `voyage_retrieve(qs, source, corpus_dict)`

- **Description**: Uses the Voyage model to retrieve the document most relevant to the query by embedding documents and reranking them based on similarity.
- **Arguments**:
  - `qs` (str): The query string.
  - `source` (list): List of document IDs within the source collection to search.
  - `corpus_dict` (dict): A dictionary mapping document IDs to their text content.
- **Returns**: The document ID of the best-matching document, or `None` if no relevant match is found.

## Requirements

To use the Voyage model, ensure the `voyageai` library is installed, and set the `VOYAGE_API_KEY` environment variable with your API key.

## Usage Example

```python
from retrieval import voyage_retrieve

# Define a query and document corpus
query = "Example query text"
source_docs = [1, 2, 3]  # Document IDs to search within
corpus_dict = {
    1: "Document 1 text",
    2: "Document 2 text",
    3: "Document 3 text"
}

# Retrieve the best matching document ID
result_id = voyage_retrieve(query, source_docs, corpus_dict)
print("Best matching document ID:", result_id)
```

In this example, voyage_retrieve will return the ID of the document that best matches the query based on embeddings and reranking.

