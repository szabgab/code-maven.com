from reportlab.pdfgen import canvas
from reportlab.rl_config import defaultPageSize
print(defaultPageSize)  # (595.2755905511812, 841.8897637795277)

WIDTH, HEIGHT = defaultPageSize

pdf_file = 'pagesize.pdf'

can = canvas.Canvas(pdf_file)

can.drawString(WIDTH/4, HEIGHT-20, "WIDTH:{} HEIGHT:{}".format(WIDTH, HEIGHT))
can.showPage()
can.save()

