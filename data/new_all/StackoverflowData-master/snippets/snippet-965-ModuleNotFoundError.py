#Source: https://stackoverflow.com/questions/63758519/why-do-i-receive-this-error-in-python-pdfminer-typeerror-can-only-concatenate
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from pdfminer.pdfpage import PDFPage

def get_pdf_file_content(path_to_pdf):
    resource_manager = PDFResourceManager(caching=True)
    out_text = StringIO
    laParams = LAParams()
    text_converter = TextConverter(resource_manager, out_text, laparams= laParams)
    fp = open(path_to_pdf, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, text_converter)
    for page in PDFPage.get_pages(fp, pagenos=set(), maxpages=0, password="", caching= True, check_extractable= True):
        interpreter.process_page(page)

    text = out_text.getvalue()

    fp.close()
    text_converter.close()
    out_text.close()

    return text

path_to_pdf = "C:\\files\\raw\\AZO - CALLSTREET REPORT  AutoZone, Inc.(AZO), Q1 2002 Earnings Call, 5-December-2001 10 00 AM ET - 05-Dec-01.pdf"
print(get_pdf_file_content(path_to_pdf))