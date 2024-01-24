# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64675521/endswith-method-raises-exception-attributeerror-str-object-has-no-attribu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(413029, _a_(413028, _n_(413027, "commands", lambda: commands), "command"))
async def c(self, ctx, color: _n_(413030, "str", lambda: str), *, name: _n_(413031, "str", lambda: str)):
    _l_(413084)

    name_lower = _c_(413034, _a_(413033, _n_(413032, "name", lambda: name), "lower"))
    _l_(413035)

    if _c_(413038, _a_(413037, _n_(413036, "name_lower", lambda: name_lower), "endswith"), "owner"):
        _l_(413083)

        embed = _c_(413045, _a_(413040, _n_(413039, "discord", lambda: discord), "Embed"), title=":x: Error Creating Faction",
            colour=_c_(413044, _a_(413043, _a_(413042, _n_(413041, "discord", lambda: discord), "Colour"), "purple")),
            description="Make sure your faction name doesn't end with the word **owner**."
        )
        _l_(413046)
        await _c_(413050, _a_(413048, _n_(413047, "ctx", lambda: ctx), "send"), embed=_n_(413049, "embed", lambda: embed))
        _l_(413051)
    else:
        if _c_(413054, _a_(413053, _n_(413052, "name_lower", lambda: name_lower), "endswith"), "faction"):
            _l_(413063)

            role_name = _c_(413057, _a_(413056, _n_(413055, "name_lower", lambda: name_lower), "capitalize"))
            _l_(413058)
        else:
            role_name = f"{_c_(413061, _a_(413060, _n_(413059, 'name_lower', lambda: name_lower), 'capitalize'))} Faction"
            _l_(413062)

        await _c_(413069, _a_(413066, _a_(413065, _n_(413064, "ctx", lambda: ctx), "guild"), "create_role"), name=_n_(413067, "role_name", lambda: role_name), color=_n_(413068, "color", lambda: color))
        _l_(413070)
        await _c_(413076, _a_(413073, _a_(413072, _n_(413071, "ctx", lambda: ctx), "guild"), "create_role"), name=f"{_n_(413074, 'role_name', lambda: role_name)} Owner", color=_n_(413075, "color", lambda: color))
        _l_(413077)

        await _c_(413081, _a_(413080, _a_(413079, _n_(413078, "ctx", lambda: ctx), "message"), "add_reaction"), ":white_check_mark:")
        _l_(413082)