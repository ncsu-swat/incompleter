# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56264449/typeerror-object-of-type-bytes-is-not-json-serializable
#!/usr/bin/python3

# Imports
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(379689)

except ImportError:
    pass
try:
    import base64
    _l_(379691)

except ImportError:
    pass
try:
    from cryptography.fernet import Fernet
    _l_(379693)

except ImportError:
    pass

# Save
def encrypt_string(string, f):
    _l_(379708)

    aux = _c_(379706, _n_(379694, "str", lambda: str), _c_(379705, _a_(379704, _c_(379703, _a_(379696, _n_(379695, "f", lambda: f), "encrypt"), _c_(379702, _a_(379698, _n_(379697, "base64", lambda: base64), "b64encode"), _c_(379701, _n_(379699, "bytes", lambda: bytes), _n_(379700, "string", lambda: string),'utf-8'))), "decode"), 'utf-8'))
    _l_(379707)
    return aux

def encrypt_dict(dict):
    _l_(379748)

    fk = _c_(379713, _a_(379712, _c_(379711, _a_(379710, _n_(379709, "Fernet", lambda: Fernet), "generate_key")), "decode"), 'utf-8')
    _l_(379714)
    f = _c_(379717, _n_(379715, "Fernet", lambda: Fernet), _n_(379716, "fk", lambda: fk))
    _l_(379718)
    ed = {}
    _l_(379719)
    _n_(379720, "ed", lambda: ed)['fk'] = _c_(379726, _a_(379722, _n_(379721, "base64", lambda: base64), "b64encode"), _c_(379725, _n_(379723, "bytes", lambda: bytes), _n_(379724, "fk", lambda: fk), 'utf-8'))
    _l_(379727)
    for key, value in _c_(379730, _a_(379729, _n_(379728, "dict", lambda: dict), "items")):
        _l_(379745)

        ekey = _c_(379734, _n_(379731, "encrypt_string", lambda: encrypt_string), _n_(379732, "key", lambda: key), _n_(379733, "f", lambda: f))
        _l_(379735)
        evalue = _c_(379739, _n_(379736, "encrypt_string", lambda: encrypt_string), _n_(379737, "value", lambda: value), _n_(379738, "f", lambda: f))
        _l_(379740)
        _n_(379741, "ed", lambda: ed)[_n_(379742, "ekey", lambda: ekey)[::-1]] = _n_(379743, "evalue", lambda: evalue)[::-1]
        _l_(379744)
    aux = _n_(379746, "ed", lambda: ed)
    _l_(379747)
    return aux

def save_game(slot, savename):
    _l_(379782)

    _c_(379750, _n_(379749, "print", lambda: print), "Saving file...")
    _l_(379751)
    path = _c_(379754, _a_(379752, 'saves/savegame{0}.json', "format"), _n_(379753, "slot", lambda: slot))
    _l_(379755)
    data = {
        'game': 'Game name here',
        'version': 'Version here',
        'author': 'Author here',
        'savename': _c_(379758, _n_(379756, "str", lambda: str), _n_(379757, "savename", lambda: savename)),
    }
    _l_(379759)
    data = _c_(379762, _n_(379760, "encrypt_dict", lambda: encrypt_dict), _n_(379761, "data", lambda: data))
    _l_(379763)
    with _c_(379766, _n_(379764, "open", lambda: open), _n_(379765, "path", lambda: path), 'w') as f:
        _l_(379777)

        _c_(379771, _a_(379768, _n_(379767, "json", lambda: json), "dump"), _n_(379769, "data", lambda: data), _n_(379770, "f", lambda: f))
        _l_(379772)
        _c_(379775, _a_(379774, _n_(379773, "f", lambda: f), "close"))
        _l_(379776)
    _c_(379780, _n_(379778, "print", lambda: print), 'Data saved in', _n_(379779, "path", lambda: path))
    _l_(379781)
try:
    import gamemodule as gm
    _l_(379784)

except ImportError:
    pass

def main():
    _l_(379795)

    _c_(379786, _n_(379785, "print", lambda: print), "Running...")
    _l_(379787)
    _c_(379790, _a_(379789, _n_(379788, "gm", lambda: gm), "save_game"), 1, 'test')
    _l_(379791)
    _c_(379793, _n_(379792, "input", lambda: input), "Press any button to continue...")
    _l_(379794)