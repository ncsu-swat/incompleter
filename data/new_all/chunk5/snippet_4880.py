# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43725686/xlwt-book-save-typeerror-must-be-str-not-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import newspaper
    _l_(658810)

except ImportError:
    pass
try:
    from newspaper import Article
    _l_(658812)

except ImportError:
    pass
try:
    import xlwt
    _l_(658814)

except ImportError:
    pass

book = _c_(658817, _a_(658816, _n_(658815, "xlwt", lambda: xlwt), "Workbook"))
_l_(658818)

sheet1 = _c_(658821, _a_(658820, _n_(658819, "book", lambda: book), "add_sheet"), "Run1", cell_overwrite_ok=True)
_l_(658822)

_c_(658825, _a_(658824, _n_(658823, "sheet1", lambda: sheet1), "write"), 0, 0, "Text")
_l_(658826)
_c_(658829, _a_(658828, _n_(658827, "sheet1", lambda: sheet1), "write"), 0, 1, "Journalist")
_l_(658830)
_c_(658833, _a_(658832, _n_(658831, "sheet1", lambda: sheet1), "write"), 0, 2, "URL")
_l_(658834)
_c_(658837, _a_(658836, _n_(658835, "sheet1", lambda: sheet1), "write"), 0, 3, "Title")
_l_(658838)

URL_list=[_n_(658839, "x", lambda: x),_n_(658840, "y", lambda: y)]
_l_(658841)

url = _n_(658842, "URL_list", lambda: URL_list)[0]
_l_(658843)

article = _c_(658846, _n_(658844, "Article", lambda: Article), _n_(658845, "url", lambda: url))
_l_(658847)

z=1
_l_(658848)

for n in _n_(658849, "URL_list", lambda: URL_list):
    _l_(658858)

    _c_(658854, _a_(658851, _n_(658850, "sheet1", lambda: sheet1), "write"), _n_(658852, "z", lambda: z), 2, _n_(658853, "n", lambda: n))
    _l_(658855)
    z=_n_(658856, "z", lambda: z)+1
    _l_(658857)

d=1
_l_(658859)

for n in _n_(658860, "URL_list", lambda: URL_list):
    _l_(658890)

    url = _n_(658861, "URL_list", lambda: URL_list)[_c_(658865, _a_(658863, _n_(658862, "URL_list", lambda: URL_list), "index"), _n_(658864, "n", lambda: n))]
    _l_(658866)
    article = _c_(658869, _n_(658867, "Article", lambda: Article), _n_(658868, "url", lambda: url))
    _l_(658870)
    _c_(658873, _a_(658872, _n_(658871, "article", lambda: article), "download"))
    _l_(658874)
    _c_(658877, _a_(658876, _n_(658875, "article", lambda: article), "parse"))
    _l_(658878)
    e = _a_(658880, _n_(658879, "article", lambda: article), "title")
    _l_(658881)
    _c_(658886, _a_(658883, _n_(658882, "sheet1", lambda: sheet1), "write"), _n_(658884, "d", lambda: d), 3, _n_(658885, "e", lambda: e))
    _l_(658887)
    d = _n_(658888, "d", lambda: d)+1
    _l_(658889)

i=1
_l_(658891)

for n in _n_(658892, "URL_list", lambda: URL_list):
    _l_(658922)

    url = _n_(658893, "URL_list", lambda: URL_list)[_c_(658897, _a_(658895, _n_(658894, "URL_list", lambda: URL_list), "index"), _n_(658896, "n", lambda: n))]
    _l_(658898)
    article = _c_(658901, _n_(658899, "Article", lambda: Article), _n_(658900, "url", lambda: url))
    _l_(658902)
    _c_(658905, _a_(658904, _n_(658903, "article", lambda: article), "download"))
    _l_(658906)
    _c_(658909, _a_(658908, _n_(658907, "article", lambda: article), "parse"))
    _l_(658910)
    b = _a_(658912, _n_(658911, "article", lambda: article), "text")
    _l_(658913)
    _c_(658918, _a_(658915, _n_(658914, "sheet1", lambda: sheet1), "write"), _n_(658916, "i", lambda: i), 0, _n_(658917, "b", lambda: b))
    _l_(658919)
    i = _n_(658920, "i", lambda: i)+1
    _l_(658921)

x=1
_l_(658923)

url = _n_(658924, "URL_list", lambda: URL_list)[0]
_l_(658925)

article = _c_(658928, _n_(658926, "Article", lambda: Article), _n_(658927, "url", lambda: url))
_l_(658929)

for n in _n_(658930, "URL_list", lambda: URL_list):
    _l_(658960)

    url = _n_(658931, "URL_list", lambda: URL_list)[_c_(658935, _a_(658933, _n_(658932, "URL_list", lambda: URL_list), "index"), _n_(658934, "n", lambda: n))]
    _l_(658936)
    article = _c_(658939, _n_(658937, "Article", lambda: Article), _n_(658938, "url", lambda: url))
    _l_(658940)
    _c_(658943, _a_(658942, _n_(658941, "article", lambda: article), "download"))
    _l_(658944)
    _c_(658947, _a_(658946, _n_(658945, "article", lambda: article), "parse"))
    _l_(658948)
    c = _a_(658950, _n_(658949, "article", lambda: article), "authors")
    _l_(658951)
    _c_(658956, _a_(658953, _n_(658952, "sheet1", lambda: sheet1), "write"), _n_(658954, "x", lambda: x), 1, _n_(658955, "c", lambda: c))
    _l_(658957)
    x = _n_(658958, "x", lambda: x)+1
    _l_(658959)

_c_(658963, _a_(658962, _n_(658961, "book", lambda: book), "save"), "Test5_Export_News.xls")
_l_(658964)