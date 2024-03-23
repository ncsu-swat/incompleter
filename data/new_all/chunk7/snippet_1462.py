# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55728879/typeerror-a-bytes-like-object-is-required-not-str-py-2-7-to-py-3-6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os,sys,csv,time
    _l_(422013)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(422015)

except ImportError:
    pass
try:
    import urllib.request
    _l_(422017)

except ImportError:
    pass
try:
    from urllib.request import urlopen
    _l_(422019)

except ImportError:
    pass

_c_(422022, _a_(422021, _n_(422020, "os", lambda: os), "chdir"), 'E:\Python\python_exercise') # The location of your file "LongCompanyList.csv"
_l_(422023) # The location of your file "LongCompanyList.csv"
companyListFile = "CompanyList.csv" # a csv file with the list of company ticker symbols and names (the file has a line with headers)
_l_(422024) # a csv file with the list of company ticker symbols and names (the file has a line with headers)
IndexLinksFile = "IndexLinks.csv" # a csv file (output of the current script) with the list of index links for each firm (the file has a line with headers)
_l_(422025) # a csv file (output of the current script) with the list of index links for each firm (the file has a line with headers)

def getIndexLink(tickerCode,FormType):
    _l_(422128)

    csvOutput = _c_(422028, _n_(422026, "open", lambda: open), _n_(422027, "IndexLinksFile", lambda: IndexLinksFile),"a+b") # "a+b" indicates that we are adding lines rather than replacing lines
    _l_(422029) # "a+b" indicates that we are adding lines rather than replacing lines
    csvWriter = _c_(422035, _a_(422031, _n_(422030, "csv", lambda: csv), "writer"), _n_(422032, "csvOutput", lambda: csvOutput), quoting = _a_(422034, _n_(422033, "csv", lambda: csv), "QUOTE_NONNUMERIC"))
    _l_(422036)

    urlLink = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK="+_n_(422037, "tickerCode", lambda: tickerCode)+"&type="+_n_(422038, "FormType", lambda: FormType)+"&dateb=&owner=exclude&count=100"
    _l_(422039)
    pageRequest = _c_(422043, _a_(422041, _n_(422040, "urllib", lambda: urllib), "Request"), _n_(422042, "urlLink", lambda: urlLink))
    _l_(422044)
    pageOpen = _c_(422048, _a_(422046, _n_(422045, "urllib", lambda: urllib), "urlopen"), _n_(422047, "pageRequest", lambda: pageRequest))
    _l_(422049)
    pageRead = _c_(422052, _a_(422051, _n_(422050, "pageOpen", lambda: pageOpen), "read"))
    _l_(422053)

    soup = _c_(422056, _n_(422054, "BeautifulSoup", lambda: BeautifulSoup), _n_(422055, "pageRead", lambda: pageRead),"html.parser")
    _l_(422057)

    #Check if there is a table to extract / code exists in edgar database
    try:
        _l_(422068)

        table = _c_(422060, _a_(422059, _n_(422058, "soup", lambda: soup), "find"), "table", { "class" : "tableFile2" })
        _l_(422061)
    except:
        _l_(422067)

        _c_(422064, _n_(422062, "print", lambda: print), "No tables found or no matching ticker symbol for ticker symbol for"+_n_(422063, "tickerCode", lambda: tickerCode))
        _l_(422065)
        aux = -1
        _l_(422066)
        return aux

    docIndex = 1
    _l_(422069)
    for row in _c_(422072, _a_(422071, _n_(422070, "table", lambda: table), "findAll"), "tr"):
        _l_(422123)

        cells = _c_(422075, _a_(422074, _n_(422073, "row", lambda: row), "findAll"), "td")
        _l_(422076)
        if _c_(422079, _n_(422077, "len", lambda: len), _n_(422078, "cells", lambda: cells))==5:
            _l_(422122)

            if _c_(422083, _a_(422082, _a_(422081, _n_(422080, "cells", lambda: cells)[0], "text"), "strip")) == _n_(422084, "FormType", lambda: FormType):
                _l_(422121)

                link = _c_(422087, _a_(422086, _n_(422085, "cells", lambda: cells)[1], "find"), "a",{"id": "documentsbutton"})
                _l_(422088)
                docLink = "https://www.sec.gov"+_n_(422089, "link", lambda: link)['href']
                _l_(422090)
                description = _c_(422096, _a_(422095, _c_(422094, _a_(422093, _a_(422092, _n_(422091, "cells", lambda: cells)[2], "text"), "encode"), 'utf8'), "strip")) #strip take care of the space in the beginning and the end
                _l_(422097) #strip take care of the space in the beginning and the end
                filingDate = _c_(422103, _a_(422102, _c_(422101, _a_(422100, _a_(422099, _n_(422098, "cells", lambda: cells)[3], "text"), "encode"), 'utf8'), "strip"))
                _l_(422104)
                newfilingDate = _c_(422107, _a_(422106, _n_(422105, "filingDate", lambda: filingDate), "replace"), "-","_")  ### <=== Change date format from 2012-1-1 to 2012_1_1 so it can be used as part of 10-K file names
                _l_(422108)  ### <=== Change date format from 2012-1-1 to 2012_1_1 so it can be used as part of 10-K file names
                _c_(422117, _a_(422110, _n_(422109, "csvWriter", lambda: csvWriter), "writerow"), [_n_(422111, "tickerCode", lambda: tickerCode), _n_(422112, "docIndex", lambda: docIndex), _n_(422113, "docLink", lambda: docLink), _n_(422114, "description", lambda: description), _n_(422115, "filingDate", lambda: filingDate),_n_(422116, "newfilingDate", lambda: newfilingDate)])
                _l_(422118)
                docIndex = _n_(422119, "docIndex", lambda: docIndex) + 1
                _l_(422120)
    _c_(422126, _a_(422125, _n_(422124, "csvOutput", lambda: csvOutput), "close"))
    _l_(422127)


def main():
    _l_(422203)

    FormType = "10-K"   ### <=== Type your document type here
    _l_(422129)   ### <=== Type your document type here
    nbDocPause = 10 ### <=== Type your number of documents to download in one batch
    _l_(422130) ### <=== Type your number of documents to download in one batch
    nbSecPause = 0 ### <=== Type your pausing time in seconds between each batch
    _l_(422131) ### <=== Type your pausing time in seconds between each batch

    csvFile = _c_(422134, _n_(422132, "open", lambda: open), _n_(422133, "companyListFile", lambda: companyListFile),"r") #<===open and read from a csv file with the list of company ticker symbols (the file has a line with headers)
    _l_(422135) #<===open and read from a csv file with the list of company ticker symbols (the file has a line with headers)
    csvReader = _c_(422139, _a_(422137, _n_(422136, "csv", lambda: csv), "reader"), _n_(422138, "csvFile", lambda: csvFile),delimiter=",")
    _l_(422140)
    csvData = _c_(422143, _n_(422141, "list", lambda: list), _n_(422142, "csvReader", lambda: csvReader))
    _l_(422144)

    csvOutput = _c_(422147, _n_(422145, "open", lambda: open), _n_(422146, "IndexLinksFile", lambda: IndexLinksFile),"a+b") #<===open and write to a csv file which will include the list of index links. New rows will be appended.
    _l_(422148) #<===open and write to a csv file which will include the list of index links. New rows will be appended.
    csvWriter = _c_(422154, _a_(422150, _n_(422149, "csv", lambda: csv), "writer"), _n_(422151, "csvOutput", lambda: csvOutput), quoting = _a_(422153, _n_(422152, "csv", lambda: csv), "QUOTE_NONNUMERIC"))
    _l_(422155)

    _c_(422158, _a_(422157, _n_(422156, "csvWriter", lambda: csvWriter), "writerow"), ["Ticker", "DocIndex","IndexLink", "Description", "FilingDate","NewFilingDate"])
    _l_(422159)
    _c_(422162, _a_(422161, _n_(422160, "csvOutput", lambda: csvOutput), "close"))
    _l_(422163)

    i = 1
    _l_(422164)
    for rowData in _n_(422165, "csvData", lambda: csvData)[1:]:
        _l_(422195)

        ticker = _n_(422166, "rowData", lambda: rowData)[0]
        _l_(422167)
        _c_(422171, _n_(422168, "getIndexLink", lambda: getIndexLink), _n_(422169, "ticker", lambda: ticker),_n_(422170, "FormType", lambda: FormType))
        _l_(422172)
        if _n_(422173, "i", lambda: i)%_n_(422174, "nbDocPause", lambda: nbDocPause) == 0:
            _l_(422192)

            _c_(422177, _n_(422175, "print", lambda: print), _n_(422176, "i", lambda: i))
            _l_(422178)
            _c_(422183, _n_(422179, "print", lambda: print), "Pause for "+_c_(422182, _n_(422180, "str", lambda: str), _n_(422181, "nbSecPause", lambda: nbSecPause))+" second .... ")
            _l_(422184)
            _c_(422190, _a_(422186, _n_(422185, "time", lambda: time), "sleep"), _c_(422189, _n_(422187, "float", lambda: float), _n_(422188, "nbSecPause", lambda: nbSecPause)))
            _l_(422191)
        i=_n_(422193, "i", lambda: i)+1
        _l_(422194)

    _c_(422198, _a_(422197, _n_(422196, "csvFile", lambda: csvFile), "close"))
    _l_(422199)
    _c_(422201, _n_(422200, "print", lambda: print), "done!")
    _l_(422202)

if _n_(422204, "__name__", lambda: __name__) == "__main__":
    _l_(422208)

    _c_(422206, _n_(422205, "main", lambda: main))
    _l_(422207)