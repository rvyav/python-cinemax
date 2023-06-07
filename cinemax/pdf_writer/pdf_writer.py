from fpdf import FPDF
from datetime import datetime

TITLE = "Invoice"


class PDF:
    def writer(self):
        pdf = FPDF()
        pdf.add_page()
        self.header(pdf)
        self.body(pdf)
        pdf.output("{}.pdf".format(TITLE.lower()), "F")

    def header(self, pdf: FPDF, name: str):
        bill_to = "Bill to: {}".format(name)
        # Set the page title
        pdf.set_title(bill_to)

        # Set the font style and size
        pdf.set_font("Arial", "B", 14)

        # Add the invoice date and title to the page
        today = datetime.now().strftime("%m/%d/%Y")
        pdf.cell(0, 10, bill_to, 0, 0, "L")
        pdf.cell(0, 10, "{}", 0, 0, "R".format(today))
        pdf.ln()

        # Set the font style and size for the table headers
        pdf.set_font("Arial", "B", 12)

    def body(self, pdf: FPDF, movie: str, seat_number: str, seat_price: str):
        seat_price = "${}".format(seat_number)
        # Set the font style and size for the table headers
        pdf.set_font("Arial", "B", 12)

        # Add the table headers
        pdf.cell(50, 10, "Movie", 1)
        pdf.cell(50, 10, "Price", 1)
        pdf.cell(50, 10, "Seat", 1)
        pdf.cell(50, 10, "Total", 1)
        pdf.ln()

        # Set the font style and size for the table rows
        pdf.set_font("Arial", "", 12)

        # Add the movie ticket details to the table
        pdf.cell(50, 10, movie, 1)
        pdf.cell(50, 10, seat_price, 1)
        pdf.cell(50, 10, seat_number, 1)
        pdf.cell(50, 10, seat_price, 1)
        pdf.ln()

        # Add the total amount due
        pdf.cell(150, 10, "Total:", 1, 0, "R")
        pdf.cell(50, 10, seat_price, 1)

    def footer(self, pdf: FPDF):
        pass


if __name__ == "__main__":
    pdf = PDF()
    pdf.writer()
