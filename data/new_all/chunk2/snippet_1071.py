# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46520034/attributeerror-function-object-has-no-attribute-method-for-if-request-metho
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(447377)
try:
    from flask import Flask, render_template, flash, request, url_for, redirect, session, g
    _l_(447379)

except ImportError:
    pass
try:
    import controllers
    _l_(447381)

except ImportError:
    pass
try:
    import config
    _l_(447383)

except ImportError:
    pass
try:
    from functools import wraps
    _l_(447385)

except ImportError:
    pass
try:
    import argparse
    _l_(447387)

except ImportError:
    pass
try:
    import json
    _l_(447389)

except ImportError:
    pass
try:
    import pprint
    _l_(447391)

except ImportError:
    pass
try:
    import requests
    _l_(447393)

except ImportError:
    pass
try:
    import sys
    _l_(447395)

except ImportError:
    pass
try:
    import urllib
    _l_(447397)

except ImportError:
    pass

# this client code can run on Python 2.x or 3.x.  Your imports can be
# simpler if you only need one of those.
try:
    _l_(447409)

    # For Python 3.0 and later
    from urllib.error import HTTPError
    _l_(447398)
    from urllib.parse import quote
    _l_(447399)
    from urllib.parse import urlencode
    _l_(447400)
except _n_(447401, "ImportError", lambda: ImportError):
    _l_(447408)

    try:
        from urllib2 import HTTPError
        _l_(447403)

    except ImportError:
        pass
    try:
        from urllib import quote
        _l_(447405)

    except ImportError:
        pass
    try:
        from urllib import urlencode
        _l_(447407)

    except ImportError:
        pass

@_c_(447412, _a_(447411, _n_(447410, "app", lambda: app), "route"), '/',  methods=["GET","POST"])
def main_route():
    _l_(447428)

    if _a_(447414, _n_(447413, "request", lambda: request), "method") == "POST":
        _l_(447424)

        input_place = _a_(447416, _n_(447415, "request", lambda: request), "form")['location']
        _l_(447417)
        input_type = _a_(447419, _n_(447418, "request", lambda: request), "form")['type']
        _l_(447420)
        aux = _c_(447422, _n_(447421, "render_template", lambda: render_template), 'index.html')
        _l_(447423)
        return aux
    aux = _c_(447426, _n_(447425, "render_template", lambda: render_template), 'index.html')
    _l_(447427)
    return aux