# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55231027/attributeerror-nonetype-object-has-no-attribute-get-text-python-3x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def MainPageSpider(max_pages):
    _l_(371161)

    page = 1
    _l_(371125)
    while _n_(371126, "page", lambda: page) <= _n_(371127, "max_pages", lambda: max_pages):
        _l_(371160)

        url = 'url' + _c_(371130, _n_(371128, "str", lambda: str), _n_(371129, "page", lambda: page))
        _l_(371131)
        source_code = _c_(371135, _a_(371133, _n_(371132, "requests", lambda: requests), "get"), _n_(371134, "url", lambda: url))
        _l_(371136)
        plain_text = _a_(371138, _n_(371137, "source_code", lambda: source_code), "text")
        _l_(371139)
        soup = _c_(371142, _n_(371140, "bs", lambda: bs), _n_(371141, "plain_text", lambda: plain_text), 'html.parser')
        _l_(371143)
        for link in _c_(371146, _a_(371145, _n_(371144, "soup", lambda: soup), "findAll"), attrs={'class':'col4'}):
            _l_(371158)

            href = 'url' + _a_(371148, _n_(371147, "link", lambda: link), "a")['href']
            _l_(371149)
            title = _a_(371152, _a_(371151, _n_(371150, "link", lambda: link), "span"), "text")
            _l_(371153)

            _c_(371156, _n_(371154, "PostPageItems", lambda: PostPageItems), _n_(371155, "href", lambda: href))
            _l_(371157)
        page += 1
        _l_(371159)


def PostPageItems(post_url):
    _l_(371188)

    source_code = _c_(371165, _a_(371163, _n_(371162, "requests", lambda: requests), "get"), _n_(371164, "post_url", lambda: post_url))
    _l_(371166)
    plain_text = _a_(371168, _n_(371167, "source_code", lambda: source_code), "text")
    _l_(371169)
    soup = _c_(371172, _n_(371170, "bs", lambda: bs), _n_(371171, "plain_text", lambda: plain_text), 'html.parser')
    _l_(371173)
    for items in _c_(371176, _a_(371175, _n_(371174, "soup", lambda: soup), "findAll"), attrs={'class':'container'}):
        _l_(371187)

        title2 = _c_(371181, _a_(371180, _c_(371179, _a_(371178, _n_(371177, "items", lambda: items), "find"), 'h1', {'class':'title'}), "get_text"))
        _l_(371182)

        _c_(371185, _n_(371183, "print", lambda: print), _n_(371184, "title2", lambda: title2))
        _l_(371186)




_c_(371190, _n_(371189, "MainPageSpider", lambda: MainPageSpider), 1)
_l_(371191)