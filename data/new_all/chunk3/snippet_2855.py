# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60849087/attributeerror-nonetype-object-has-no-attribute-name-error-occurs-when-i-tr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from docx import Document
    _l_(568152)

except ImportError:
    pass
document=_c_(568154, _n_(568153, "Document", lambda: Document), 'C:\\Users\\abc\\Desktop\\check\\Leave_Policy_converted.docx')
_l_(568155)
for paragraph in _a_(568157, _n_(568156, "document", lambda: document), "paragraphs"):
    _l_(568167)

    if _a_(568160, _a_(568159, _n_(568158, "paragraph", lambda: paragraph), "style"), "name") == 'Heading 1':
        _l_(568166)

        _c_(568164, _n_(568161, "print", lambda: print), _a_(568163, _n_(568162, "paragraph", lambda: paragraph), "text"))
        _l_(568165)