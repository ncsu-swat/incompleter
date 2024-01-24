# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71508606/attributeerror-navigablestring-object-has-no-attribute-keys-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(535674)

except ImportError:
    pass
try:
    import csv
    _l_(535676)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup as bs
    _l_(535678)

except ImportError:
    pass

global newsitems
_l_(535679)
def loadRSS():
    _l_(535695)

    url="https://rss.nytimes.com/services/xml/rss/nyt/Africa.xml"
    _l_(535680)
    resp=_c_(535684, _a_(535682, _n_(535681, "requests", lambda: requests), "get"), _n_(535683, "url", lambda: url))
    _l_(535685)
    with _c_(535687, _n_(535686, "open", lambda: open), 'topnewsfeed.xml','wb') as f:
        _l_(535694)

        _c_(535692, _a_(535689, _n_(535688, "f", lambda: f), "write"), _a_(535691, _n_(535690, "resp", lambda: resp), "content"))
        _l_(535693)

def extractData():
    _l_(535768)

    infile = _c_(535697, _n_(535696, "open", lambda: open), "topnewsfeed.xml","r",encoding='utf-8')
    _l_(535698)
    contents = _c_(535701, _a_(535700, _n_(535699, "infile", lambda: infile), "read"))
    _l_(535702)
    soup = _c_(535705, _n_(535703, "bs", lambda: bs), _n_(535704, "contents", lambda: contents),'xml')
    _l_(535706)
    guids= _c_(535709, _a_(535708, _n_(535707, "soup", lambda: soup), "find_all"), 'guid')
    _l_(535710)
    titles = _c_(535713, _a_(535712, _n_(535711, "soup", lambda: soup), "find_all"), 'title')
    _l_(535714)
    pubDates= _c_(535717, _a_(535716, _n_(535715, "soup", lambda: soup), "find_all"), 'pubDate')
    _l_(535718)
    descs= _c_(535721, _a_(535720, _n_(535719, "soup", lambda: soup), "find_all"), 'description')
    _l_(535722)
    links= _c_(535725, _a_(535724, _n_(535723, "soup", lambda: soup), "find_all"), 'link')
    _l_(535726)
    newsitems=[]
    _l_(535727)
    for (guid,title,pubDate,desc,link) in _c_(535734, _n_(535728, "zip", lambda: zip), _n_(535729, "guids", lambda: guids),_n_(535730, "titles", lambda: titles),_n_(535731, "pubDates", lambda: pubDates),_n_(535732, "descs", lambda: descs),_n_(535733, "links", lambda: links)):
        _l_(535765)

        _c_(535739, _a_(535736, _n_(535735, "newsitems", lambda: newsitems), "append"), _a_(535738, _n_(535737, "guid", lambda: guid), "string"))
        _l_(535740)
        _c_(535745, _a_(535742, _n_(535741, "newsitems", lambda: newsitems), "append"), _a_(535744, _n_(535743, "title", lambda: title), "string"))
        _l_(535746)
        _c_(535751, _a_(535748, _n_(535747, "newsitems", lambda: newsitems), "append"), _a_(535750, _n_(535749, "pubDate", lambda: pubDate), "string"))
        _l_(535752)
        _c_(535757, _a_(535754, _n_(535753, "newsitems", lambda: newsitems), "append"), _a_(535756, _n_(535755, "desc", lambda: desc), "string"))
        _l_(535758)
        _c_(535763, _a_(535760, _n_(535759, "newsitems", lambda: newsitems), "append"), _a_(535762, _n_(535761, "link", lambda: link), "string"))
        _l_(535764)
    aux = _n_(535766, "newsitems", lambda: newsitems)
    _l_(535767)
    return aux

def savetoCSV(array,filename):
    _l_(535789)

    fields=['Guid','Title','PubDate','Description','Link']
    _l_(535769)
    with _c_(535772, _n_(535770, "open", lambda: open), _n_(535771, "filename", lambda: filename),'w') as csvfile:
        _l_(535788)

        writer=_c_(535777, _a_(535774, _n_(535773, "csv", lambda: csv), "DictWriter"), _n_(535775, "csvfile", lambda: csvfile),fieldnames=_n_(535776, "fields", lambda: fields))
        _l_(535778)
        _c_(535781, _a_(535780, _n_(535779, "writer", lambda: writer), "writeheader"))
        _l_(535782)
        _c_(535786, _a_(535784, _n_(535783, "writer", lambda: writer), "writerows"), _n_(535785, "array", lambda: array))
        _l_(535787)
def run():
    _l_(535800)

    _c_(535791, _n_(535790, "loadRSS", lambda: loadRSS))
    _l_(535792)
    newsitems=_c_(535794, _n_(535793, "extractData", lambda: extractData))
    _l_(535795)
    _c_(535798, _n_(535796, "savetoCSV", lambda: savetoCSV), _n_(535797, "newsitems", lambda: newsitems),'topnews.csv')
    _l_(535799)
_c_(535802, _n_(535801, "run", lambda: run))
_l_(535803)