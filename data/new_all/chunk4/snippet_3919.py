# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64912514/filenotfounderror-even-though-the-file-exists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(608124, _n_(608123, "open", lambda: open), '../assets/database/database.json','r') as E:
    _l_(608130)

    stuffs = _c_(608128, _a_(608126, _n_(608125, "json", lambda: json), "load"), _n_(608127, "E", lambda: E))
    _l_(608129)