# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64492779/scrapy-typeerror-can-only-concatenate-str-not-list-to-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(345984)

except ImportError:
    pass
try:
    from scrapy.spiders import Rule
    _l_(345986)

except ImportError:
    pass
try:
    from scrapy.spiders import CrawlSpider
    _l_(345988)

except ImportError:
    pass
try:
    from scrapy.selector import Selector
    _l_(345990)

except ImportError:
    pass
# from urllib.parse import urljoin


class ZomatoSpider(_a_(345992, _n_(345991, "scrapy", lambda: scrapy), "Spider")):
    _l_(346087)

    name = 'zomato'
    _l_(345993)
    allowed_domain = ['foodbizmalaysia.com']
    _l_(345994)
    start_urls = ['http://www.foodbizmalaysia.com/category/3/bakery-pastry-supplies?classid=DS-B42850']
    _l_(345995)
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "cookie": "dnetsid=5kegaefgfpb0efhf3idfxn30; afrvt=14846924c9bb4e87b5576addf94f8cc4; _ga=GA1.2.1937980614.1603360774; _gid=GA1.2.1358979332.1603360774"
    }
    _l_(345996)


    def parse(self, response):
        _l_(346007)

        url = "http://www.foodbizmalaysia.com/"
        _l_(345997)

        yield _c_(346005, _a_(345999, _n_(345998, "scrapy", lambda: scrapy), "Request"), _n_(346000, "url", lambda: url), 
            callback=_a_(346002, _n_(346001, "self", lambda: self), "parse_api"), 
            headers=_a_(346004, _n_(346003, "self", lambda: self), "headers"))
        _l_(346006)


    def parse_api(self, response):
        _l_(346039)

        base_url = 'http://www.foodbizmalaysia.com'
        _l_(346008)
        sel = _c_(346011, _n_(346009, "Selector", lambda: Selector), _n_(346010, "response", lambda: response))
        _l_(346012)
        sites = _c_(346015, _a_(346014, _n_(346013, "sel", lambda: sel), "xpath"), '/html')
        _l_(346016)
                
        for data in _n_(346017, "sites", lambda: sites):
            _l_(346038)

            categories = _c_(346022, _a_(346021, _c_(346020, _a_(346019, _n_(346018, "data", lambda: data), "xpath"), '//div[@class="post_content"]/a[contains(@href, "category")]/@href'), "extract"))
            _l_(346023)
            category_url = _n_(346024, "base_url", lambda: base_url) + _n_(346025, "categories", lambda: categories)
            _l_(346026)

            request = _c_(346034, _a_(346028, _n_(346027, "scrapy", lambda: scrapy), "Request"), _n_(346029, "category_url", lambda: category_url), 
                callback=_a_(346031, _n_(346030, "self", lambda: self), "parse_restaurant_company"), 
                headers=_a_(346033, _n_(346032, "self", lambda: self), "headers")
            ) 
            _l_(346035) 

            yield _n_(346036, "request", lambda: request)
            _l_(346037)


    def parse_restaurant_company(self, response):
        _l_(346071)

        base_url = 'http://www.foodbizmalaysia.com'
        _l_(346040)
        sel = _c_(346043, _n_(346041, "Selector", lambda: Selector), _n_(346042, "response", lambda: response))
        _l_(346044)
        sites = _c_(346047, _a_(346046, _n_(346045, "sel", lambda: sel), "xpath"), '/html')
        _l_(346048)

        for data in _n_(346049, "sites", lambda: sites):
            _l_(346059)

            company = _c_(346054, _a_(346053, _c_(346052, _a_(346051, _n_(346050, "data", lambda: data), "xpath"), '//a[contains(@id, "ContentPlaceHolder1_dgrdCompany_Hyperlink4_")]/@href'), "extract_first"))
            _l_(346055)
            company_url = _n_(346056, "base_url", lambda: base_url) + _n_(346057, "company", lambda: company)
            _l_(346058)

        request = _c_(346067, _a_(346061, _n_(346060, "scrapy", lambda: scrapy), "Request"), _n_(346062, "company_url", lambda: company_url),
                callback=_a_(346064, _n_(346063, "self", lambda: self), "parse_company_details"), 
                headers=_a_(346066, _n_(346065, "self", lambda: self), "headers")

        )
        _l_(346068)
        yield _n_(346069, "request", lambda: request)
        _l_(346070)

    def parse_company_details(self, response):
        _l_(346086)

        sel = _c_(346074, _n_(346072, "Selector", lambda: Selector), _n_(346073, "response", lambda: response))
        _l_(346075)
        sites = _c_(346078, _a_(346077, _n_(346076, "sel", lambda: sel), "xpath"), '/html')
        _l_(346079)

        yield {
            'name' : _c_(346084, _a_(346083, _c_(346082, _a_(346081, _n_(346080, "sites", lambda: sites), "xpath"), '//span[@class="coprofileh3"]/text()'), "get"))
        }
        _l_(346085)