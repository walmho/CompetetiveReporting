from jinja2 import Environment, FileSystemLoader
import pandas as pd
from datetime import datetime

class txtTemplate():
    def createBase(txtFile, index, value, rating):
        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)
        template = env.get_template(txtFile)
        out = template.render(number=index, price=value, star=rating)
        return out

    def printOut(file, data):
        with open(file, 'a+') as f:
            # Clears any current report. May want to make an archive folder instead and move any previous content there
            f.write(f"{data}\n")

    def dateReport(file):
        with open(file, 'w') as f:
            f.write(f"Report generated at {datetime.now()}\n")

class pdfTemplate():
    def loadTemplate(template, value, rating):
        x = value[0]
        y = rating[0]
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(template)
