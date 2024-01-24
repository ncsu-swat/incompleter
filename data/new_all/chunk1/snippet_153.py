# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69187685/getting-attributeerror-module-base64-has-no-attribute-decodestring-error-wh
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from ldif3 import LDIFParser
    _l_(381410)

except ImportError:
    pass

parser = _c_(381414, _n_(381411, "LDIFParser", lambda: LDIFParser), _c_(381413, _n_(381412, "open", lambda: open), 'dse3.ldif', 'rb'))
_l_(381415)
for dn, entry in _c_(381418, _a_(381417, _n_(381416, "parser", lambda: parser), "parse")):
    _l_(381427)

    if _n_(381419, "dn", lambda: dn) == "cn=Schema Compatibility,cn=plugins,cn=config":
        _l_(381426)

        if _n_(381420, "entry", lambda: entry)['nsslapd-pluginEnabled'] == ['on']:
            _l_(381425)

            _c_(381423, _n_(381421, "print", lambda: print), 'Entry record: %s' % _n_(381422, "dn", lambda: dn))
            _l_(381424)