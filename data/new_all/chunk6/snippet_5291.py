# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73379445/cant-loop-in-nested-dictionary-typeerror-argument-of-type-bool-is-not-iter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(353675)

except ImportError:
    pass
    
class MlSpider(_a_(353677, _n_(353676, "scrapy", lambda: scrapy), "Spider")):
    _l_(353679)

    name = 'detalhador'
    _l_(353678)

start_urls=['https://produto.mercadolivre.com.br/MLB-1304118411-sandalia-feminina-anabela-confortavel-pingente-mac-cod-133-_JM?attributes=COLOR_SECONDARY_COLOR%3AUHJldGE%3D%2CSIZE%3AMzU%3D&quantity=1']
_l_(353680)

def parse(self, response,**kwargs):
    _l_(353703)

    try:
        import json
        _l_(353682)

    except ImportError:
        pass

    d = _c_(353687, _a_(353686, _c_(353685, _a_(353684, _n_(353683, "response", lambda: response), "xpath"), '//script[contains(., "window.__PRELOADED_STATE__")]/text()'), "re_first"), r'(?s)window.__PRELOADED_STATE__ = (.+?\});')
    _l_(353688)
    data = _c_(353692, _a_(353690, _n_(353689, "json", lambda: json), "loads"), _n_(353691, "d", lambda: d))
    _l_(353693)
    
    temp='itemPrice'
    _l_(353694)
    res = [_n_(353695, "val", lambda: val)[_n_(353696, "temp", lambda: temp)] for key, val in _c_(353699, _a_(353698, _n_(353697, "data", lambda: data), "items")) if _n_(353700, "temp", lambda: temp) in _n_(353701, "val", lambda: val)]
    _l_(353702)