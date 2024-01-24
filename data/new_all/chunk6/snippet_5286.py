# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73379445/cant-loop-in-nested-dictionary-typeerror-argument-of-type-bool-is-not-iter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(359522)

except ImportError:
    pass
    
class MlSpider(_a_(359524, _n_(359523, "scrapy", lambda: scrapy), "Spider")):
    _l_(359526)

    name = 'detalhador'
    _l_(359525)

start_urls=['https://produto.mercadolivre.com.br/MLB-1304118411-sandalia-feminina-anabela-confortavel-pingente-mac-cod-133-_JM?attributes=COLOR_SECONDARY_COLOR%3AUHJldGE%3D%2CSIZE%3AMzU%3D&quantity=1']
_l_(359527)

def parse(self, response,**kwargs):
    _l_(359550)

    try:
        import json
        _l_(359529)

    except ImportError:
        pass

    d = _c_(359534, _a_(359533, _c_(359532, _a_(359531, _n_(359530, "response", lambda: response), "xpath"), '//script[contains(., "window.__PRELOADED_STATE__")]/text()'), "re_first"), r'(?s)window.__PRELOADED_STATE__ = (.+?\});')
    _l_(359535)
    data = _c_(359539, _a_(359537, _n_(359536, "json", lambda: json), "loads"), _n_(359538, "d", lambda: d))
    _l_(359540)
    
    temp='itemPrice'
    _l_(359541)
    res = [_n_(359542, "val", lambda: val)[_n_(359543, "temp", lambda: temp)] for key, val in _c_(359546, _a_(359545, _n_(359544, "data", lambda: data), "items")) if _n_(359547, "temp", lambda: temp) in _n_(359548, "val", lambda: val)]
    _l_(359549)