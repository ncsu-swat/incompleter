# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70644536/how-to-get-around-typeerror-coroutine-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def help_utilities(ctx):
    _l_(369102)

    embed = _c_(369063, _a_(369058, _n_(369057, "discord", lambda: discord), "Embed"), color=_c_(369062, _a_(369061, _a_(369060, _n_(369059, "discord", lambda: discord), "Colour"), "dark_blue"))
    )
    _l_(369064)
    _c_(369067, _a_(369066, _n_(369065, "embed", lambda: embed), "set_author"), name="help utils")
    _l_(369068)
    _c_(369071, _a_(369070, _n_(369069, "embed", lambda: embed), "add_field"), name="Decode", value="Decodes an encrypted message (Base64)")
    _l_(369072)
    _c_(369075, _a_(369074, _n_(369073, "embed", lambda: embed), "add_field"), name="Encode", value="Encodes a message in base64")
    _l_(369076)
    _c_(369079, _a_(369078, _n_(369077, "embed", lambda: embed), "add_field"), name='Embed', value='Speak through the bot, but with fancy text"', inline=False)
    _l_(369080)
    _c_(369083, _a_(369082, _n_(369081, "embed", lambda: embed), "add_field"), name="Add/Subtract/Multiply/Divide", value="Just take two values and do whatever operation with them", inline=False)
    _l_(369084)
    _c_(369087, _a_(369086, _n_(369085, "embed", lambda: embed), "add_field"), name="Reverse", value="Reverses your text :/", inline=False)
    _l_(369088)
    _c_(369091, _a_(369090, _n_(369089, "embed", lambda: embed), "add_field"), name='Say', value='Speak through the bot!', inline=False)
    _l_(369092)
    author = _a_(369095, _a_(369094, _n_(369093, "ctx", lambda: ctx), "message"), "author")
    _l_(369096)
    _c_(369100, _a_(369098, _n_(369097, "author", lambda: author), "send"), embed=_n_(369099, "embed", lambda: embed))
    _l_(369101)

@_c_(369105, _a_(369104, _n_(369103, "client", lambda: client), "command"), pass_context=True)
async def help(ctx, arg=None):
    _l_(369159)

    author = _a_(369108, _a_(369107, _n_(369106, "ctx", lambda: ctx), "message"), "author")
    _l_(369109)

    if _n_(369110, "arg", lambda: arg) is None:
        _l_(369148)

        embed = _c_(369117, _a_(369112, _n_(369111, "discord", lambda: discord), "Embed"), color=_c_(369116, _a_(369115, _a_(369114, _n_(369113, "discord", lambda: discord), "Colour"), "gold"))
        )
        _l_(369118)
        _c_(369121, _a_(369120, _n_(369119, "embed", lambda: embed), "set_author"), name='Help')
        _l_(369122)
        _c_(369125, _a_(369124, _n_(369123, "embed", lambda: embed), "add_field"), name="Invite", value="Sends the invite url of the bot lmao", inline=False)
        _l_(369126)
        _c_(369129, _a_(369128, _n_(369127, "embed", lambda: embed), "add_field"), name="Disclaimer", value="for the commands below you need to call them like this: .mod \n Basically the second word :sleepy:")
        _l_(369130)
        _c_(369133, _a_(369132, _n_(369131, "embed", lambda: embed), "add_field"), name="help mod", value="To see more info on my moderation commands", inline=False)
        _l_(369134)
        _c_(369137, _a_(369136, _n_(369135, "embed", lambda: embed), "add_field"), name="help utils", value="To see more info on my utility commands", inline=False)
        _l_(369138)
        _c_(369141, _a_(369140, _n_(369139, "embed", lambda: embed), "add_field"), name="help fun", value="My more fun commands :eyes:", inline=False)
        _l_(369142)
        await _c_(369146, _a_(369144, _n_(369143, "author", lambda: author), "send"), embed=_n_(369145, "embed", lambda: embed))
        _l_(369147)
    if (_n_(369149, "arg", lambda: arg) == "utils") or (_n_(369150, "arg", lambda: arg) == "Utils"):
        _l_(369158)

        _c_(369152, _n_(369151, "help_utilities", lambda: help_utilities))
        _l_(369153)
   # there are more If statments like this but right now I will only focus on 1
   # So you can get the idea of whats going on
    else:
        await _c_(369156, _a_(369155, _n_(369154, "ctx", lambda: ctx), "send"), "bro thats not a valid argument")
        _l_(369157)