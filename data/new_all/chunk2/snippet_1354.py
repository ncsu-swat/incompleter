# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75229680/problem-in-class-when-use-dictionary-attributeerror-my-data-object-has-no-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Page1(_a_(458352, _n_(458351, "tk", lambda: tk), "Frame")):
    _l_(458406)

    def __init__(self, master, other, **kw):
        _l_(458405)

        _c_(458357, _a_(458354, _n_(458353, "super", lambda: super)(), "__init__"), _n_(458355, "master", lambda: master), **_n_(458356, "kw", lambda: kw))
        _l_(458358)
        _c_(458361, _a_(458360, _n_(458359, "self", lambda: self), "configure"), bg='white')
        _l_(458362)

        class My_Data():
            _l_(458373)

            def __init__(self, Name, Year, Other):
                _l_(458372)

                _n_(458363, "self", lambda: self).Name: _n_(458364, "str", lambda: str)
                _l_(458365)
                _n_(458366, "self", lambda: self).Year: _n_(458367, "float", lambda: float)
                _l_(458368)
                _n_(458369, "self", lambda: self).Other: _n_(458370, "float", lambda: float)
                _l_(458371)
        def function1(self):
            _l_(458404)

            My_Dictionary = {}
            _l_(458374)
            x = _c_(458377, _a_(458376, _n_(458375, "cursor", lambda: cursor), "execute"), "sql")
            _l_(458378)

            for row in _c_(458381, _a_(458380, _n_(458379, "x", lambda: x), "fetchall")):
                _l_(458403)

                if _n_(458382, "row", lambda: row)[0] not in _n_(458383, "My_Dictionary", lambda: My_Dictionary):
                    _l_(458395)

                    Data = _c_(458389, _n_(458384, "My_Data", lambda: My_Data), Name=_n_(458385, "row", lambda: row)[1],
                        Year=_n_(458386, "row", lambda: row)[2],
                        Other=_c_(458388, _n_(458387, "list", lambda: list)))
                    _l_(458390)

                    _n_(458391, "My_Dictionary", lambda: My_Dictionary)[_n_(458392, "row", lambda: row)[0]] = _n_(458393, "info", lambda: info)
                    _l_(458394)
                _c_(458401, _a_(458399, _a_(458398, _n_(458396, "My_Dictionary", lambda: My_Dictionary)[_n_(458397, "row", lambda: row)[0]], "Other"), "append"), _n_(458400, "row", lambda: row)[3])
                _l_(458402)