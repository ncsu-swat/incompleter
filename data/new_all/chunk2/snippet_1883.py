# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76196828/nameerror-global-name-open-is-not-defined-error-in-init-py-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class CustomAgent(_a_(461184, _n_(461183, "Agent", lambda: Agent), "Movies")):
    _l_(461197)

    def update(self, metadata, media, lang):
        _l_(461196)

        uri = "http://domain.tld/file?id=%s" % _c_(461189, _a_(461186, _n_(461185, "urllib", lambda: urllib), "quote"), _a_(461188, _n_(461187, "metadata", lambda: metadata), "id"))
        _l_(461190)
        data = _c_(461194, _a_(461192, _n_(461191, "JSON", lambda: JSON), "ObjectFromURL"), _n_(461193, "uri", lambda: uri))
        _l_(461195)