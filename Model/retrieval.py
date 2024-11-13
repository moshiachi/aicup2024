import voyageai

# Initialize Voyage Client
vo = voyageai.Client()  # Ensure VOYAGE_API_KEY is set in environment variables

def voyage_retrieve(qs, source, corpus_dict):
    """
    Performs retrieval using the Voyage model to find the best-matching document.

    Args:
        qs (str): Query string.
        source (list): List of source document IDs.
        corpus_dict (dict): Dictionary with document IDs and their text content.

    Returns:
        int or None: ID of the best-matching document, or None if no match found.
    """
    filtered_corpus = [corpus_dict[int(file)].strip() for file in source if corpus_dict[int(file)].strip()]
    
    if not filtered_corpus:
        print("Error: All documents in filtered_corpus are empty.")
        return None

    try:
        embedded_documents = vo.embed(filtered_corpus, model="voyage-3", input_type="document")
    except Exception as e:
        print("Error during embedding:", e)
        return None

    try:
        reranking = vo.rerank(qs, filtered_corpus, model="rerank-2", top_k=1)
        if reranking.results:
            best_doc = reranking.results[0].document
        else:
            print("No results from reranking.")
            return None
    except Exception as e:
        print("Error during reranking:", e)
        return None

    res = [key for key, value in corpus_dict.items() if value.strip() == best_doc.strip()]
    return res[0] if res else None
