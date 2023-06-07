from fpdf import FPDF

TITLE = "Invoice"


class PDF:
    def writer(self):
        pdf = FPDF()
        pdf.add_page()
        self.header(pdf)
        self.body(pdf)
        pdf.output("{}.pdf".format(TITLE.lower()), "F")

    def header(self, pdf: FPDF):
        # Set the page title
        pdf.set_title("Invoice for John")

        # Set the font style and size
        pdf.set_font("Arial", "B", 14)

        # Add the invoice date and title to the page
        pdf.cell(0, 10, "Invoice for John", 0, 0, "L")
        pdf.cell(0, 10, "Date: 2022-02-28", 0, 0, "R")
        pdf.ln()

        # Set the font style and size for the table headers
        pdf.set_font("Arial", "B", 12)

    def body(self, pdf: FPDF):
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
        pdf.cell(50, 10, "Indiana Jones", 1)
        pdf.cell(50, 10, "$20.00", 1)
        pdf.cell(50, 10, "A31", 1)
        pdf.cell(50, 10, "$20.00", 1)
        pdf.ln()

        # Add the total amount due
        pdf.cell(150, 10, "Total:", 1, 0, "R")
        pdf.cell(50, 10, "$20.00", 1)

    def footer(self, pdf: FPDF):
        pass


if __name__ == "__main__":
    pdf = PDF()
    pdf.writer()
