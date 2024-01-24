# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66663801/errorhandling-indexerror-and-attribute-error-with-discordpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_a_(586110, _n_(586109, "redditsearch", lambda: redditsearch), "error")
async def redditsearch_error(ctx, inst):
    _l_(586125)

    if _c_(586114, _n_(586111, "isinstance", lambda: isinstance), _n_(586112, "inst", lambda: inst), _n_(586113, "IndexError", lambda: IndexError)):
        _l_(586124)

        await _c_(586117, _a_(586116, _n_(586115, "ctx", lambda: ctx), "send"), f"Exception raised. This probably means I failed to find an image.")
        _l_(586118)
    else:
        await _c_(586122, _a_(586120, _n_(586119, "ctx", lambda: ctx), "send"), f"Exception raised. \n\n{_n_(586121, 'inst', lambda: inst)}")
        _l_(586123)