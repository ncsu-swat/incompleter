# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60941433/iterating-through-a-dictionary-typeerror-list-indices-must-be-integers-or-slic
# -*- coding: utf-8 -*-
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(663007)

except ImportError:
    pass
try:
    from ..items import JobcollectorItem
    _l_(663009)

except ImportError:
    pass
try:
    from ..AutoCrawler import searchIndeed
    _l_(663011)

except ImportError:
    pass


class IndeedSpider(_a_(663013, _n_(663012, "scrapy", lambda: scrapy), "Spider")):
    _l_(663069)

    name = 'indeed'
    _l_(663014)
    page_number = 2
    _l_(663015)
    start_urls = [_a_(663017, _n_(663016, "searchIndeed", lambda: searchIndeed), "current_page_url")]
    _l_(663018)

    def parse(self, response):
        _l_(663068)

        items = _c_(663020, _n_(663019, "JobcollectorItem", lambda: JobcollectorItem))
        _l_(663021)

        position = _c_(663026, _a_(663025, _c_(663024, _a_(663023, _n_(663022, "response", lambda: response), "css"), '.jobtitle::text'), "extract"))
        _l_(663027)
        company = _c_(663032, _a_(663031, _c_(663030, _a_(663029, _n_(663028, "response", lambda: response), "css"), 'span.company::text'), "extract"))
        _l_(663033)
        location = _c_(663038, _a_(663037, _c_(663036, _a_(663035, _n_(663034, "response", lambda: response), "css"), '.location::text'), "extract"))
        _l_(663039)

        # print(position[0])

        _n_(663040, "items", lambda: items)['position'] = _n_(663041, "position", lambda: position)
        _l_(663042)
        _n_(663043, "items", lambda: items)['company'] = _n_(663044, "company", lambda: company)
        _l_(663045)
        _n_(663046, "items", lambda: items)['location'] = _n_(663047, "location", lambda: location)
        _l_(663048)

        for key in _c_(663051, _a_(663050, _n_(663049, "items", lambda: items), "keys")):
            _l_(663065)

            prestripped = _n_(663052, "items", lambda: items)[_n_(663053, "key", lambda: key)]
            _l_(663054)
            for object in _n_(663055, "prestripped", lambda: prestripped):
                _l_(663060)

                object = _c_(663058, _a_(663057, _n_(663056, "object", lambda: object), "strip"), '\n')
                _l_(663059)
            _n_(663061, "items", lambda: items)[_n_(663062, "key", lambda: key)] = _n_(663063, "prestripped", lambda: prestripped)
            _l_(663064)

        yield _n_(663066, "items", lambda: items)
        _l_(663067)