from weasyprint import HTML
def printOut(file, data):
    HTML(string=data).write_pdf(file)