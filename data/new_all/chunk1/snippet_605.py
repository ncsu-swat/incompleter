# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73666495/how-to-avoid-attributeerror-nonetype-object-has-no-attribute-text-webscrapi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(406176)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(406178)

except ImportError:
    pass
try:
    import webbrowser
    _l_(406180)

except ImportError:
    pass

while True:
    _l_(406224)

    url = _c_(406183, _a_(406182, _n_(406181, "requests", lambda: requests), "get"), "https://www.reddit.com/r/random")
    _l_(406184)
    soup = _c_(406188, _n_(406185, "BeautifulSoup", lambda: BeautifulSoup), _a_(406187, _n_(406186, "url", lambda: url), "content"), "html.parser")
    _l_(406189)
    title = _a_(406193, _c_(406192, _a_(406191, _n_(406190, "soup", lambda: soup), "find"), class_="_2yYPPW47QxD4lFQTKpfpLQ"), "text") ## this is supposed to get the title of the subreddit and this is where my error is occurring
    _l_(406194) ## this is supposed to get the title of the subreddit and this is where my error is occurring

    _c_(406197, _n_(406195, "print", lambda: print), f"{_n_(406196, 'title', lambda: title)} \nSelect this subreddit? (Y/N)")
    _l_(406198)
    ans = _c_(406202, _a_(406201, _c_(406200, _n_(406199, "input", lambda: input), ""), "lower"))
    _l_(406203)

    if _n_(406204, "ans", lambda: ans) == "y":
        _l_(406223)

        url = "https://www.reddit.com/%s" % _n_(406205, "title", lambda: title) ## Some issue, not sure what
        _l_(406206) ## Some issue, not sure what
        _c_(406210, _a_(406208, _n_(406207, "webbrowser", lambda: webbrowser), "open"), _n_(406209, "url", lambda: url))
        _l_(406211)
        break
        _l_(406212)
    elif _n_(406213, "ans", lambda: ans) == "n":
        _l_(406222)

        _c_(406215, _n_(406214, "print", lambda: print), "Try again!")
        _l_(406216)
        continue
        _l_(406217)
    else:
        _c_(406219, _n_(406218, "print", lambda: print), "Wrong choice!")
        _l_(406220)
        break
        _l_(406221)