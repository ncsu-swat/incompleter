# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77442220/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(546751, _a_(546750, _n_(546749, "bot", lambda: bot), "command"), pass_context = True)
@_c_(546754, _a_(546753, _n_(546752, "commands", lambda: commands), "has_permissions"), administrator=True)
async def limpar(ctx, ammount):
    _l_(546769)

    await _c_(546758, _a_(546756, _n_(546755, "ctx", lambda: ctx), "send"), f'{_n_(546757, "ammount", lambda: ammount)} are going to be deleted')
    _l_(546759)
    _c_(546761, _n_(546760, 'sleep', lambda: sleep), 2)
    _l_(546762)
    await _c_(546767, _a_(546765, _a_(546764, _n_(546763, 'ctx', lambda: ctx), 'channel'), 'purge'), limit=_n_(546766, 'ammount', lambda: ammount))
    _l_(546768)