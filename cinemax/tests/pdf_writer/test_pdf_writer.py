from unittest.mock import MagicMock
import tempfile
from cinemax.pdf_writer.pdf_writer import PDF


def test_writer():
    with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as file:
        # Create a MagicMock instance of the PDF class
        pdf_mock = MagicMock(spec=PDF)
        pdf_mock.header = MagicMock()
        pdf_mock.body = MagicMock()
        pdf_mock.output = MagicMock(return_value=file)

        # Call writer method
        pdf_mock.writer("John Doe", "Booksmart", "C12", "$10.00")

        # Assert that the header and body methods were called once
        pdf_mock.header.assert_called_once_with(pdf_mock, "John Doe")
        pdf_mock.body.assert_called_once_with(pdf_mock, "Booksmart", "C12", "$10.00")

        # Assert that the output method was called once with the correct argument
        pdf_mock.output.assert_called_once_with("F")

        # Assert that the output file contains the expected content
        with open(file.name, "rb") as f:
            content = f.read()
            assert b"Invoice for John Doe" in content
            assert b"Book: Booksmart" in content
            assert b"Code: C12" in content
            assert b"Price: $10.00" in content
