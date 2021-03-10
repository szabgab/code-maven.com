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

def add_image():

    from PyPDF2 import PdfFileWriter, PdfFileReader
    import io

    in_pdf_file = 'multipage.pdf'
    out_pdf_file = 'with_image.pdf'
    img_file = '../../static/img/code_maven_440x440.png'

    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    #can.drawString(10, 100, "Hello world")
    x_start = 0
    y_start = 0
    can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')
    can.showPage()
    can.showPage()
    can.showPage()
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    new_pdf = PdfFileReader(packet)

    # read the existing PDF
    existing_pdf = PdfFileReader(open(in_pdf_file, "rb"))
    output = PdfFileWriter()

    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.getPage(i)
        page.mergePage(new_pdf.getPage(i))
        output.addPage(page)

    outputStream = open(out_pdf_file, "wb")
    output.write(outputStream)
    outputStream.close()


create_pdf()
add_image()

