# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62862039/typeerror-descriptor-strftime-for-datetime-date-objects-doesnt-apply-to-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(406227, _a_(406226, _n_(406225, "client", lambda: client), "command"))
async def nitrosince(ctx, member: _a_(406229, _n_(406228, "discord", lambda: discord), "Member"), guild: _a_(406231, _n_(406230, "discord", lambda: discord), "Guild") = None):
  _l_(406273)

  member = _a_(406233, _n_(406232, "ctx", lambda: ctx), "member") if not _n_(406234, "member", lambda: member)  else _n_(406235, "member", lambda: member)
  _l_(406236)
  guild = _a_(406238, _n_(406237, "ctx", lambda: ctx), "guild") if not _n_(406239, "guild", lambda: guild) else _n_(406240, "guild", lambda: guild)
  _l_(406241)

  embed = _c_(406248, _a_(406243, _n_(406242, "discord", lambda: discord), "Embed"), colour=_c_(406247, _a_(406246, _a_(406245, _n_(406244, "discord", lambda: discord), "Colour"), "blue")),
        title="NitroSince Command",
        
    )
  _l_(406249)

  _c_(406259, _a_(406251, _n_(406250, "embed", lambda: embed), "add_field"), name=f"{_n_(406252, 'member', lambda: member)} Has had Nitro Since:", value = _c_(406258, _a_(406255, _a_(406254, _n_(406253, "datetime", lambda: datetime), "date"), "strftime"), _a_(406257, _n_(406256, "member", lambda: member), "premium_since"), '%a, %b %d %Y')

)
  _l_(406260)
  _c_(406266, _a_(406262, _n_(406261, "embed", lambda: embed), "set_footer"), text="I was made by Grenade Visuals#0001", icon_url=_a_(406265, _a_(406264, _n_(406263, "ctx", lambda: ctx), "author"), "avatar_url"))
  _l_(406267)
  await _c_(406271, _a_(406269, _n_(406268, "ctx", lambda: ctx), "send"), embed=_n_(406270, "embed", lambda: embed))
  _l_(406272)