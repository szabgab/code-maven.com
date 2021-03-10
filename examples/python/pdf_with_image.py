from reportlab.pdfgen import canvas

img_file = '../../static/img/code_maven_440x440.png'
pdf_file = 'hello_world.pdf'

can = canvas.Canvas(pdf_file)
can.drawString(20, 400, "Hello World!")

x_start = 0
y_start = 0
can.drawImage(img_file, x_start, y_start, width=120, preserveAspectRatio=True, mask='auto')

can.showPage()
can.save()

