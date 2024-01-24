# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55012786/typeerror-close-spider-missing-1-required-positional-argument-reason
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scrapy
    _l_(416292)

except ImportError:
    pass
try:
    import scrapy_splash
    _l_(416294)

except ImportError:
    pass
try:
    from scrapy.linkextractors import LinkExtractor
    _l_(416296)

except ImportError:
    pass
try:
    from cointelegraph_spider.items import CointelegraphSpiderItem
    _l_(416298)

except ImportError:
    pass
try:
    import sqlite3 as sq3
    _l_(416300)

except ImportError:
    pass

class CointelegraphspiderSpider(_a_(416302, _n_(416301, "scrapy", lambda: scrapy), "Spider")):
    _l_(416455)

    name = 'cointelegraphspider'
    _l_(416303)
    allowed_domains = ['cointelegraph.com']
    _l_(416304)
    start_urls = ['http://cointelegraph.com/']
    _l_(416305)



    def start_requests(self):
        _l_(416318)


        """
        Doc string
        """

        # Execute the LUA script for "Load Mor" button
        script = """

            function main(splash, args)
                assert(splash:go(args.url))
                splash:wait(0.5)
                local num_clicks = 2
                local delay = 1.5
                local load_more = splash:jsfunc(
                            [[
                                function ()
                                {
                                    var el = document.getElementsByClassName('post-preview-list-navigation__btn post-preview-list-navigation__btn_load-more');
                                    el[0].click();
                                } 
                            ]]

                            )

                for _ = 1, num_clicks do
                    load_more()
                    splash:wait(delay)
                end        

                return 
                {
                    html = splash:html(),
                }
            end

        """
        _l_(416306)

        for url in _a_(416308, _n_(416307, "self", lambda: self), "start_urls"):
            _l_(416317)


            yield _c_(416315, _a_(416310, _n_(416309, "scrapy_splash", lambda: scrapy_splash), "SplashRequest"), url=_n_(416311, "url", lambda: url),
                    callback=_a_(416313, _n_(416312, "self", lambda: self), "parse_main_page"),
                    args={
                            'wait':3,
                            'lua_source':_n_(416314, "script", lambda: script),
                            #'timeout': 3600 # Here the max-timeout is 60 -- to increase it launch the docker with --max-timeout xxxxx
                            },
                    endpoint="execute",
                    )
            _l_(416316)

    def parse_main_page(self, response):
        _l_(416366)

        """
        Doc string
        """        
        # Convert Splash response into html response object
        html = _c_(416322, _a_(416320, _n_(416319, "scrapy", lambda: scrapy), "Selector"), _n_(416321, "response", lambda: response))
        _l_(416323)

        # Check DB for existing records
        conn = _c_(416326, _a_(416325, _n_(416324, "sq3", lambda: sq3), "connect"), "D:\\DCC\\Projects\\crypto_projects\\master_data.db")
        _l_(416327)
        db_links = _c_(416332, _a_(416331, _c_(416330, _a_(416329, _n_(416328, "conn", lambda: conn), "execute"), "select link from cointelegraph"), "fetchall")) # list of tuples
        _l_(416333) # list of tuples
        db_links = [_n_(416334, "elem", lambda: elem)[0] for elem in _n_(416335, "db_links", lambda: db_links)] # flattening list
        _l_(416336) # flattening list
        _c_(416339, _n_(416337, "print", lambda: print), "DB LINKS! ", _n_(416338, "db_links", lambda: db_links))
        _l_(416340)
        #db_links = ["aaa",]
        _c_(416343, _a_(416342, _n_(416341, "conn", lambda: conn), "close")) # close connection
        _l_(416344) # close connection

        # Extract all links to be followed
        news_links = _c_(416350, _a_(416347, _c_(416346, _n_(416345, "LinkExtractor", lambda: LinkExtractor), restrict_xpaths=['//ul[@class="post-preview-list-cards"]/li/div/article/a', # Main Body
                                                    '//div[@class="main-news-tabs__wrp"]/ul/li/div/a'] # "Editor's Choice" & "Hot Stories"
                                    ), "extract_links"), _a_(416349, _n_(416348, "html", lambda: html), "response"))
        _l_(416351)

        for link in _n_(416352, "news_links", lambda: news_links)[:2]:
            _l_(416365)

            # Follow only new links
            if _a_(416354, _n_(416353, "link", lambda: link), "url") not in _n_(416355, "db_links", lambda: db_links):
                _l_(416364)

                yield _c_(416362, _a_(416357, _n_(416356, "scrapy", lambda: scrapy), "Request"), _a_(416359, _n_(416358, "link", lambda: link), "url"), callback=_a_(416361, _n_(416360, "self", lambda: self), "parse_article"))
                _l_(416363)


    def parse_article(self, response):
        _l_(416454)

        """
        Doc string
        """

        # Create Item for Pipeline
        item = _c_(416368, _n_(416367, "CointelegraphSpiderItem", lambda: CointelegraphSpiderItem))
        _l_(416369)

        _n_(416370, "item", lambda: item)['author'] = _c_(416377, _a_(416376, _c_(416375, _a_(416374, _c_(416373, _a_(416372, _n_(416371, "response", lambda: response), "xpath"), '//div[@class="name"]/a/text()'), "extract_first")), "strip"))
        _l_(416378)
        _n_(416379, "item", lambda: item)['timestamp'] = _c_(416386, _a_(416385, _c_(416384, _a_(416383, _c_(416382, _a_(416381, _n_(416380, "response", lambda: response), "xpath"), '//div/@datetime'), "extract_first")), "split"), 't')[0] # %Y-%m-%d
        _l_(416387) # %Y-%m-%d
        _n_(416388, "item", lambda: item)['title'] = _c_(416395, _a_(416394, _c_(416393, _a_(416392, _c_(416391, _a_(416390, _n_(416389, "response", lambda: response), "xpath"), '//h1[@class="header"]/text()'), "extract_first")), "strip"))
        _l_(416396)
        _n_(416397, "item", lambda: item)['body'] = _c_(416404, _a_(416398, ' ', "join"), _c_(416403, _a_(416402, _c_(416401, _a_(416400, _n_(416399, "response", lambda: response), "xpath"), '//div[@class="post-full-text contents js-post-full-text"]/p//text()'), "extract")))
        _l_(416405)
        _n_(416406, "item", lambda: item)['quotes'] = _c_(416413, _a_(416407, ';;;', "join"), _c_(416412, _a_(416411, _c_(416410, _a_(416409, _n_(416408, "response", lambda: response), "xpath"), '//div[@class="post-full-text contents js-post-full-text"]/blockquote//text()'), "extract")))
        _l_(416414)
        _n_(416415, "item", lambda: item)['int_links'] = _c_(416422, _a_(416416, ';;;', "join"), _c_(416421, _a_(416420, _c_(416419, _a_(416418, _n_(416417, "response", lambda: response), "xpath"), '//div[@class="post-full-text contents js-post-full-text"]/p/a/@href'), "extract")))
        _l_(416423)
        _tmp = [_c_(416426, _a_(416425, _n_(416424, "elem", lambda: elem), "replace"), '#','') for elem in _c_(416431, _a_(416430, _c_(416429, _a_(416428, _n_(416427, "response", lambda: response), "xpath"), '//div[@class="tags"]/ul/li/a/text()'), "extract"))]
        _l_(416432)
        _n_(416433, "item", lambda: item)['tags'] = _c_(416439, _a_(416434, ';;;', "join"), [_c_(416437, _a_(416436, _n_(416435, "elem", lambda: elem), "replace"), ' ','') for elem in _n_(416438, "_tmp", lambda: _tmp)])
        _l_(416440)
        _n_(416441, "item", lambda: item)['link'] = _a_(416443, _n_(416442, "response", lambda: response), "url")
        _l_(416444)
        _n_(416445, "item", lambda: item)['news_id'] = _c_(416450, _n_(416446, "str", lambda: str), _c_(416449, _n_(416447, "hash", lambda: hash), _n_(416448, "item", lambda: item)['link']))
        _l_(416451)

        yield _n_(416452, "item", lambda: item)
        _l_(416453)