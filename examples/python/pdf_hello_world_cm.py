from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf_file = 'hello_world_cm.pdf'

can = canvas.Canvas(pdf_file)
can.drawString(2*cm, 20*cm, "Hello World!")
can.showPage()
can.save()

