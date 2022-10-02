from jinja2 import Environment, FileSystemLoader
from datetime import datetime

#Should turn this into a class
def createBase(txtFile, index, value, rating):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(txtFile)
    out = template.render(number=index, price=value, star=rating)
    return out

def printOut(file, line):
    with open(file, 'a+') as f:
        # Clears any current report. May want to make an archive folder instead and move any previous content there
        f.write(f"{line}\n")

def dateReport(file):
    with open(file, 'w') as f:
        f.write(f"\nReport generated at {datetime.now()}\n")
