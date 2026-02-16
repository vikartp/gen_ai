# PDF Parser

A simple Python application to extract and print text from PDF files.

## Features

- Extract text from all pages of a PDF file
- Print text to console with page numbers
- Save extracted text to a .txt file
- Support for command-line arguments or default file path

## Installation

1. Install Python (if not already installed)
2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Using Command Line Argument

```bash
python pdf_parser.py path/to/your/file.pdf
```

### Method 2: Using Default Path

Edit the `default_pdf_path` variable in `pdf_parser.py` to point to your PDF file, then run:

```bash
python pdf_parser.py
```

## Example

```bash
python pdf_parser.py "C:\Users\YourName\Documents\sample.pdf"
```

## Output

- The extracted text will be printed to the console with page numbers
- A text file with the extracted content will be saved as `<original_filename>_extracted.txt`

## Requirements

- Python 3.6+
- PyPDF2

## Error Handling

The application handles:
- File not found errors
- Invalid PDF files
- Extraction errors with helpful error messages
