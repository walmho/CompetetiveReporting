from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import txtTemplate, pdfTemplate
from sendReport.sendOff import printOut

if __name__ == "__main__":
    outFile = "outputs/output.txt"
    templateFile = "templates/mainLayout.html"
    status, ppN, ratings = get_page("Hillsboro", "Oregon", "US", debug=False)
    txtTemplate.dateReport(outFile)

    pdfTemplate.loadTemplate(templateFile, ppN, ratings)
    printOut(ppN, "outputs/report.pdf")

    # for index in range(len(ppN)):
    #     basic = txtTemplate.createBase("basics.txt", index+1, ppN[index], ratings[index])
    #     txtTemplate.printOut(outFile, basic)
