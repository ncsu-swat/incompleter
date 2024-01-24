# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54858344/python-error-attributeerror-nonetype-object-has-no-attribute-text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import warnings
    _l_(458271)

except ImportError:
    pass
try:
    import requests
    _l_(458273)

except ImportError:
    pass
try:
    from colorama import init
    _l_(458275)

except ImportError:
    pass
_c_(458277, _n_(458276, "init", lambda: init), autoreset=True)
_l_(458278)
try:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    _l_(458280)

except ImportError:
    pass
_c_(458284, _a_(458282, _n_(458281, "warnings", lambda: warnings), "simplefilter"), "ignore", _n_(458283, "UserWarning", lambda: UserWarning))
_l_(458285)
_c_(458289, _a_(458287, _n_(458286, "warnings", lambda: warnings), "simplefilter"), 'ignore', _n_(458288, "InsecureRequestWarning", lambda: InsecureRequestWarning))
_l_(458290)
try:
    from bs4 import BeautifulSoup as BS
    _l_(458292)

except ImportError:
    pass


with _c_(458294, _n_(458293, "open", lambda: open), 'ips.txt','r') as urls:
    _l_(458328)

    for url in _c_(458297, _a_(458296, _n_(458295, "urls", lambda: urls), "readlines")):
        _l_(458327)

        req = _c_(458300, _a_(458299, _n_(458298, "url", lambda: url), "strip"))
        _l_(458301)
        try:
            _l_(458326)

            page=_c_(458305, _a_(458303, _n_(458302, "requests", lambda: requests), "get"), _n_(458304, "req", lambda: req), verify=False, allow_redirects=False, stream=True, timeout=10)
            _l_(458306)
            soup = _c_(458310, _n_(458307, "BS", lambda: BS), _a_(458309, _n_(458308, "page", lambda: page), "text"))
            _l_(458311)

            _c_(458318, _n_(458312, "print", lambda: print), '\033[32m' + _n_(458313, "req", lambda: req) + ' - Title: ', _a_(458317, _c_(458316, _a_(458315, _n_(458314, "soup", lambda: soup), "find"), 'title'), "text"))
            _l_(458319)
        except _a_(458321, _n_(458320, "requests", lambda: requests), "RequestException") as e:
            _l_(458325)

            _c_(458323, _n_(458322, "print", lambda: print), '[!] Timeout!')
            _l_(458324)