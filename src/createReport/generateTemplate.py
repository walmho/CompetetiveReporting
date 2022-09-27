from jinja2 import Environment, FileSystemLoader

def createBase(txtFile):
    loader=FileSystemLoader("templates/")
    environment = Environment(loader)
    template = environment.get_template(txtFile)
    template.render()
    return template
