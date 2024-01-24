# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55809581/attributeerror-regexpreplacer-object-has-no-attribute-replace
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(382693)

except ImportError:
    pass
replacement_patterns = [
(r'won\'t', 'will not'),
(r'can\'t', 'cannot'),
(r'i\'m', 'i am'),
(r'ain\'t', 'is not'),
(r'(\w+)\'ll', '\g<1> will'),
(r'(\w+)n\'t', '\g<1> not'),
(r'(\w+)\'ve', '\g<1> have'),
(r'(\w+)\'s', '\g<1> is'),
(r'(\w+)\'re', '\g<1> are'),
(r'(\w+)\'d', '\g<1> would')
]
_l_(382694)
class RegexpReplacer(_n_(382695, "object", lambda: object)):
    _l_(382721)

    def __init__(self, patterns=_n_(382696, "replacement_patterns", lambda: replacement_patterns)):
        _l_(382720)

        _n_(382697, "self", lambda: self).patterns = [(_c_(382701, _a_(382699, _n_(382698, "re", lambda: re), "compile"), _n_(382700, "regex", lambda: regex)), _n_(382702, "repl", lambda: repl)) for (regex, repl) in _n_(382703, "patterns", lambda: patterns)]
        _l_(382704)
        def replace(self, text):
            _l_(382719)

            s = _n_(382705, "text", lambda: text)
            _l_(382706)
            for (pattern, repl) in _a_(382708, _n_(382707, "self", lambda: self), "patterns"):
                _l_(382718)

                s = _c_(382714, _a_(382710, _n_(382709, "re", lambda: re), "sub"), _n_(382711, "pattern", lambda: pattern), _n_(382712, "repl", lambda: repl), _n_(382713, "s", lambda: s))
                _l_(382715)
                aux = _n_(382716, "s", lambda: s)
                _l_(382717)
                return aux
replacer=_c_(382723, _n_(382722, "RegexpReplacer", lambda: RegexpReplacer))
_l_(382724)
_c_(382729, _n_(382725, "print", lambda: print), _c_(382728, _a_(382727, _n_(382726, "replacer", lambda: replacer), "replace"), "can't is a contradicton"))
_l_(382730)