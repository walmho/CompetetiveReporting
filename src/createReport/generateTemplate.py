from jinja2 import Environment, FileSystemLoader

def createBase(txtFile, index, value, rating):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template(txtFile)
    out = template.render(number=index, price=value, star=rating)
    return out
