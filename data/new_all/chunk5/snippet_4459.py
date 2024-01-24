# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57291114/how-to-add-exception-to-skip-attributeerror-in-my-code
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(649109)

except ImportError:
    pass
try:
    import requests
    _l_(649111)

except ImportError:
    pass
try:
    import pymysql.cursors
    _l_(649113)

except ImportError:
    pass
urls2 = []
_l_(649114)
result = _c_(649117, _a_(649116, _n_(649115, "requests", lambda: requests), "get"), "http://desaku.bandungkab.go.id/desaonline/")
_l_(649118)
src = _a_(649120, _n_(649119, "result", lambda: result), "content")
_l_(649121)
soup = _c_(649124, _n_(649122, "BeautifulSoup", lambda: BeautifulSoup), _n_(649123, "src", lambda: src), 'lxml')
_l_(649125)
links = _c_(649128, _a_(649127, _n_(649126, "soup", lambda: soup), "find_all"), 'a')
_l_(649129)
urls = []
_l_(649130)
for link in _n_(649131, "links", lambda: links):
    _l_(649143)

    if "www" in _a_(649133, _n_(649132, "link", lambda: link), "text"):
        _l_(649142)

        url = _a_(649135, _n_(649134, "link", lambda: link), "attrs")['href']
        _l_(649136)
        _c_(649140, _a_(649138, _n_(649137, "urls", lambda: urls), "append"), _n_(649139, "url", lambda: url))
        _l_(649141)

num1=_c_(649146, _n_(649144, "len", lambda: len), _n_(649145, "urls", lambda: urls))
_l_(649147)
b=0
_l_(649148)
while _n_(649149, "b", lambda: b)<10:
    _l_(649181)

    result2 = _c_(649154, _a_(649151, _n_(649150, "requests", lambda: requests), "get"), _n_(649152, "urls", lambda: urls)[_n_(649153, "b", lambda: b)])
    _l_(649155)
    src2 = _a_(649157, _n_(649156, "result2", lambda: result2), "content")
    _l_(649158)
    soup = _c_(649161, _n_(649159, "BeautifulSoup", lambda: BeautifulSoup), _n_(649160, "src2", lambda: src2), 'lxml')
    _l_(649162)
    links2 = _c_(649165, _a_(649164, _n_(649163, "soup", lambda: soup), "find_all"), 'a')
    _l_(649166)
    for link in _n_(649167, "links2", lambda: links2):
        _l_(649179)

        if "selengkapnya" in _a_(649169, _n_(649168, "link", lambda: link), "text"):
            _l_(649178)

            url2 = _a_(649171, _n_(649170, "link", lambda: link), "attrs")['href']
            _l_(649172)
            _c_(649176, _a_(649174, _n_(649173, "urls2", lambda: urls2), "append"), _n_(649175, "url2", lambda: url2))
            _l_(649177)
    b+=1
    _l_(649180)

num=_c_(649184, _n_(649182, "len", lambda: len), _n_(649183, "urls2", lambda: urls2))
_l_(649185)
i=0
_l_(649186)
while _n_(649187, "i", lambda: i)<_n_(649188, "num", lambda: num):
    _l_(649281)

    html = _c_(649193, _a_(649190, _n_(649189, "requests", lambda: requests), "get"), _n_(649191, "urls2", lambda: urls2)[_n_(649192, "i", lambda: i)])
    _l_(649194)
    src = _a_(649196, _n_(649195, "html", lambda: html), "content")
    _l_(649197)
    soup = _c_(649200, _n_(649198, "BeautifulSoup", lambda: BeautifulSoup), _n_(649199, "src", lambda: src), 'lxml')
    _l_(649201)
    recordList = _c_(649204, _a_(649203, _n_(649202, "soup", lambda: soup), "findAll"), "div", {"class": "artikel", })
    _l_(649205)
    recordlist = _c_(649208, _a_(649207, _n_(649206, "soup", lambda: soup), "find_all"), 'div', attrs={'class':'sampul2'})
    _l_(649209)

    connection = _c_(649214, _a_(649211, _n_(649210, "pymysql", lambda: pymysql), "connect"), host='localhost',
                                 user='root',
                                 password='',
                                 db='bs4-test',
                                 charset='utf8mb4',
                                cursorclass=_a_(649213, _a_(649212, pymysql, "cursors"), "DictCursor"))
    _l_(649215)

    try:
        _l_(649279)

        with _c_(649218, _a_(649217, _n_(649216, "connection", lambda: connection), "cursor")) as cursor:
            _l_(649263)

            for record in _n_(649219, "recordList", lambda: recordList):
                _l_(649262)

    #except AttributeError:
                #continue #WHERE TO PUT THIS EXCEPTION,TO SKIP ATRRIBUTEERRROR?
                title = _c_(649226, _a_(649225, _c_(649224, _a_(649223, _c_(649222, _a_(649221, _n_(649220, "record", lambda: record), "find"), "h2", {"class": "judul",      }), "get_text")), "strip"))
                _l_(649227)
                date = _c_(649235, _a_(649234, _a_(649233, _a_(649232, _a_(649231, _c_(649230, _a_(649229, _n_(649228, "record", lambda: record), "find"), 'i'), "next_sibling"), "next_sibling"), "next_sibling"), "replace"), '\t\t\t\t\t\t\t', '')
                _l_(649236)
                content = _c_(649243, _a_(649242, _c_(649241, _a_(649240, _c_(649239, _a_(649238, _n_(649237, "record", lambda: record), "find"), "div", {"class":"teks"}), "get_text")), "strip"))
                _l_(649244)
                image = _a_(649246, _n_(649245, "record", lambda: record), "img")['src']
                _l_(649247)
                cover = _a_(649249, _n_(649248, "record", lambda: record), "img")['src']
                _l_(649250)
                sql = "INSERT INTO `artikel` (`jdl`, `tgl`, `kon`, `gambar`, `sampul`) VALUES (%s, %s, %s, %s, %s)"
                _l_(649251)
                _c_(649260, _a_(649253, _n_(649252, "cursor", lambda: cursor), "execute"), _n_(649254, "sql", lambda: sql), (_n_(649255, "title", lambda: title), _n_(649256, "date", lambda: date), _n_(649257, "content", lambda: content), _n_(649258, "image", lambda: image), _n_(649259, "cover", lambda: cover)))
                _l_(649261)
        _c_(649266, _a_(649265, _n_(649264, "connection", lambda: connection), "commit"))
        _l_(649267)
        _c_(649269, _n_(649268, "print", lambda: print), "Record inserted successfully into table")
        _l_(649270)
    finally:
        _l_(649278)

        _c_(649273, _a_(649272, _n_(649271, "connection", lambda: connection), "close"))
        _l_(649274)
        _c_(649276, _n_(649275, "print", lambda: print), "MySQL connection is closed")
        _l_(649277)
    i+=1
    _l_(649280)