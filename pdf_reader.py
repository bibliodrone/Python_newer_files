import PyPDF2

pdfFileObj = open('BudgetDataFY18.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

print("Page count:" + str(pdfReader.numPages))

for i in range (1):
    pageObj = pdfReader.getPage(i)
    print("---------" + str(i) + "----------")
    pText = pageObj.extractText()

    pSplit = pText.split("\n")
    for p in pSplit:
        print(p, end = "  ")
   
    
