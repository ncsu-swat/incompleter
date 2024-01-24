# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72518657/typeerror-unsupported-operand-types-for-paragraph-and-str-replace-wor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from docx import Document
    _l_(471062)

except ImportError:
    pass

document = _c_(471064, _n_(471063, "Document", lambda: Document), 'rea.docx')
_l_(471065)

for paragraph in _a_(471067, _n_(471066, "document", lambda: document), "paragraphs"):
    _l_(471077)

    if _n_(471068, "paragraph", lambda: paragraph)+'Ocean' in _a_(471070, _n_(471069, "paragraph", lambda: paragraph), "text"):
        _l_(471076)

        _c_(471074, _a_(471073, _a_(471072, _n_(471071, "paragraph", lambda: paragraph), "text"), "replace"), "Sea")
        _l_(471075)