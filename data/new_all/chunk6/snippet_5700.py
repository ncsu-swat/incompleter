# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48948539/odd-attributeerror-nonetype-object-has-no-attribute-group-error
#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(345115)

except ImportError:
    pass
try:
    import itertools
    _l_(345117)

except ImportError:
    pass

with _c_(345119, _n_(345118, "open", lambda: open), 'Desktop/data.txt', 'r') as myfile:
    _l_(345126)

    data=_c_(345124, _a_(345123, _c_(345122, _a_(345121, _n_(345120, "myfile", lambda: myfile), "read")), "replace"), '\n', '')
    _l_(345125)

num = 0
_l_(345127)

for x in _c_(345130, _a_(345129, _n_(345128, "itertools", lambda: itertools), "repeat"), None, 8):
    _l_(345196)

    num = _c_(345133, _n_(345131, "int", lambda: int), _n_(345132, "num", lambda: num)) + 1
    _l_(345134)
    if _c_(345137, _n_(345135, "int", lambda: int), _n_(345136, "num", lambda: num)) < 10:
        _l_(345142)

        num = '0' + _c_(345140, _n_(345138, "str", lambda: str), _n_(345139, "num", lambda: num))
        _l_(345141)
    firstString = _c_(345149, _a_(345148, _c_(345147, _a_(345144, _n_(345143, "re", lambda: re), "search"), r"id=\"question_" + _n_(345145, "num", lambda: num) + "_whole_question\" data-sidebar-reference=\"\">    (.*?) <input", _n_(345146, "data", lambda: data)), "group"), 1)
    _l_(345150)
    secondString = _c_(345157, _a_(345156, _c_(345155, _a_(345152, _n_(345151, "re", lambda: re), "search"), r"id=\"question_" + _n_(345153, "num", lambda: num) + "_wol_1\"(.*?)  </div>", _n_(345154, "data", lambda: data)), "group"), 1)
    _l_(345158)
    secondString = _c_(345162, _a_(345160, _n_(345159, "secondString", lambda: secondString), "replace"), " name=\"question_" + _n_(345161, "num", lambda: num) + "_wol_1\" onchange=\"has_unsaved_work();\" size=\"10\" type=\"text\" />", "")
    _l_(345163)
    finalString = _n_(345164, "firstString", lambda: firstString) + " _" + _n_(345165, "secondString", lambda: secondString)
    _l_(345166)
    englishWord = _c_(345170, _a_(345168, _n_(345167, "re", lambda: re), "search"), r"(<i><span lang=\"en-US\">(.*?)</span></i>)", _n_(345169, "finalString", lambda: finalString))
    _l_(345171)
    englishWord = _c_(345179, _a_(345178, _c_(345177, _a_(345173, _n_(345172, "re", lambda: re), "search"), r"<i>(.*?)</i>", _c_(345176, _n_(345174, "str", lambda: str), _n_(345175, "englishWord", lambda: englishWord))), "group"), 1)
    _l_(345180)
    englishWord = "<i>" + _n_(345181, "englishWord", lambda: englishWord) + "</i>"
    _l_(345182)
    finalString = _c_(345186, _a_(345184, _n_(345183, "finalString", lambda: finalString), "replace"), _n_(345185, "englishWord", lambda: englishWord), "")
    _l_(345187)
    finalString = _c_(345190, _a_(345189, _n_(345188, "finalString", lambda: finalString), "replace"), "()", "")
    _l_(345191)
    _c_(345194, _n_(345192, "print", lambda: print), _n_(345193, "finalString", lambda: finalString))
    _l_(345195)