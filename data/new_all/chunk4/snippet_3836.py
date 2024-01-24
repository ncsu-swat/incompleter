# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66663801/errorhandling-indexerror-and-attribute-error-with-discordpy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(591020, _a_(591019, _n_(591018, "bot", lambda: bot), "command"))
async def redditsearch(ctx, sub):
    _l_(591111)

    start_time = _c_(591023, _a_(591022, _n_(591021, "time", lambda: time), "time"))
    _l_(591024)
    listing = []
    _l_(591025)
    subreddit = await _c_(591029, _a_(591027, _n_(591026, "reddit", lambda: reddit), "subreddit"), _n_(591028, "sub", lambda: sub))
    _l_(591030)
    _c_(591034, _n_(591031, "print", lambda: print), _a_(591033, _n_(591032, "subreddit", lambda: subreddit), "subreddit_type"))
    _l_(591035)
    if _c_(591038, _a_(591037, _n_(591036, "sub", lambda: sub), "lower")) in _n_(591039, "bannedsubs", lambda: bannedsubs):
        _l_(591110)

        await _c_(591042, _a_(591041, _n_(591040, "ctx", lambda: ctx), "send"), "Banned subreddit.")
        _l_(591043)
        aux = ""
        _l_(591044)
        return aux
    elif _a_(591046, _n_(591045, "subreddit", lambda: subreddit), "over18") == True:
        _l_(591109)

        await _c_(591049, _a_(591048, _n_(591047, "ctx", lambda: ctx), "send"), "No NSFW subreddits.")
        _l_(591050)
        aux = ""
        _l_(591051)
        return aux
    else:
        async for submission in _c_(591054, _a_(591053, _n_(591052, "subreddit", lambda: subreddit), "hot"), limit=100):
            _l_(591070)

            if _c_(591058, _a_(591057, _a_(591056, _n_(591055, "submission", lambda: submission), "url"), "endswith"), ("jpg", "jpeg", "png", "gifv")) and not _a_(591060, _n_(591059, "submission", lambda: submission), "spoiler") and not _a_(591062, _n_(591061, "submission", lambda: submission), "over_18"):
                _l_(591069)

                _c_(591066, _a_(591064, _n_(591063, "listing", lambda: listing), "append"), _n_(591065, "submission", lambda: submission))
                _l_(591067)
            else:
                pass
                _l_(591068)
    
        _c_(591074, _a_(591072, _n_(591071, "random", lambda: random), "shuffle"), _n_(591073, "listing", lambda: listing))
        _l_(591075)
        post = _n_(591076, "listing", lambda: listing)[0]
        _l_(591077)
        if _a_(591079, _n_(591078, "submission", lambda: submission), "link_flair_text") == None:
            _l_(591098)

            await _c_(591086, _a_(591081, _n_(591080, "ctx", lambda: ctx), "send"), f"{_a_(591083, _n_(591082, 'post', lambda: post), 'title')}\n{_a_(591085, _n_(591084, 'post', lambda: post), 'url')}")
            _l_(591087)
        else:
            await _c_(591096, _a_(591089, _n_(591088, "ctx", lambda: ctx), "send"), f"[{_a_(591091, _n_(591090, 'submission', lambda: submission), 'link_flair_text')}] \n{_a_(591093, _n_(591092, 'post', lambda: post), 'title')}\n{_a_(591095, _n_(591094, 'post', lambda: post), 'url')}")
            _l_(591097)
        end_time = _c_(591101, _a_(591100, _n_(591099, "time", lambda: time), "time"))
        _l_(591102)
        await _c_(591107, _a_(591104, _n_(591103, "ctx", lambda: ctx), "send"), f"---- Took %s seconds to lookup ----" % (_n_(591105, "end_time", lambda: end_time) - _n_(591106, "start_time", lambda: start_time)))
        _l_(591108)