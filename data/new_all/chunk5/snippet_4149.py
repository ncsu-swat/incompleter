# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62286462/error-command-raised-an-exception-typeerror-nonetype-object-is-not-subscr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(688083, _a_(688082, _n_(688081, "client", lambda: client), "command"))
async def anime(ctx):
    _l_(688116)

    await _c_(688086, _a_(688085, _n_(688084, "ctx", lambda: ctx), "send"), "Récupération d'un anime...")
    _l_(688087)
    anime = 0
    _l_(688088)
    while _n_(688089, "anime", lambda: anime) == 0:
        _l_(688115)

        async with _c_(688092, _a_(688091, _n_(688090, "ctx", lambda: ctx), "typing")):
            _l_(688114)

            try:
                _l_(688113)

                ref = _c_(688094, _n_(688093, "randrange", lambda: randrange), 1, 40500)
                _l_(688095)
                anime = _c_(688098, _n_(688096, "Anime", lambda: Anime), _n_(688097, "ref", lambda: ref))
                _l_(688099)
                await _c_(688103, _a_(688101, _n_(688100, "ctx", lambda: ctx), "send"), _n_(688102, "anime", lambda: anime))
                _l_(688104)
            except _n_(688105, "ValueError", lambda: ValueError) as err:
                _l_(688112)

                if _c_(688108, _n_(688106, "str", lambda: str), _n_(688107, "err", lambda: err)) == 'No such id on MyAnimeList':
                    _l_(688111)

                    pass
                    _l_(688109)
                else:
                    pass
                    _l_(688110)