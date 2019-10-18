from reportlab.pdfgen import canvas

pdf_file = 'hello_world.pdf'

can = canvas.Canvas(pdf_file)
can.drawString(20, 400, "Hello World!")
can.showPage()
can.save()

