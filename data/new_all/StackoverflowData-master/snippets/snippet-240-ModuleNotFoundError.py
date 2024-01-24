#Source: https://stackoverflow.com/questions/56249161/typeerror-unsupported-operand-types-for-list-and-int-while-extractin
import numpy
import PyPDF2

fd = open('./sample2.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(fd)
page = pdfreader.getPage(1)
content = page.extractText()
tableList = content.split('\n')
#table has four columns
lines = numpy.array_split(tableList, len(tableList/4))
# displaying row by row 
for i in range(0,5):
    print(lines[i])