from dataRetrieval.scrapeData import get_page
from createReport.generateTemplate import txtTemplate, pdfTemplate

if __name__ == "__main__":
    outFile = "outputs/output.txt"
    templateFile = "templates/basicLayout.html"
    status, ppN, ratings = get_page("Hillsboro", "Oregon", "US", debug=False)
    txtTemplate.dateReport(outFile)

    pdfTemplate.loadTemplate(templateFile, 0, ppN, ratings)

    # for index in range(len(ppN)):
    #     basic = txtTemplate.createBase("basics.txt", index+1, ppN[index], ratings[index])
    #     txtTemplate.printOut(outFile, basic)
