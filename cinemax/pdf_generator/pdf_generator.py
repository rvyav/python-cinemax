from fpdf import FPDF

TITLE = "Invoice"


class PDF:
    def generate(self):
        pdf = FPDF()
        self.header(pdf)
        pdf.output("{}.pdf".format(TITLE.lower()), "F")

    def header(self, pdf: FPDF):
        pdf.add_page()
        pdf.set_font("Arial", "B", 40)
        pdf.cell(60, 10, "Invoice")
        pdf.cell(60, 98, "Bill To: ", ln=True)

    def body():
        pass

    def footer():
        pass


if __name__ == "__main__":
    pdf = PDF()
    pdf.generate()
