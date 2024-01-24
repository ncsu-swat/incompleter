# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43725686/xlwt-book-save-typeerror-must-be-str-not-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import newspaper
    _l_(670633)

except ImportError:
    pass
try:
    from newspaper import Article
    _l_(670635)

except ImportError:
    pass
try:
    import xlwt
    _l_(670637)

except ImportError:
    pass

book = _c_(670640, _a_(670639, _n_(670638, "xlwt", lambda: xlwt), "Workbook"))
_l_(670641)

sheet1 = _c_(670644, _a_(670643, _n_(670642, "book", lambda: book), "add_sheet"), "Run1", cell_overwrite_ok=True)
_l_(670645)

_c_(670648, _a_(670647, _n_(670646, "sheet1", lambda: sheet1), "write"), 0, 0, "Text")
_l_(670649)
_c_(670652, _a_(670651, _n_(670650, "sheet1", lambda: sheet1), "write"), 0, 1, "Journalist")
_l_(670653)
_c_(670656, _a_(670655, _n_(670654, "sheet1", lambda: sheet1), "write"), 0, 2, "URL")
_l_(670657)
_c_(670660, _a_(670659, _n_(670658, "sheet1", lambda: sheet1), "write"), 0, 3, "Title")
_l_(670661)

URL_list=[_n_(670662, "x", lambda: x),_n_(670663, "y", lambda: y)]
_l_(670664)

url = _n_(670665, "URL_list", lambda: URL_list)[0]
_l_(670666)

article = _c_(670669, _n_(670667, "Article", lambda: Article), _n_(670668, "url", lambda: url))
_l_(670670)

z=1
_l_(670671)

for n in _n_(670672, "URL_list", lambda: URL_list):
    _l_(670681)

    _c_(670677, _a_(670674, _n_(670673, "sheet1", lambda: sheet1), "write"), _n_(670675, "z", lambda: z), 2, _n_(670676, "n", lambda: n))
    _l_(670678)
    z=_n_(670679, "z", lambda: z)+1
    _l_(670680)

d=1
_l_(670682)

for n in _n_(670683, "URL_list", lambda: URL_list):
    _l_(670713)

    url = _n_(670684, "URL_list", lambda: URL_list)[_c_(670688, _a_(670686, _n_(670685, "URL_list", lambda: URL_list), "index"), _n_(670687, "n", lambda: n))]
    _l_(670689)
    article = _c_(670692, _n_(670690, "Article", lambda: Article), _n_(670691, "url", lambda: url))
    _l_(670693)
    _c_(670696, _a_(670695, _n_(670694, "article", lambda: article), "download"))
    _l_(670697)
    _c_(670700, _a_(670699, _n_(670698, "article", lambda: article), "parse"))
    _l_(670701)
    e = _a_(670703, _n_(670702, "article", lambda: article), "title")
    _l_(670704)
    _c_(670709, _a_(670706, _n_(670705, "sheet1", lambda: sheet1), "write"), _n_(670707, "d", lambda: d), 3, _n_(670708, "e", lambda: e))
    _l_(670710)
    d = _n_(670711, "d", lambda: d)+1
    _l_(670712)

i=1
_l_(670714)

for n in _n_(670715, "URL_list", lambda: URL_list):
    _l_(670745)

    url = _n_(670716, "URL_list", lambda: URL_list)[_c_(670720, _a_(670718, _n_(670717, "URL_list", lambda: URL_list), "index"), _n_(670719, "n", lambda: n))]
    _l_(670721)
    article = _c_(670724, _n_(670722, "Article", lambda: Article), _n_(670723, "url", lambda: url))
    _l_(670725)
    _c_(670728, _a_(670727, _n_(670726, "article", lambda: article), "download"))
    _l_(670729)
    _c_(670732, _a_(670731, _n_(670730, "article", lambda: article), "parse"))
    _l_(670733)
    b = _a_(670735, _n_(670734, "article", lambda: article), "text")
    _l_(670736)
    _c_(670741, _a_(670738, _n_(670737, "sheet1", lambda: sheet1), "write"), _n_(670739, "i", lambda: i), 0, _n_(670740, "b", lambda: b))
    _l_(670742)
    i = _n_(670743, "i", lambda: i)+1
    _l_(670744)

x=1
_l_(670746)

url = _n_(670747, "URL_list", lambda: URL_list)[0]
_l_(670748)

article = _c_(670751, _n_(670749, "Article", lambda: Article), _n_(670750, "url", lambda: url))
_l_(670752)

for n in _n_(670753, "URL_list", lambda: URL_list):
    _l_(670783)

    url = _n_(670754, "URL_list", lambda: URL_list)[_c_(670758, _a_(670756, _n_(670755, "URL_list", lambda: URL_list), "index"), _n_(670757, "n", lambda: n))]
    _l_(670759)
    article = _c_(670762, _n_(670760, "Article", lambda: Article), _n_(670761, "url", lambda: url))
    _l_(670763)
    _c_(670766, _a_(670765, _n_(670764, "article", lambda: article), "download"))
    _l_(670767)
    _c_(670770, _a_(670769, _n_(670768, "article", lambda: article), "parse"))
    _l_(670771)
    c = _a_(670773, _n_(670772, "article", lambda: article), "authors")
    _l_(670774)
    _c_(670779, _a_(670776, _n_(670775, "sheet1", lambda: sheet1), "write"), _n_(670777, "x", lambda: x), 1, _n_(670778, "c", lambda: c))
    _l_(670780)
    x = _n_(670781, "x", lambda: x)+1
    _l_(670782)

_c_(670786, _a_(670785, _n_(670784, "book", lambda: book), "save"), "Test5_Export_News.xls")
_l_(670787)