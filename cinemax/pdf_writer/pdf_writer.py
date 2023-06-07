from fpdf import FPDF
from datetime import date

TITLE = "Invoice"


class PDF:
    def writer(self, name, movie, seat_number, seat_price):
        pdf = FPDF()
        pdf.add_page()
        self.header(pdf, name)
        self.body(pdf, movie, seat_number, seat_price)
        pdf.output("{}.pdf".format(TITLE.lower()), "F")

    def header(self, pdf: FPDF, name: str):
        bill_to = "Bill to: {}".format(name)
        # Set the page title
        pdf.set_title(bill_to)

        # Set the font style and size
        pdf.set_font("Arial", "B", 14)

        # Add the invoice date and title to the page
        today = date.today().strftime("%m/%d/%Y")
        pdf.cell(0, 10, bill_to, 0, 0, "L")
        pdf.cell(0, 10, today, 0, 0, "R")
        pdf.ln()

        # Set the font style and size for the table headers
        pdf.set_font("Arial", "B", 12)

    def body(self, pdf: FPDF, movie: str, seat_number: str, seat_price: str):
        seat_price = "${}".format(seat_price)
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
    pdf.writer("Ema", "Adele", "B32", "19.99")
