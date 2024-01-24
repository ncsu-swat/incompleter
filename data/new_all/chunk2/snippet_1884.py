# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76196828/nameerror-global-name-open-is-not-defined-error-in-init-py-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CustomAgent(_a_(436440, _n_(436439, "Agent", lambda: Agent), "Movies")):
    _l_(436452)

    def update(self, metadata, media, lang):
        _l_(436451)

        with _c_(436442, _n_(436441, "open", lambda: open), "db.tsv", "r") as fp:
            _l_(436450)

            line = _c_(436445, _a_(436444, _n_(436443, "fp", lambda: fp), "readline"))
            _l_(436446)
            while _n_(436447, "line", lambda: line):
                _l_(436449)

                ...
                _l_(436448)