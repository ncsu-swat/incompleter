# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64846589/attributeerror-response-content-isnt-text-what-is-the-problem
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(537119)

except ImportError:
    pass
try:
    import json
    _l_(537121)

except ImportError:
    pass


class BasisMembersSpider(_a_(537123, _n_(537122, "scrapy", lambda: scrapy), "Spider")):
    _l_(537174)

    name = 'basis'
    _l_(537124)
    allowed_domains = ['www.basis.org.bd']
    _l_(537125)

    def start_requests(self):
        _l_(537134)

        start_url = 'https://basis.org.bd/get-member-list?page=1&team='
        _l_(537126)
        yield _c_(537132, _a_(537128, _n_(537127, "scrapy", lambda: scrapy), "Request"), url=_n_(537129, "start_url", lambda: start_url), callback=_a_(537131, _n_(537130, "self", lambda: self), "get_membership_no"))
        _l_(537133)

    def get_membership_no(self, response):
        _l_(537169)


        data_array = _c_(537139, _a_(537136, _n_(537135, "json", lambda: json), "loads"), _a_(537138, _n_(537137, "response", lambda: response), "body"))['data']
        _l_(537140)
        next_page = _c_(537145, _a_(537142, _n_(537141, "json", lambda: json), "loads"), _a_(537144, _n_(537143, "response", lambda: response), "body"))['links']['next']
        _l_(537146)
        
        for data in _n_(537147, "data_array", lambda: data_array):
            _l_(537159)

            next_url = _c_(537150, _a_(537148, 'https://basis.org.bd/get-company-profile/{0}', "format"), _n_(537149, "data", lambda: data)['membership_no'])
            _l_(537151)
            yield _c_(537157, _a_(537153, _n_(537152, "scrapy", lambda: scrapy), "Request"), url=_n_(537154, "next_url", lambda: next_url), callback=_a_(537156, _n_(537155, "self", lambda: self), "parse"))
            _l_(537158)
        if _n_(537160, "next_page", lambda: next_page):
            _l_(537168)

            yield _c_(537166, _a_(537162, _n_(537161, "scrapy", lambda: scrapy), "Request"), url=_n_(537163, "next_page", lambda: next_page), callback=_a_(537165, _n_(537164, "self", lambda: self), "get_membership_no"))
            _l_(537167)

    def parse(self, response):
        _l_(537173)

        _c_(537171, _n_(537170, "print", lambda: print), "Printing informations....................................................")
        _l_(537172)