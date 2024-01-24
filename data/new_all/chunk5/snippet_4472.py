# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57024304/how-to-fix-attributeerror-client-object-has-no-attribute-send-message-wit
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(668751)

except ImportError:
    pass
try:
    import requests
    _l_(668753)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(668755)

except ImportError:
    pass

client = _c_(668758, _a_(668757, _n_(668756, "discord", lambda: discord), "Client"))
_l_(668759)

@_a_(668761, _n_(668760, "client", lambda: client), "event")
async def on_ready():
    _l_(668768)

    _c_(668766, _n_(668762, "print", lambda: print), _c_(668765, _a_(668763, 'We have logged in as {0.user}', "format"), _n_(668764, "client", lambda: client)))
    _l_(668767)

channel = _c_(668771, _a_(668770, _n_(668769, "client", lambda: client), "get_channel"), 'CHANNEL ID')
_l_(668772)

@_a_(668774, _n_(668773, "client", lambda: client), "event")
async def on_message(message):
    _l_(668818)

    if _a_(668776, _n_(668775, "message", lambda: message), "author") == _a_(668778, _n_(668777, "client", lambda: client), "user"):
        _l_(668780)

        aux = ""
        _l_(668779)
        return aux

    if _c_(668784, _a_(668783, _a_(668782, _n_(668781, "message", lambda: message), "content"), "startswith"), '!dfx2'):
        _l_(668817)

        website_url = _a_(668788, _c_(668787, _a_(668786, _n_(668785, "requests", lambda: requests), "get"), 'http://novaworld.cc/dfx2lobby.php?lob=pub'), "text")
        _l_(668789)
        soup = _c_(668792, _n_(668790, "BeautifulSoup", lambda: BeautifulSoup), _n_(668791, "website_url", lambda: website_url), 'html.parser')
        _l_(668793)
        table = _c_(668796, _a_(668795, _n_(668794, "soup", lambda: soup), "find"), 'table')
        _l_(668797)
        test = _c_(668800, _a_(668799, _n_(668798, "table", lambda: table), "select_one"), 'tr:contains("!GET SOME")')
        _l_(668801)
        text = _c_(668804, _a_(668803, _n_(668802, "test", lambda: test), "get_text"))
        _l_(668805)
        _c_(668808, _n_(668806, "print", lambda: print), _n_(668807, "text", lambda: text))
        _l_(668809)
        await _c_(668815, _a_(668811, _n_(668810, "channel", lambda: channel), "send"), _a_(668813, _n_(668812, "message", lambda: message), "channel"), content = _n_(668814, "text", lambda: text))
        _l_(668816)

_c_(668821, _a_(668820, _n_(668819, "client", lambda: client), "run"), 'TOKEN')
_l_(668822)