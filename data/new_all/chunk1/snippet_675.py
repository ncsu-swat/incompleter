# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59577129/python3-concatenate-str-not-bytes-to-bytes-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_dictonary = {
         "subfolder\a_file.bin" :  ["A3", "B3", "2400"] ,
         "subfolder\b_file.bin" :  ["A4", "B4", "3000"] , 
}
_l_(400750)

for d in _n_(400751, "my_dictonary", lambda: my_dictonary) :
    _l_(400801)

    with _c_(400754, _n_(400752, "open", lambda: open), _n_(400753, "d", lambda: d), "rb") as r:
        _l_(400758)

data = _c_(400757, _a_(400756, _n_(400755, "r", lambda: r), "read"))
    content= ""
    _l_(400759)

    for line in _n_(400760, "my_dictonary", lambda: my_dictonary)[_n_(400761, "d", lambda: d)]:
        _l_(400767)

        content= _n_(400762, "content", lambda: content)+ _c_(400765, _n_(400763, "str", lambda: str), _n_(400764, "line", lambda: line)) + "\n"
        _l_(400766)

    file_set = _c_(400769, _n_(400768, "set", lambda: set))
    _l_(400770)

    for filename in _c_(400773, _a_(400772, _n_(400771, "glob", lambda: glob), "iglob"), './**/*', recursive=True):
        _l_(400783)

        _c_(400781, _a_(400775, _n_(400774, "file_set", lambda: file_set), "add"), _c_(400780, _a_(400778, _a_(400777, _n_(400776, "os", lambda: os), "path"), "abspath"), _n_(400779, "filename", lambda: filename)))
        _l_(400782)

    f_slice = _c_(400786, _a_(400785, _n_(400784, "d", lambda: d), "split"), '\\')
    _l_(400787)
    f_slice = _c_(400790, _a_(400789, _n_(400788, "f_slice", lambda: f_slice)[1], "split"), ".bin")
    _l_(400791)
    file_n = ""
    _l_(400792)
    for e in _n_(400793, "file_set", lambda: file_set):
        _l_(400800)

        if _n_(400794, "f_slice", lambda: f_slice)[0] in _n_(400795, "e", lambda: e) and ".cap" in _n_(400796, "e", lambda: e):
            _l_(400799)

            file_n = _n_(400797, "e", lambda: e)
            _l_(400798)

with _c_(400804, _n_(400802, "open", lambda: open), _n_(400803, "file_n", lambda: file_n), 'wb') as f:
    _l_(400810)

_c_(400809, _a_(400806, _n_(400805, "f", lambda: f), "write"), _n_(400807, "content", lambda: content) + _n_(400808, "data", lambda: data)