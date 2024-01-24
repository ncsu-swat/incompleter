# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75851013/reoccuring-attributeerror-nonetype-object-has-no-attribute-find-all
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(604121, _n_(604120, "range", lambda: range), 10,140,20):
     _l_(604144)

     url = (f'https://www.indeed.com/cmp/Ey/reviews?fcountry=IT&start={_n_(604122, "i", lambda: i)}')
     _l_(604123)
     header = {'User-Agent':'Mozilla/5.0 Gecko/20100101 Firefox/33.0 GoogleChrome/10.0'}
     _l_(604124)
     page = _c_(604129, _a_(604126, _n_(604125, 'requests', lambda: requests), 'get'), _n_(604127, 'url', lambda: url),headers = _n_(604128, 'header', lambda: header))
     _l_(604130)
     soup = _c_(604134, _n_(604131, 'BeautifulSoup', lambda: BeautifulSoup), _a_(604133, _n_(604132, 'page', lambda: page), 'content'), 'lxml')
     _l_(604135)
     results = _c_(604138, _a_(604137, _n_(604136, 'soup', lambda: soup), 'find'), 'div', { 'id' : 'cmp-container'})
     _l_(604139)
     elems = _c_(604142, _a_(604141, _n_(604140, 'results', lambda: results), 'find_all'), class_="cmp-Review-container")
     _l_(604143)