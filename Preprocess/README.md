# Preprocess

This directory contains the `data_preprocess.py` script, which is responsible for loading and preprocessing text data from PDF files. It supports both direct text extraction and OCR (Optical Character Recognition) for cases where PDF content is stored as images.

## Files

- **data_preprocess.py**: Contains functions to load and preprocess text data from PDFs.

## Functions

### `load_data(source_path)`

- **Description**: Iterates through all PDF files in the specified directory and extracts their text content.
- **Arguments**:
  - `source_path` (str): Path to the directory containing PDF files.
- **Returns**: A dictionary with document IDs as keys and extracted text content as values.

### `read_pdf(pdf_loc, page_infos=None)`

- **Description**: Reads and extracts text from a single PDF file. If text extraction fails, it uses OCR to extract text from images within the PDF.
- **Arguments**:
  - `pdf_loc` (str): Path to the PDF file.
  - `page_infos` (list, optional): Specifies a range of pages to extract.
- **Returns**: A string containing the extracted text from the PDF.

## Requirements

Ensure you have the following libraries installed:
- `pdfplumber`
- `pdf2image`
- `pytesseract`

## Usage Example

```python
from data_preprocess import load_data

# Load data from a directory of PDF files
source_path = 'path/to/pdf_directory'
corpus_dict = load_data(source_path)
```
The processed text content is returned as a dictionary, which can be used for retrieval tasks.