import pytest
import os
import sys
from unittest.mock import patch, mock_open, MagicMock
from pdf_parser import extract_text_from_pdf, main
import PyPDF2


class TestExtractTextFromPDF:
    """Test cases for extract_text_from_pdf function"""
    
    def test_file_not_found(self, capsys):
        """Test handling of non-existent file"""
        result = extract_text_from_pdf("nonexistent_file.pdf")
        
        assert result is None
        captured = capsys.readouterr()
        assert "Error: File 'nonexistent_file.pdf' not found!" in captured.out
    
    def test_invalid_file_extension(self, capsys):
        """Test handling of non-PDF file"""
        # Create a temporary text file
        test_file = "test_file.txt"
        with open(test_file, 'w') as f:
            f.write("test content")
        
        try:
            result = extract_text_from_pdf(test_file)
            
            assert result is None
            captured = capsys.readouterr()
            assert "is not a PDF file!" in captured.out
        finally:
            # Cleanup
            if os.path.exists(test_file):
                os.remove(test_file)
    
    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data=b'mock pdf content')
    @patch('PyPDF2.PdfReader')
    def test_successful_extraction_single_page(self, mock_pdf_reader, mock_file, mock_exists, capsys):
        """Test successful text extraction from single-page PDF"""
        # Mock PDF reader and page
        mock_page = MagicMock()
        mock_page.extract_text.return_value = "This is test text from page 1"
        
        mock_reader_instance = MagicMock()
        mock_reader_instance.pages = [mock_page]
        mock_pdf_reader.return_value = mock_reader_instance
        
        test_pdf = "test_single.pdf"
        result = extract_text_from_pdf(test_pdf)
        
        assert result is not None
        assert "Page 1" in result
        assert "This is test text from page 1" in result
        
        captured = capsys.readouterr()
        assert "Total Pages: 1" in captured.out
        assert "Extraction Complete!" in captured.out
    
    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data=b'mock pdf content')
    @patch('PyPDF2.PdfReader')
    def test_successful_extraction_multiple_pages(self, mock_pdf_reader, mock_file, mock_exists, capsys):
        """Test successful text extraction from multi-page PDF"""
        # Mock PDF reader and pages
        mock_page1 = MagicMock()
        mock_page1.extract_text.return_value = "Text from page 1"
        
        mock_page2 = MagicMock()
        mock_page2.extract_text.return_value = "Text from page 2"
        
        mock_page3 = MagicMock()
        mock_page3.extract_text.return_value = "Text from page 3"
        
        mock_reader_instance = MagicMock()
        mock_reader_instance.pages = [mock_page1, mock_page2, mock_page3]
        mock_pdf_reader.return_value = mock_reader_instance
        
        test_pdf = "test_multi.pdf"
        result = extract_text_from_pdf(test_pdf)
        
        assert result is not None
        assert "Page 1" in result
        assert "Page 2" in result
        assert "Page 3" in result
        assert "Text from page 1" in result
        assert "Text from page 2" in result
        assert "Text from page 3" in result
        
        captured = capsys.readouterr()
        assert "Total Pages: 3" in captured.out
    
    @patch('os.path.exists', return_value=True)
    @patch('builtins.open', new_callable=mock_open, read_data=b'mock pdf content')
    @patch('PyPDF2.PdfReader')
    def test_pdf_reader_exception(self, mock_pdf_reader, mock_file, mock_exists, capsys):
        """Test handling of PDF reading exceptions"""
        mock_pdf_reader.side_effect = Exception("Corrupted PDF file")
        
        test_pdf = "test_error.pdf"
        result = extract_text_from_pdf(test_pdf)
        
        assert result is None
        captured = capsys.readouterr()
        assert "Error processing PDF:" in captured.out
        assert "Corrupted PDF file" in captured.out


class TestMainFunction:
    """Test cases for main function"""
    
    @patch('pdf_parser.extract_text_from_pdf')
    @patch('sys.argv', ['pdf_parser.py'])
    def test_main_with_default_path(self, mock_extract, capsys):
        """Test main function with default PDF path"""
        mock_extract.return_value = "Sample extracted text"
        
        main()
        
        captured = capsys.readouterr()
        assert "No PDF path provided" in captured.out
        assert "Using default:" in captured.out
        mock_extract.assert_called_once()
    
    @patch('pdf_parser.extract_text_from_pdf')
    @patch('sys.argv', ['pdf_parser.py', 'custom_file.pdf'])
    def test_main_with_custom_path(self, mock_extract):
        """Test main function with custom PDF path from command line"""
        mock_extract.return_value = "Sample extracted text"
        
        main()
        
        mock_extract.assert_called_once_with('custom_file.pdf')
    
    @patch('pdf_parser.extract_text_from_pdf')
    @patch('builtins.open', new_callable=mock_open)
    @patch('sys.argv', ['pdf_parser.py', 'test.pdf'])
    def test_main_saves_output_file(self, mock_file, mock_extract, capsys):
        """Test that main function saves extracted text to file"""
        mock_extract.return_value = "Extracted text content"
        
        main()
        
        # Verify file write was attempted
        mock_file.assert_called()
        captured = capsys.readouterr()
        assert "Text also saved to:" in captured.out
    
    @patch('pdf_parser.extract_text_from_pdf')
    @patch('sys.argv', ['pdf_parser.py', 'test.pdf'])
    def test_main_no_text_extracted(self, mock_extract, capsys):
        """Test main function when extraction fails"""
        mock_extract.return_value = None
        
        main()
        
        captured = capsys.readouterr()
        assert "Text also saved to:" not in captured.out


class TestIntegration:
    """Integration tests with actual PDF files (if available)"""
    
    @pytest.mark.skipif(not os.path.exists('file-sample.pdf'), 
                        reason="file-sample.pdf not found")
    def test_real_pdf_file_sample(self, capsys):
        """Test with actual file-sample.pdf if it exists"""
        result = extract_text_from_pdf('file-sample.pdf')
        
        assert result is not None
        assert len(result) > 0
        
        captured = capsys.readouterr()
        assert "Extraction Complete!" in captured.out
    
    @pytest.mark.skipif(not os.path.exists('rotated-sample.pdf'), 
                        reason="rotated-sample.pdf not found")
    def test_real_pdf_rotated_sample(self, capsys):
        """Test with actual rotated-sample.pdf if it exists"""
        result = extract_text_from_pdf('rotated-sample.pdf')
        
        assert result is not None
        assert len(result) > 0
        
        captured = capsys.readouterr()
        assert "Extraction Complete!" in captured.out


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
