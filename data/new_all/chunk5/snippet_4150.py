# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62286462/error-command-raised-an-exception-typeerror-nonetype-object-is-not-subscr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(648687, _a_(648686, _n_(648685, "client", lambda: client), "command"))
async def anime(ctx):
    _l_(648720)

    await _c_(648690, _a_(648689, _n_(648688, "ctx", lambda: ctx), "send"), "Récupération d'un anime...")
    _l_(648691)
    anime = 0
    _l_(648692)
    while _n_(648693, "anime", lambda: anime) == 0:
        _l_(648719)

        async with _c_(648696, _a_(648695, _n_(648694, "ctx", lambda: ctx), "typing")):
            _l_(648718)

            try:
                _l_(648717)

                ref = _c_(648698, _n_(648697, "randrange", lambda: randrange), 1, 40500)
                _l_(648699)
                anime = _c_(648702, _n_(648700, "Anime", lambda: Anime), _n_(648701, "ref", lambda: ref))
                _l_(648703)
                await _c_(648707, _a_(648705, _n_(648704, "ctx", lambda: ctx), "send"), _n_(648706, "anime", lambda: anime))
                _l_(648708)
            except _n_(648709, "ValueError", lambda: ValueError) as err:
                _l_(648716)

                if _c_(648712, _n_(648710, "str", lambda: str), _n_(648711, "err", lambda: err)) == 'No such id on MyAnimeList':
                    _l_(648715)

                    pass
                    _l_(648713)
                else:
                    pass
                    _l_(648714)