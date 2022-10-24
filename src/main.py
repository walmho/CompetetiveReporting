from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import txtTemplate, pdfTemplate
from sendReport.sendOff import pdfOut

location = {"city":"Hillsboro", "state":"Oregon", "country":"US"}

if __name__ == "__main__":
    outFile = "outputs/output.txt"
    templateFile = "templates/mainLayout.html"
    status, ppN, ratings = get_page(location["city"], location["state"], location["country"], debug=False)

    pdfOutput = pdfTemplate(ppN, ratings, location)
    pdfOutput.loadTemplate()
    pdfOut("outputs/outputTest.html", "outputs/report.pdf")

    # txtTemplate.dateReport(outFile)
    # for index in range(len(ppN)):
    #     basic = txtTemplate.createBase("basics.txt", index+1, ppN[index], ratings[index])
    #     txtTemplate.printOut(outFile, basic)
