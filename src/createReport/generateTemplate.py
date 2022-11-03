from jinja2 import Environment, FileSystemLoader
import pandas as pd
from datetime import datetime
import pdfkit

from createReport.addAnalysis import expensiveRatings

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
    def __init__(self, totalScraped, ratings, location, averagePPN, unrated, expensivePercentile, expensiveReviews, mostExpensive, cheapPercentile, cheapReviews, leastExpensive, imageLocation, imageAlt):
        self.average = averagePPN
        self.ratings = ratings
        self.unrated = unrated
        self.totalScraped = totalScraped

        self.expensivePercentile = expensivePercentile
        self.expensiveReviews = expensiveReviews
        self.cheapPercentile = cheapPercentile
        self.cheapReviews = cheapReviews

        self.mostExpensive = mostExpensive
        self.leastExpensive = leastExpensive

        self.graph = imageLocation
        self.alternateText = imageAlt

        self.city = location["city"]
        self.state = location["state"]
        self.country = location["country"]

    def loadTemplate(self):
        """ Fills template file with updated variables

        Returns:
            Writes to a proxy html file with new data
        """
        template_loader = FileSystemLoader(searchpath="./templates")
        template_env = Environment(loader=template_loader)
        template_file = "mainLayout.html"
        template = template_env.get_template(template_file)
        output_text = template.render(
            city=self.city,
            state=self.state,
            country=self.country,
            time=datetime.now(),
            averagePrice=self.average,
            unratedHouses = self.unrated,
            totalScrapedHouses = (self.totalScraped*20),

            expensivePercentile = self.expensivePercentile,
            expensiveRatingAverage = self.expensiveReviews,
            expensivePrice = self.mostExpensive,
            
            cheapPercentile = self.cheapPercentile,
            cheapRatingAverage = self.cheapReviews,
            cheapPrice = self.leastExpensive,

            source = self.graph,
            alt = self.alternateText

        ) 

        html_path = "./outputs/updated.html"
        html_file = open(html_path, 'w+')
        html_file.write(output_text)
        html_file.close()
