# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44307828/export-a-tex-file-file-from-python-script-typeerror-a-float-is-required
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(393094, _n_(393090, "open", lambda: open), _n_(393091, "directoryPath", lambda: directoryPath) + _a_(393093, _n_(393092, "os", lambda: os), "sep") +'commonTables3.tex','w') as f:
    _l_(393102)

    _c_(393100, _a_(393096, _n_(393095, "f", lambda: f), "write"), _n_(393097, "content", lambda: content)%({'index':_c_(393099, _n_(393098, "str", lambda: str), 3)}))
    _l_(393101)