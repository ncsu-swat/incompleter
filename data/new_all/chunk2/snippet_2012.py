# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70147604/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(475818, _n_(475817, "client", lambda: client), "event")
async def on_ready():
    _l_(475846)

    _c_(475821, _a_(475820, _n_(475819, "changeStatus", lambda: changeStatus), "start"))
    _l_(475822)
    kvuqqs = _c_(475825, _a_(475824, _n_(475823, "client", lambda: client), "get_channel"), 906998823187017728)
    _l_(475826)
    librar = _c_(475829, _a_(475828, _n_(475827, "client", lambda: client), "get_channel"), 906168716197232660)
    _l_(475830)

    await _c_(475833, _a_(475832, _n_(475831, "kvuqqs", lambda: kvuqqs), "send"), 'Айоу! Бот был включен. \nК сожалению, на данный момент обновлений нет. \n`l.хелп`')
    _l_(475834)
    await _c_(475844, _a_(475836, _n_(475835, "librar", lambda: librar), "send"), embed=_c_(475843, _a_(475838, _n_(475837, "discord", lambda: discord), "Embed"), title='Бот был включен!', description='Версия бота на данный момент: 2.0.1.', color=_c_(475842, _a_(475840, _n_(475839, "random", lambda: random), "choice"), _n_(475841, "colors", lambda: colors))))
    _l_(475845)