# PDF Parser

A Python utility for extracting text from PDF files, including support for rotated text.

## Features

- Extract text from all pages of a PDF file
- Print text to console with page numbers
- Save extracted text to a `.txt` file
- Support for command-line arguments or default file path
- Handles rotated text in PDFs

## Prerequisites

- **Python** 3.10 or higher

## Setup

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

- **Windows:** `venv\Scripts\activate`
- **Linux/Mac:** `source venv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Using Command Line Argument

```bash
python pdf_parser.py path/to/your/file.pdf
```

### Using Default Path

Edit the `default_pdf_path` variable in `pdf_parser.py` to point to your PDF file, then run:

```bash
python pdf_parser.py
```

### Example

```bash
python pdf_parser.py "C:\Users\YourName\Documents\sample.pdf"
```

## Output

- The extracted text will be printed to the console with page numbers
- A text file with the extracted content will be saved as `<original_filename>_extracted.txt`

## Testing

```bash
pytest test_pdf_parser.py
```

## Key Files

| File | Description |
|------|-------------|
| `pdf_parser.py` | Main PDF parsing script |
| `requirements.txt` | Python dependencies |
| `test_pdf_parser.py` | Unit tests |
| `file-sample.pdf` | Sample PDF for testing |
| `rotated-text-sample.pdf` | Sample PDF with rotated text |

## Notes

- Generated text files (`*_extracted.txt`) are gitignored and NOT committed
- PyPDF2

## Error Handling

The application handles:
- File not found errors
- Invalid PDF files
- Extraction errors with helpful error messages
