from jinja2 import Environment, FileSystemLoader

#Should turn this into a class
def createBase(txtFile, index, value, rating):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(txtFile)
    out = template.render(number=index, price=value, star=rating)
    return out

def printOut(file, line):
    with open(file, 'w') as f:
        f.write(f"{line}\n")