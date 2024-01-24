# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63250747/python3-discord-selfbot-nameerror-name-tokens-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
loop = _c_(530462, _a_(530461, _n_(530460, "asyncio", lambda: asyncio), "get_event_loop"))
_l_(530463)
def Selfbottokens():
    _l_(530474)

    with _c_(530465, _n_(530464, "open", lambda: open), "tokens.txt", "r") as f:
        _l_(530473)

        tokens = [_c_(530468, _a_(530467, _n_(530466, "token", lambda: token), "strip"), "\n") for token in _c_(530471, _a_(530470, _n_(530469, "f", lambda: f), "readlines"))]
        _l_(530472)
for i in _c_(530479, _n_(530475, "range", lambda: range), _c_(530478, _n_(530476, "len", lambda: len), _n_(530477, "tokens", lambda: tokens))):
    _l_(530494)

    _c_(530483, _a_(530481, _n_(530480, "client", lambda: client), "add_cog"), _n_(530482, "client", lambda: client))
    _l_(530484)
    _c_(530492, _a_(530486, _n_(530485, "loop", lambda: loop), "create_task"), _c_(530491, _a_(530488, _n_(530487, "client", lambda: client), "start"), _n_(530489, "tokens", lambda: tokens)[_n_(530490, "i", lambda: i)], bot=False))
    _l_(530493)