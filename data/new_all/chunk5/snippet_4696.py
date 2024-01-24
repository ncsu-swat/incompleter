# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52414070/attributeerror-nonetype-object-has-no-attribute-mention
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
client = _c_(665006, _a_(665005, _n_(665004, "discord", lambda: discord), "Client"))
_l_(665007)

async def background_loop():
    _l_(665071)

    await _c_(665010, _a_(665009, _n_(665008, "client", lambda: client), "wait_until_ready"))
    _l_(665011)
    channel = _c_(665014, _a_(665013, _n_(665012, "client", lambda: client), "get_channel"), "479919577279758340")
    _l_(665015)
    while not _a_(665017, _n_(665016, "client", lambda: client), "is_closed"):
        _l_(665070)

        loot = _c_(665020, _a_(665019, _n_(665018, "random", lambda: random), "randint"), 25,50)
        _l_(665021)
        emojigrab = '💰'
        _l_(665022)
        emojimsg = await _c_(665027, _a_(665024, _n_(665023, "client", lambda: client), "send_message"), _n_(665025, "channel", lambda: channel), _n_(665026, "emojigrab", lambda: emojigrab))
        _l_(665028)
        await _c_(665032, _a_(665030, _n_(665029, "client", lambda: client), "add_reaction"), _n_(665031, "emojimsg", lambda: emojimsg), "👍")
        _l_(665033)
        x = await _c_(665040, _a_(665035, _n_(665034, "client", lambda: client), "wait_for_reaction"), emoji="👍", message=_n_(665036, "emojimsg", lambda: emojimsg),
                                             check=lambda reaction, user: _n_(665037, "user", lambda: user) != _a_(665039, _n_(665038, "client", lambda: client), "user"))
        _l_(665041)
        if _n_(665042, "x", lambda: x):
            _l_(665069)

            await _c_(665046, _a_(665044, _n_(665043, "client", lambda: client), "delete_message"), _n_(665045, "emojimsg", lambda: emojimsg))
            _l_(665047)
            await _c_(665057, _a_(665049, _n_(665048, "client", lambda: client), "send_message"), _n_(665050, "channel", lambda: channel), _c_(665056, _a_(665051, "{} secures the bag. {} found inside. ", "format"), _a_(665054, _a_(665053, _n_(665052, "x", lambda: x), "user"), "mention"), _n_(665055, "loot", lambda: loot)))
            _l_(665058)
            _c_(665063, _n_(665059, "add_dollars", lambda: add_dollars), _a_(665061, _n_(665060, "x", lambda: x), "user"), _n_(665062, "loot", lambda: loot))
            _l_(665064)
            await _c_(665067, _a_(665066, _n_(665065, "asyncio", lambda: asyncio), "sleep"), 1800)
            _l_(665068)

try:
    _l_(665083)

    with _c_(665073, _n_(665072, "open", lambda: open), "cash.json") as fp:
        _l_(665079)

        cash = _c_(665077, _a_(665075, _n_(665074, "json", lambda: json), "load"), _n_(665076, "fp", lambda: fp))
        _l_(665078)
except _n_(665080, "Exception", lambda: Exception):
    _l_(665082)

    cash = {}
    _l_(665081)

def save_cash():
    _l_(665093)

    with _c_(665085, _n_(665084, "open", lambda: open), "cash.json", "w+") as fp:
        _l_(665092)

        _c_(665090, _a_(665087, _n_(665086, "json", lambda: json), "dump"), _n_(665088, "cash", lambda: cash), _n_(665089, "fp", lambda: fp), sort_keys=True, indent=4)
        _l_(665091)

def add_dollars(user: _a_(665095, _n_(665094, "discord", lambda: discord), "User"), dollars: _n_(665096, "int", lambda: int)):
    _l_(665126)

    id = _a_(665098, _n_(665097, "user", lambda: user), "id")
    _l_(665099)
    if _n_(665100, "id", lambda: id) not in _n_(665101, "cash", lambda: cash):
        _l_(665105)

        _n_(665102, "cash", lambda: cash)[_n_(665103, "id", lambda: id)] = {}
        _l_(665104)
    _n_(665106, "cash", lambda: cash)[_n_(665107, "id", lambda: id)]["dollars"] = _c_(665111, _a_(665110, _n_(665108, "cash", lambda: cash)[_n_(665109, "id", lambda: id)], "get"), "dollars", 0) + _n_(665112, "dollars", lambda: dollars)
    _l_(665113)
    _c_(665121, _n_(665114, "print", lambda: print), _c_(665120, _a_(665115, "{} now has {} dollars", "format"), _a_(665117, _n_(665116, "user", lambda: user), "name"), _n_(665118, "cash", lambda: cash)[_n_(665119, "id", lambda: id)]["dollars"]))
    _l_(665122)
    _c_(665124, _n_(665123, "save_cash", lambda: save_cash))
    _l_(665125)

def remove_dollars(user: _a_(665128, _n_(665127, "discord", lambda: discord), "User"), dollars: _n_(665129, "int", lambda: int)):
    _l_(665159)

    id = _a_(665131, _n_(665130, "user", lambda: user), "id")
    _l_(665132)
    if _n_(665133, "id", lambda: id) not in _n_(665134, "cash", lambda: cash):
        _l_(665138)

        _n_(665135, "cash", lambda: cash)[_n_(665136, "id", lambda: id)] = {}
        _l_(665137)
    _n_(665139, "cash", lambda: cash)[_n_(665140, "id", lambda: id)]["dollars"] = _c_(665144, _a_(665143, _n_(665141, "cash", lambda: cash)[_n_(665142, "id", lambda: id)], "get"), "dollars", 0) - _n_(665145, "dollars", lambda: dollars)
    _l_(665146)
    _c_(665154, _n_(665147, "print", lambda: print), _c_(665153, _a_(665148, "{} now has {} dollars", "format"), _a_(665150, _n_(665149, "user", lambda: user), "name"), _n_(665151, "cash", lambda: cash)[_n_(665152, "id", lambda: id)]["dollars"]))
    _l_(665155)
    _c_(665157, _n_(665156, "save_cash", lambda: save_cash))
    _l_(665158)

def add_dollars_stolen(user: _a_(665161, _n_(665160, "discord", lambda: discord), "User"), dollars_stolen: _n_(665162, "int", lambda: int)):
    _l_(665192)

    id = _a_(665164, _n_(665163, "user", lambda: user), "id")
    _l_(665165)
    if _n_(665166, "id", lambda: id) not in _n_(665167, "cash", lambda: cash):
        _l_(665171)

        _n_(665168, "cash", lambda: cash)[_n_(665169, "id", lambda: id)] = {}
        _l_(665170)
    _n_(665172, "cash", lambda: cash)[_n_(665173, "id", lambda: id)]["dollars_stolen"] = _c_(665177, _a_(665176, _n_(665174, "cash", lambda: cash)[_n_(665175, "id", lambda: id)], "get"), "dollars_stolen", 0) + _n_(665178, "dollars_stolen", lambda: dollars_stolen)
    _l_(665179)
    _c_(665187, _n_(665180, "print", lambda: print), _c_(665186, _a_(665181, "{} stole ${}", "format"), _a_(665183, _n_(665182, "user", lambda: user), "name"), _n_(665184, "cash", lambda: cash)[_n_(665185, "id", lambda: id)]["dollars_stolen"]))
    _l_(665188)
    _c_(665190, _n_(665189, "save_cash", lambda: save_cash))
    _l_(665191)

def get_dollars_stolen(user: _a_(665194, _n_(665193, "discord", lambda: discord), "User")):
    _l_(665207)

    id = _a_(665196, _n_(665195, "user", lambda: user), "id")
    _l_(665197)
    if _n_(665198, "id", lambda: id) in _n_(665199, "cash", lambda: cash):
        _l_(665205)

        aux = _c_(665203, _a_(665202, _n_(665200, "cash", lambda: cash)[_n_(665201, "id", lambda: id)], "get"), "dollars_stolen", 0)
        _l_(665204)
        return aux
    aux = 0
    _l_(665206)
    return aux

def get_dollars(user: _a_(665209, _n_(665208, "discord", lambda: discord), "User")):
    _l_(665222)

    id = _a_(665211, _n_(665210, "user", lambda: user), "id")
    _l_(665212)
    if _n_(665213, "id", lambda: id) in _n_(665214, "cash", lambda: cash):
        _l_(665220)

        aux = _c_(665218, _a_(665217, _n_(665215, "cash", lambda: cash)[_n_(665216, "id", lambda: id)], "get"), "dollars", 0)
        _l_(665219)
        return aux
    aux = 0
    _l_(665221)
    return aux

@_a_(665224, _n_(665223, "client", lambda: client), "event")
async def on_ready():
    _l_(665228)

    _c_(665226, _n_(665225, "print", lambda: print), 'Bot Online.')
    _l_(665227)

@_a_(665230, _n_(665229, "client", lambda: client), "event")
async def on_message(message):
    _l_(665278)

    if _a_(665232, _n_(665231, "message", lambda: message), "author") == _a_(665234, _n_(665233, "client", lambda: client), "user"):
        _l_(665236)

        aux = ""
        _l_(665235)
        return aux

    if _c_(665242, _a_(665241, _c_(665240, _a_(665239, _a_(665238, _n_(665237, "message", lambda: message), "content"), "lower")), "startswith"), "?cash"):
        _l_(665277)

        if _c_(665246, _a_(665245, _a_(665244, _n_(665243, "message", lambda: message), "content"), "lower")) == "?cash":
            _l_(665276)

            if _c_(665250, _n_(665247, "get_dollars", lambda: get_dollars), _a_(665249, _n_(665248, "message", lambda: message), "author")) < 0:
                _l_(665275)

                await _c_(665261, _a_(665252, _n_(665251, "client", lambda: client), "send_message"), _a_(665254, _n_(665253, "message", lambda: message), "channel"), _c_(665260, _a_(665255, "You're ${} in the hole!", "format"), _c_(665259, _n_(665256, "get_dollars", lambda: get_dollars), _a_(665258, _n_(665257, "message", lambda: message), "author"))))
                _l_(665262)
            else:
                await _c_(665273, _a_(665264, _n_(665263, "client", lambda: client), "send_message"), _a_(665266, _n_(665265, "message", lambda: message), "channel"), _c_(665272, _a_(665267, "You've acquired ${}! :dollar:", "format"), _c_(665271, _n_(665268, "get_dollars", lambda: get_dollars), _a_(665270, _n_(665269, "message", lambda: message), "author"))))
                _l_(665274)


_c_(665284, _a_(665281, _a_(665280, _n_(665279, "client", lambda: client), "loop"), "create_task"), _c_(665283, _n_(665282, "background_loop", lambda: background_loop)))
_l_(665285)