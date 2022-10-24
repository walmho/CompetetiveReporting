from jinja2 import Environment, FileSystemLoader
import pandas as pd
from datetime import datetime
import pdfkit

config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

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
    def __init__(self, ppN, ratings, location):
        self.ppN = ppN
        self.average = float(sum(ppN)/(len(ppN)))
        self.ratings = ratings
        self.city = location["city"]
        self.state = location["state"]
        self.country = location["country"]

    def loadTemplate(self):
        template_loader = FileSystemLoader(searchpath="./templates")
        template_env = Environment(loader=template_loader)
        template_file = "test.html"
        template = template_env.get_template(template_file)
        output_text = template.render(
            city=self.city,
            state=self.state,
            country=self.country,
            time=datetime.now(),
            averagePrice=self.average,

        )

        html_path = "./outputs/updated.html"
        html_file = open(html_path, 'w+')
        html_file.write(output_text)
        html_file.close()
