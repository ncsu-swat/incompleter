# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70395860/how-to-fix-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
lines = _c_(580530, _a_(580529, _c_(580528, _a_(580527, _n_(580526, "subprocess", lambda: subprocess), "check_output"), [
        "git",
        "log",
        "--all",
        "--no-merges",
        "--shortstat",
        "--reverse",
        "--pretty=format:'%ad;%an'",
    ]
), "splitlines"))
_l_(580531)

for line in _n_(580532, "lines", lambda: lines):
    _l_(580543)

    _c_(580535, _n_(580533, "print", lambda: print), _n_(580534, "line", lambda: line))
    _l_(580536)
    if "file changed" in _n_(580537, "line", lambda: line) or "files changed" in _n_(580538, "line", lambda: line):
        _l_(580542)

        _c_(580540, _n_(580539, "print", lambda: print), "do something")
        _l_(580541)