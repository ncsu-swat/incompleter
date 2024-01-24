# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56519945/i-want-to-write-json-files-with-data-that-i-scraped-with-a-webscraper-and-an-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(669616, _n_(669615, "open", lambda: open), 'C:/Users/Maximvs/PycharmProjects/Scrapy/planInfo/planInfo/spiders/Freedom_api.json') as json_file:
    _l_(669624)

    dataRaw = _c_(669620, _a_(669618, _n_(669617, "json", lambda: json), "load"), _n_(669619, "json_file", lambda: json_file))
    _l_(669621)
    dataText = _n_(669622, "dataRaw", lambda: dataRaw)
    _l_(669623)


def writeToJSONFile(path, fileName, data):
    _l_(669638)

    filePathNameWExt = '' + _n_(669625, "path", lambda: path) + '/' + _n_(669626, "fileName", lambda: fileName) + '.json'
    _l_(669627)

    with _c_(669630, _n_(669628, "open", lambda: open), _n_(669629, "filePathNameWExt", lambda: filePathNameWExt), 'w') as fp:
        _l_(669637)

        _c_(669635, _a_(669632, _n_(669631, "json", lambda: json), "dump"), _n_(669633, "data", lambda: data), _n_(669634, "fp", lambda: fp))
        _l_(669636)


path = 'C:/Users/Maximvs/Documents/Scraper_Plans'
_l_(669639)


for Linkindex,link in _c_(669642, _n_(669640, "enumerate", lambda: enumerate), _n_(669641, "PhonePermutationLinks", lambda: PhonePermutationLinks)):
    _l_(669652)

    fileName = _c_(669646, _n_(669643, "str", lambda: str), _n_(669644, "phonesListExtended", lambda: phonesListExtended)[_n_(669645, "Linkindex", lambda: Linkindex)]) + " " + _c_(669650, _n_(669647, "str", lambda: str), _n_(669648, "phonePlansListExtended", lambda: phonePlansListExtended)[_n_(669649, "Linkindex", lambda: Linkindex)])
    _l_(669651)