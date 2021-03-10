from reportlab.pdfgen import canvas


def create_pdf():
    pdf_file = 'multipage.pdf'

    can = canvas.Canvas(pdf_file)

    can.drawString(20, 800, "First Page")
    can.showPage()

    can.drawString(20, 800, "Second Page")
    can.showPage()

    can.drawString(20, 700, "Third Page")
    can.showPage()

    can.save()

create_pdf()


