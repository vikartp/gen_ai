import PyPDF2
import sys
import os

def extract_text_from_pdf(pdf_path):
    """
    Extract and print text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
    
    Returns:
        str: Extracted text from the PDF
    """
    try:
        # Check if file exists
        if not os.path.exists(pdf_path):
            print(f"Error: File '{pdf_path}' not found!")
            return None
        
        # Check if it's a PDF file
        if not pdf_path.lower().endswith('.pdf'):
            print(f"Error: '{pdf_path}' is not a PDF file!")
            return None
        
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Get number of pages
            num_pages = len(pdf_reader.pages)
            print(f"\n{'='*60}")
            print(f"PDF File: {os.path.basename(pdf_path)}")
            print(f"Total Pages: {num_pages}")
            print(f"{'='*60}\n")
            
            # Extract text from all pages
            full_text = ""
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                
                print(f"\n--- Page {page_num + 1} ---\n")
                print(page_text)
                
                full_text += f"\n--- Page {page_num + 1} ---\n{page_text}\n"
            
            print(f"\n{'='*60}")
            print(f"Extraction Complete!")
            print(f"{'='*60}\n")
            
            return full_text
            
    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return None

def main():
    # Mock file path - Replace this with your actual PDF path
    default_pdf_path = "../kongsberg/logiCoT-paper.pdf"
    
    # Check if user provided a path as command line argument
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = default_pdf_path
        print(f"No PDF path provided. Using default: {default_pdf_path}")
        print(f"Usage: python pdf_parser.py <path_to_pdf_file>\n")
    
    # Extract and print text
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Optional: Save to a text file
    if extracted_text:
        output_file = pdf_path.replace('.pdf', '_extracted.txt')
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            print(f"Text also saved to: {output_file}")
        except Exception as e:
            print(f"Could not save to file: {str(e)}")

if __name__ == "__main__":
    main()
