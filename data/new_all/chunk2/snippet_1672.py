# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64941040/extension-cogs-reddit-raised-an-error-typeerror-init-missing-1-require
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord, praw, random
    _l_(460574)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(460576)

except ImportError:
    pass

reddit = _c_(460579, _a_(460578, _n_(460577, "praw", lambda: praw), "Reddit"), client_id = '<id>', client_secret = '<secret>', username = '<username>', password = '<password>', user_agent = 'pythonpraw') # this is undoubtedly all correct
_l_(460580) # this is undoubtedly all correct


# There is an underscore in this class identifier because a "Reddit" class already exists within the "praw" package
class _Reddit(_a_(460582, _n_(460581, "commands", lambda: commands), "Cog")):
    _l_(460633)

    def __init__(self, client):
        _l_(460586)

        _n_(460583, "self", lambda: self).client = _n_(460584, "client", lambda: client)
        _l_(460585)


    @_c_(460589, _a_(460588, _n_(460587, "commands", lambda: commands), "command"))
    async def meme(self, ctx):
        _l_(460632)

        subreddit = _c_(460592, _a_(460591, _n_(460590, "reddit", lambda: reddit), "subreddit"), 'memes')
        _l_(460593)
        top = _c_(460596, _a_(460595, _n_(460594, "subreddit", lambda: subreddit), "top"), limit=50)
        _l_(460597)
        all_submissions = []
        _l_(460598)

        for submission in _n_(460599, "top", lambda: top):
            _l_(460605)

            _c_(460603, _a_(460601, _n_(460600, "all_submissions", lambda: all_submissions), "append"), _n_(460602, "submission", lambda: submission))
            _l_(460604)

        random_submission = _c_(460609, _a_(460607, _n_(460606, "random", lambda: random), "choice"), _n_(460608, "all_submissions", lambda: all_submissions))
        _l_(460610)

        submission_name = _a_(460612, _n_(460611, "random_submission", lambda: random_submission), "title")
        _l_(460613)
        submission_url = _a_(460615, _n_(460614, "random_submission", lambda: random_submission), "url")
        _l_(460616)

        embed = _c_(460620, _a_(460618, _n_(460617, "discord", lambda: discord), "Embed"), title=_n_(460619, "submission_name", lambda: submission_name))
        _l_(460621)
        _c_(460625, _a_(460623, _n_(460622, "embed", lambda: embed), "set_image"), url=_n_(460624, "submission_url", lambda: submission_url))
        _l_(460626)

        await _c_(460630, _a_(460628, _n_(460627, "ctx", lambda: ctx), "send"), embed=_n_(460629, "embed", lambda: embed))
        _l_(460631)


def setup(client):
    _l_(460640)

    _c_(460638, _a_(460635, _n_(460634, "client", lambda: client), "add_cog"), _c_(460637, _n_(460636, "_Reddit", lambda: _Reddit)))
    _l_(460639)