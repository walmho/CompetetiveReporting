import jinja2
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
    def loadTemplate(template, index, value, rating):
        template_loader = jinja2.FileSystemLoader(searchpath="./")
        template_env = jinja2.Environment(loader=template_loader)
        template_file = template
        template = template_env.get_template(template_file)
        output_text = template.render(
            name=index,
            address=value,
            date=datetime.now(),
            invoice=rating,
            item=rating,
            amount=rating,
            )

        html_path = template
        html_file = open(html_path, 'w')
        html_file.write(output_text)
        html_file.close()