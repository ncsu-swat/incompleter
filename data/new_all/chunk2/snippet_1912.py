# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36877016/typeerror-str-does-not-support-the-buffer-interface-in-html2text
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib
    _l_(422567)

except ImportError:
    pass
try:
    import html2text
    _l_(422569)

except ImportError:
    pass
url='http://www.google.com'
_l_(422570)
page = _c_(422575, _a_(422573, _a_(422572, _n_(422571, "urllib", lambda: urllib), "request"), "urlopen"), _n_(422574, "url", lambda: url))
_l_(422576)
html_content = _c_(422579, _a_(422578, _n_(422577, "page", lambda: page), "read"))
_l_(422580)
rendered_content = _c_(422584, _a_(422582, _n_(422581, "html2text", lambda: html2text), "html2text"), _n_(422583, "html_content", lambda: html_content))
_l_(422585)