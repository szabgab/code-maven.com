from reportlab.pdfgen import canvas

pdf_file = 'hello_world_fonts.pdf'

can = canvas.Canvas(pdf_file)

print(can.getAvailableFonts())
# 'Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique',
# 'Helvetica', 'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique',
# 'Symbol',
# 'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman',
# 'ZapfDingbats'

can.setFont("Helvetica", 24)
can.drawString(20, 400, "Hello")
can.drawString(40, 360, "World")

can.setFont("Courier", 16)
can.drawString(60, 300, "How are you?")

can.showPage()
can.save()

