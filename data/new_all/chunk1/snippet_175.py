# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34572553/django-attributeerror-nonetype-object-has-no-attribute-split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os, shutil
    _l_(418591)

except ImportError:
    pass
try:
    from django.conf import settings
    _l_(418593)

except ImportError:
    pass
try:
    from django.core.management import call_command
    _l_(418595)

except ImportError:
    pass
try:
    from django.core.management.base import BaseCommand
    _l_(418597)

except ImportError:
    pass
try:
    from django.core.urlresolvers import reverse
    _l_(418599)

except ImportError:
    pass
try:
    from django.test.client import Client
    _l_(418601)

except ImportError:
    pass

def get_pages():
    _l_(418614)

    for name in _c_(418606, _a_(418603, _n_(418602, "os", lambda: os), "listdir"), _a_(418605, _n_(418604, "settings", lambda: settings), "STATIC_PAGES_DIRECTORY")):
        _l_(418613)

        if _c_(418609, _a_(418608, _n_(418607, "name", lambda: name), "endswith"), '.html'):
            _l_(418612)

            yield _n_(418610, "name", lambda: name)[:-5]
            _l_(418611)


class Command(_n_(418615, "BaseCommand", lambda: BaseCommand)):
    _l_(418693)

    help = 'Build static site output.'
    _l_(418616)

    def handle(self, *args, **options):
        _l_(418692)

        """Request pages and build output."""
        if _c_(418622, _a_(418619, _a_(418618, _n_(418617, "os", lambda: os), "path"), "exists"), _a_(418621, _n_(418620, "settings", lambda: settings), "SITE_OUTPUT_DIRECTORY")):
            _l_(418629)

            _c_(418627, _a_(418624, _n_(418623, "shutil", lambda: shutil), "rmtree"), _a_(418626, _n_(418625, "settings", lambda: settings), "SITE_OUTPUT_DIRECTORY"))
            _l_(418628)
        _c_(418634, _a_(418631, _n_(418630, "os", lambda: os), "mkdir"), _a_(418633, _n_(418632, "settings", lambda: settings), "SITE_OUTPUT_DIRECTORY")) 
        _l_(418635) 
        _c_(418640, _a_(418637, _n_(418636, "os", lambda: os), "makedirs"), _a_(418639, _n_(418638, "settings", lambda: settings), "STATIC_ROOT"))   
        _l_(418641)   
        _c_(418643, _n_(418642, "call_command", lambda: call_command), 'collectstatic', interactive=False, clear=True, verbosity=0)
        _l_(418644)
        this_client_will = _c_(418646, _n_(418645, "Client", lambda: Client))
        _l_(418647)

        for page in _c_(418649, _n_(418648, "get_pages", lambda: get_pages)):
            _l_(418691)

            the_page_url = _c_(418652, _n_(418650, "reverse", lambda: reverse), 'page',kwargs={'slug': _n_(418651, "page", lambda: page)})      # PROBLEM SEEMS TO GENERATE STARTING HERE
            _l_(418653)      # PROBLEM SEEMS TO GENERATE STARTING HERE
            response = _c_(418657, _a_(418655, _n_(418654, "this_client_will", lambda: this_client_will), "get"), _n_(418656, "the_page_url", lambda: the_page_url))
            _l_(418658)
            if _n_(418659, "page", lambda: page) == 'index.html':
                _l_(418676)

                output_dir = _a_(418661, _n_(418660, "settings", lambda: settings), "SITE_OUTPUT_DIRECTORY")
                _l_(418662)
            else:
                output_dir = _c_(418669, _a_(418665, _a_(418664, _n_(418663, "os", lambda: os), "path"), "join"), _a_(418667, _n_(418666, "settings", lambda: settings), "SITE_OUTPUT_DIRECTORY"), _n_(418668, "page", lambda: page))
                _l_(418670)
                _c_(418674, _a_(418672, _n_(418671, "os", lambda: os), "makedirs"), _n_(418673, "output_dir", lambda: output_dir))
                _l_(418675)
            with _c_(418683, _n_(418677, "open", lambda: open), _c_(418682, _a_(418680, _a_(418679, _n_(418678, "os", lambda: os), "path"), "join"), _n_(418681, "output_dir", lambda: output_dir), 'index.html'), 'wb', encoding='utf8') as f:
                _l_(418690)

                _c_(418688, _a_(418685, _n_(418684, "f", lambda: f), "write"), _a_(418687, _n_(418686, "response", lambda: response), "content"))
                _l_(418689)