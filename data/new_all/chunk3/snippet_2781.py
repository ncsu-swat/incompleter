# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63258398/typeerror-cannot-mix-str-and-non-str-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from scrapy import Spider
    _l_(566213)

except ImportError:
    pass
try:
    from scrapy.http import Request
    _l_(566215)

except ImportError:
    pass


class CourseSpider(_n_(566216, "Spider", lambda: Spider)):
    _l_(566289)

    name = 'course'
    _l_(566217)
    allowed_domains = ['coursera.org']
    _l_(566218)
    start_urls = ['https://coursera.org/about/partners']
    _l_(566219)

    def parse(self, response):
        _l_(566254)

        listings = _c_(566222, _a_(566221, _n_(566220, "response", lambda: response), "xpath"), '//div[@class="rc-PartnerBox vertical-box"]')
        _l_(566223)
        for listing in _n_(566224, "listings", lambda: listings):
            _l_(566253)

            title = _c_(566229, _a_(566228, _c_(566227, _a_(566226, _n_(566225, "listing", lambda: listing), "xpath"), './/div[@class="partner-box-wrapper card-one-clicker flex-1"]/p'), "extract_first"))
            _l_(566230)
            relative_url = _c_(566235, _a_(566234, _c_(566233, _a_(566232, _n_(566231, "listing", lambda: listing), "xpath"), './/a/@href'), "extract_first"))
            _l_(566236)
            absolute_url = _c_(566240, _a_(566238, _n_(566237, "response", lambda: response), "urljoin"), _n_(566239, "relative_url", lambda: relative_url))
            _l_(566241)

            yield _c_(566251, _n_(566242, "Request", lambda: Request), _c_(566246, _a_(566244, _n_(566243, "response", lambda: response), "urljoin"), _n_(566245, "relative_url", lambda: relative_url)), callback = _a_(566248, _n_(566247, "self", lambda: self), "parse_listing"),meta={'title':_n_(566249, "title", lambda: title),'absolute_url':_n_(566250, "absolute_url", lambda: absolute_url)})
            _l_(566252)

    def parse_listing(self,response):
        _l_(566288)

        titles = _c_(566258, _a_(566257, _a_(566256, _n_(566255, "response", lambda: response), "meta"), "get"), 'title')
        _l_(566259)
        absolute_url = _c_(566263, _a_(566262, _a_(566261, _n_(566260, "response", lambda: response), "meta"), "get"), 'absolute_url')
        _l_(566264)
        titles_course =  _c_(566269, _a_(566268, _c_(566267, _a_(566266, _n_(566265, "response", lambda: response), "xpath"), '//div[@class="name headline-1-text"]/text()'), "extract"))
        _l_(566270)
        url_link = _c_(566275, _a_(566274, _c_(566273, _a_(566272, _n_(566271, "response", lambda: response), "xpath"), '//div[@class="rc-Course"]/a/@href'), "extract"))
        _l_(566276)
        abs_url = _c_(566280, _a_(566278, _n_(566277, "response", lambda: response), "urljoin"), _n_(566279, "url_link", lambda: url_link))
        _l_(566281)

        yield {'title':_n_(566282, "title", lambda: title),
        'titles':_n_(566283, "title", lambda: title),
        'absolute_url':_n_(566284, "absolute_url", lambda: absolute_url),
        'titles_course':_n_(566285, "titles_course", lambda: titles_course),
        'abs_url':_n_(566286, "abs_url", lambda: abs_url)}
        _l_(566287)