import os
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm

def load_data(source_path):
    """
    Loads and preprocesses all PDF files in the specified directory.
    
    Args:
        source_path (str): Path to the directory containing PDF files.

    Returns:
        dict: A dictionary mapping file IDs to their extracted text content.
    """
    masked_file_ls = os.listdir(source_path)
    corpus_dict = {
        int(file.replace('.pdf', '')): read_pdf(os.path.join(source_path, file)) for file in tqdm(masked_file_ls)
    }
    return corpus_dict

def read_pdf(pdf_loc, page_infos=None):
    """
    Reads and extracts text from a PDF file. Uses OCR if text extraction fails.

    Args:
        pdf_loc (str): Path to the PDF file.
        page_infos (list, optional): Page range to extract; extracts all pages if None.

    Returns:
        str: Extracted text content from the PDF file.
    """
    pdf_text = ''
    pdf = pdfplumber.open(pdf_loc)
    
    pages = pdf.pages[page_infos[0]:page_infos[1]] if page_infos else pdf.pages
    for page_num, page in enumerate(pages):
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"
        else:
            print(f"Performing OCR on page {page_num + 1} of {pdf_loc}")
            images = convert_from_path(pdf_loc, first_page=page_num + 1, last_page=page_num + 1)
            for image in images:
                ocr_text = pytesseract.image_to_string(image, lang='eng')
                pdf_text += ocr_text + "\n"

        tables = page.extract_tables()
        for table in tables:
            table_text = ""
            for row in table:
                row_text = " | ".join(str(cell) for cell in row if cell)
                table_text += row_text + "\n"
            pdf_text += table_text
    
    pdf.close()
    return pdf_text
