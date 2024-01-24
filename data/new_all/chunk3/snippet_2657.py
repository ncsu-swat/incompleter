# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67668673/how-to-pick-up-the-correct-class-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(565235)

except ImportError:
    pass
try:
    import tldextract
    _l_(565237)

except ImportError:
    pass


class Scraper:
    _l_(565258)

    scrapers = {}
    _l_(565238)

    def __init_subclass__(scraper_class):
        _l_(565245)

        _a_(565240, _n_(565239, "Scraper", lambda: Scraper), "scrapers")[_a_(565242, _n_(565241, "scraper_class", lambda: scraper_class), "url")] = _n_(565243, "scraper_class", lambda: scraper_class) # .url -> Unresolved attribute reference 'url' for class 'Scraper' 
        _l_(565244) # .url -> Unresolved attribute reference 'url' for class 'Scraper' 

    @_n_(565246, "classmethod", lambda: classmethod)
    def for_url(cls, url):
        _l_(565257)

        k = _c_(565250, _a_(565248, _n_(565247, "tldextract", lambda: tldextract), "extract"), _n_(565249, "url", lambda: url))
        _l_(565251)
        aux = _c_(565255, _n_(565252, "scrapers", lambda: scrapers)[_a_(565254, _n_(565253, "k", lambda: k), "domain")]) #<-- Unresolved reference 'scrapers' 
        _l_(565256) #<-- Unresolved reference 'scrapers' 
        return aux #<-- Unresolved reference 'scrapers' 


class BBCScraper(_n_(565259, "Scraper", lambda: Scraper)):
    _l_(565267)

    url = 'bbc.co.uk'
    _l_(565260)

    def scrape(s):
        _l_(565266)

        _c_(565263, _n_(565261, "print", lambda: print), _n_(565262, "s", lambda: s))
        _l_(565264)
        aux = "Yay works!"
        _l_(565265)
        # FIXME Scrape the correct values for BBC
        return aux


url = 'https://www.bbc.co.uk/'
_l_(565268)
scraper = _c_(565272, _a_(565270, _n_(565269, "Scraper", lambda: Scraper), "for_url"), _n_(565271, "url", lambda: url))
_l_(565273)
_c_(565276, _a_(565275, _n_(565274, "scraper", lambda: scraper), "scrape"), "yay")
_l_(565277)