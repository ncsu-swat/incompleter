# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54279772/filenotfounderror-errno-2-no-such-file-or-directory-ubuntu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(402518, _n_(402517, "open", lambda: open), './folder/tickets.csv', 'w', encoding='utf-8') as ouf:
    _l_(402530)

    for i in _n_(402519, "d", lambda: d):
        _l_(402529)

        i = _c_(402522, _n_(402520, "str", lambda: str), _n_(402521, "i", lambda: i))
        _l_(402523)
        _c_(402527, _a_(402525, _n_(402524, "ouf", lambda: ouf), "write"), _n_(402526, "i", lambda: i) + '\n')
        _l_(402528)