# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70644536/how-to-get-around-typeerror-coroutine-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def help_utilities(ctx):
    _l_(340345)

    embed = _c_(340306, _a_(340301, _n_(340300, "discord", lambda: discord), "Embed"), color=_c_(340305, _a_(340304, _a_(340303, _n_(340302, "discord", lambda: discord), "Colour"), "dark_blue"))
    )
    _l_(340307)
    _c_(340310, _a_(340309, _n_(340308, "embed", lambda: embed), "set_author"), name="help utils")
    _l_(340311)
    _c_(340314, _a_(340313, _n_(340312, "embed", lambda: embed), "add_field"), name="Decode", value="Decodes an encrypted message (Base64)")
    _l_(340315)
    _c_(340318, _a_(340317, _n_(340316, "embed", lambda: embed), "add_field"), name="Encode", value="Encodes a message in base64")
    _l_(340319)
    _c_(340322, _a_(340321, _n_(340320, "embed", lambda: embed), "add_field"), name='Embed', value='Speak through the bot, but with fancy text"', inline=False)
    _l_(340323)
    _c_(340326, _a_(340325, _n_(340324, "embed", lambda: embed), "add_field"), name="Add/Subtract/Multiply/Divide", value="Just take two values and do whatever operation with them", inline=False)
    _l_(340327)
    _c_(340330, _a_(340329, _n_(340328, "embed", lambda: embed), "add_field"), name="Reverse", value="Reverses your text :/", inline=False)
    _l_(340331)
    _c_(340334, _a_(340333, _n_(340332, "embed", lambda: embed), "add_field"), name='Say', value='Speak through the bot!', inline=False)
    _l_(340335)
    author = _a_(340338, _a_(340337, _n_(340336, "ctx", lambda: ctx), "message"), "author")
    _l_(340339)
    _c_(340343, _a_(340341, _n_(340340, "author", lambda: author), "send"), embed=_n_(340342, "embed", lambda: embed))
    _l_(340344)

@_c_(340348, _a_(340347, _n_(340346, "client", lambda: client), "command"), pass_context=True)
async def help(ctx, arg=None):
    _l_(340402)

    author = _a_(340351, _a_(340350, _n_(340349, "ctx", lambda: ctx), "message"), "author")
    _l_(340352)

    if _n_(340353, "arg", lambda: arg) is None:
        _l_(340391)

        embed = _c_(340360, _a_(340355, _n_(340354, "discord", lambda: discord), "Embed"), color=_c_(340359, _a_(340358, _a_(340357, _n_(340356, "discord", lambda: discord), "Colour"), "gold"))
        )
        _l_(340361)
        _c_(340364, _a_(340363, _n_(340362, "embed", lambda: embed), "set_author"), name='Help')
        _l_(340365)
        _c_(340368, _a_(340367, _n_(340366, "embed", lambda: embed), "add_field"), name="Invite", value="Sends the invite url of the bot lmao", inline=False)
        _l_(340369)
        _c_(340372, _a_(340371, _n_(340370, "embed", lambda: embed), "add_field"), name="Disclaimer", value="for the commands below you need to call them like this: .mod \n Basically the second word :sleepy:")
        _l_(340373)
        _c_(340376, _a_(340375, _n_(340374, "embed", lambda: embed), "add_field"), name="help mod", value="To see more info on my moderation commands", inline=False)
        _l_(340377)
        _c_(340380, _a_(340379, _n_(340378, "embed", lambda: embed), "add_field"), name="help utils", value="To see more info on my utility commands", inline=False)
        _l_(340381)
        _c_(340384, _a_(340383, _n_(340382, "embed", lambda: embed), "add_field"), name="help fun", value="My more fun commands :eyes:", inline=False)
        _l_(340385)
        await _c_(340389, _a_(340387, _n_(340386, "author", lambda: author), "send"), embed=_n_(340388, "embed", lambda: embed))
        _l_(340390)
    if (_n_(340392, "arg", lambda: arg) == "utils") or (_n_(340393, "arg", lambda: arg) == "Utils"):
        _l_(340401)

        _c_(340395, _n_(340394, "help_utilities", lambda: help_utilities))
        _l_(340396)
   # there are more If statments like this but right now I will only focus on 1
   # So you can get the idea of whats going on
    else:
        await _c_(340399, _a_(340398, _n_(340397, "ctx", lambda: ctx), "send"), "bro thats not a valid argument")
        _l_(340400)