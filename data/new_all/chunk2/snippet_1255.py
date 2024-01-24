# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62740709/typeerror-init-got-an-unexpected-keyword-argument-choices-in-pythons-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(455940)

except ImportError:
    pass

parser = _c_(455943, _a_(455942, _n_(455941, "argparse", lambda: argparse), "ArgumentParser"))
_l_(455944)
_c_(455947, _a_(455946, _n_(455945, "parser", lambda: parser), "add_argument"), '-u', '--url',help='Passing one url')
_l_(455948)
_c_(455951, _a_(455950, _n_(455949, "parser", lambda: parser), "add_argument"), '-t', '--type', action='store_true',help='To download pages/posts', choices=['pages', 'posts'])
_l_(455952)
args = _c_(455955, _a_(455954, _n_(455953, "parser", lambda: parser), "parse_args"))
_l_(455956)

url = _a_(455958, _n_(455957, "args", lambda: args), "url")
_l_(455959)

if _a_(455961, _n_(455960, "args", lambda: args), "type") == "pages":
    _l_(455964)

    url_link = _n_(455962, "url", lambda: url) + "/wp-json/wp/v2/pages/?per_page=100"
    _l_(455963)
if _a_(455966, _n_(455965, "args", lambda: args), "type") == "posts":
    _l_(455969)

    url_link = _n_(455967, "url", lambda: url) + "/wp-json/wp/v2/posts/?per_page=100"
    _l_(455968)