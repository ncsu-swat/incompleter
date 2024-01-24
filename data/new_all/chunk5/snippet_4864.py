# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44741865/name-error-help-in-a-loop
    # Main Logic, Direction Buttons

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while True:
    _l_(695110)

    for  event in _c_(695036, _a_(695035, _a_(695034, _n_(695033, "pygame", lambda: pygame), "event"), "get")):
        _l_(695109)

        if _a_(695038, _n_(695037, "event", lambda: event), "type") == _a_(695040, _n_(695039, "pygame", lambda: pygame), "QUIT"):
            _l_(695108)

            _c_(695043, _a_(695042, _n_(695041, "pygame", lambda: pygame), "quit"))
            _l_(695044)
            _c_(695047, _a_(695046, _n_(695045, "sys", lambda: sys), "exit"))
            _l_(695048)
        elif _a_(695050, _n_(695049, "event", lambda: event), "type") == _a_(695052, _n_(695051, "pygame", lambda: pygame), "KEYDOWN"):
            _l_(695107)

            if _a_(695054, _n_(695053, "event", lambda: event), "key") == _a_(695056, _n_(695055, "pygame", lambda: pygame), "K_RIGHT") or _a_(695058, _n_(695057, "event", lambda: event), "key") == _c_(695060, _n_(695059, "ord", lambda: ord), 'r'):
                _l_(695062)

                changeto = 'RIGHT'
                _l_(695061)
            if _a_(695064, _n_(695063, "event", lambda: event), "key") == _a_(695066, _n_(695065, "pygame", lambda: pygame), "K_LEFT") or _a_(695068, _n_(695067, "event", lambda: event), "key") == _c_(695070, _n_(695069, "ord", lambda: ord), 'l'):
                _l_(695072)

                changeto = 'LEFT'
                _l_(695071)
            if _a_(695074, _n_(695073, "event", lambda: event), "key") == _a_(695076, _n_(695075, "pygame", lambda: pygame), "K_UP") or _a_(695078, _n_(695077, "event", lambda: event), "key") == _c_(695080, _n_(695079, "ord", lambda: ord), 'u'):
                _l_(695082)

                changeto = 'UP' 
                _l_(695081) 
            if _a_(695084, _n_(695083, "event", lambda: event), "key") == _a_(695086, _n_(695085, "pygame", lambda: pygame), "K_DOWN") or _a_(695088, _n_(695087, "event", lambda: event), "key") == _c_(695090, _n_(695089, "ord", lambda: ord), 'd'):
                _l_(695092)

                changeto = 'DOWN'
                _l_(695091)
            if _a_(695094, _n_(695093, "event", lambda: event), "key") == _a_(695096, _n_(695095, "pygame", lambda: pygame), "K_ESCAPE"):
                _l_(695106)

                _c_(695104, _a_(695099, _a_(695098, _n_(695097, "pygame", lambda: pygame), "event"), "post"), _c_(695103, _a_(695101, _n_(695100, "pygame", lambda: pygame), "event"), _n_(695102, "QUIT", lambda: QUIT)))
                _l_(695105)