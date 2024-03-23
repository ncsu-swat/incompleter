# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70967843/how-to-deal-with-typeerror-cannot-concatenate-object-of-type-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(590576)

except ImportError:
    pass
try:
    import shutil
    _l_(590578)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(590580)

except ImportError:
    pass

src_dir_path = r'D:\1. SEC EDGAR年报数据' 
_l_(590581) 
to_dir_path = r'D:\12 年报提取尝试'  
_l_(590582)  
df = _c_(590585, _a_(590584, _n_(590583, "pd", lambda: pd), "read_excel"), r'D:\11. 年报提取尝试\CIK代码.xlsx')
_l_(590586)
ciklist = _c_(590594, _n_(590587, "list", lambda: list), _c_(590593, _n_(590588, "map", lambda: map), _n_(590589, "str", lambda: str), _c_(590592, _a_(590591, _n_(590590, "df", lambda: df)['cik_full'], "tolist"))))
_l_(590595)
key1 = _n_(590596, "ciklist", lambda: ciklist) 
_l_(590597) 

filelist = _c_(590601, _a_(590599, _n_(590598, "os", lambda: os), "listdir"), _n_(590600, "src_dir_path", lambda: src_dir_path))  
_l_(590602)  
for row in _n_(590603, "df", lambda: df):
    _l_(590609)

    _c_(590607, _a_(590605, _n_(590604, "df", lambda: df), "append"), _n_(590606, "row", lambda: row))
    _l_(590608)


def printallfiles(dirs, abspath):
    _l_(590644)

    for file in _n_(590610, "dirs", lambda: dirs):
        _l_(590643)

        sub_path = _c_(590616, _a_(590613, _a_(590612, _n_(590611, "os", lambda: os), "path"), "join"), _n_(590614, "abspath", lambda: abspath), _n_(590615, "file", lambda: file))  
        _l_(590617)  
        if _c_(590622, _a_(590620, _a_(590619, _n_(590618, "os", lambda: os), "path"), "isdir"), _n_(590621, "sub_path", lambda: sub_path)):
            _l_(590642)

            temppath = _c_(590626, _a_(590624, _n_(590623, "os", lambda: os), "listdir"), _n_(590625, "sub_path", lambda: sub_path))
            _l_(590627)
            _c_(590631, _n_(590628, "printallfiles", lambda: printallfiles), _n_(590629, "temppath", lambda: temppath), _n_(590630, "sub_path", lambda: sub_path))  
            _l_(590632)  
        else:
            if _n_(590633, "key1", lambda: key1) in _n_(590634, "file", lambda: file):
                _l_(590641)

                _c_(590639, _a_(590636, _n_(590635, "shutil", lambda: shutil), "copy"), _n_(590637, "sub_path", lambda: sub_path), _n_(590638, "to_dir_path", lambda: to_dir_path))
                _l_(590640)


_c_(590648, _n_(590645, "printallfiles", lambda: printallfiles), _n_(590646, "filelist", lambda: filelist), _n_(590647, "src_dir_path", lambda: src_dir_path)) 
_l_(590649) 