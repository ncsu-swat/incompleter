# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71498995/discord-python-error-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import discord
    _l_(565531)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(565533)

except ImportError:
    pass
try:
    import random
    _l_(565535)

except ImportError:
    pass

intents = _c_(565539, _a_(565538, _a_(565537, _n_(565536, "discord", lambda: discord), "Intents"), "all"))
_l_(565540)
_n_(565541, "discord", lambda: discord).members = True
_l_(565542)
_n_(565543, "intents", lambda: intents).members = True
_l_(565544)
client = _c_(565548, _a_(565546, _n_(565545, "commands", lambda: commands), "Bot"), command_prefix="!", intents=_n_(565547, "intents", lambda: intents))
_l_(565549)

@_c_(565552, _a_(565551, _n_(565550, "client", lambda: client), "command"))
async def highLow(ctx: _a_(565554, _n_(565553, "commands", lambda: commands), "Context")):
    _l_(565631)

    AceCard = [1]
    _l_(565555)
    TwoCard = [2]
    _l_(565556)
    ThreeCard = [3]
    _l_(565557)
    FourCard = [4]
    _l_(565558)
    FiveCard = [5]
    _l_(565559)
    SixCard = [6]
    _l_(565560)
    SevenCard = [7]
    _l_(565561)
    EightCard = [8]
    _l_(565562)
    NineCard = [9]
    _l_(565563)
    TenCard = [10]
    _l_(565564)
    JackCard = [11]
    _l_(565565)
    QueenCard = [12]
    _l_(565566)
    KingCard = [13]
    _l_(565567)
    randomCard = _c_(565583, _a_(565569, _n_(565568, "random", lambda: random), "choice"), {_n_(565570, "AceCard", lambda: AceCard)}, {_n_(565571, "TwoCard", lambda: TwoCard)}, {_n_(565572, "ThreeCard", lambda: ThreeCard)}, {_n_(565573, "FourCard", lambda: FourCard)}, {_n_(565574, "FiveCard", lambda: FiveCard)}, {_n_(565575, "SixCard", lambda: SixCard)}, {_n_(565576, "SevenCard", lambda: SevenCard)}, {_n_(565577, "EightCard", lambda: EightCard)}, {_n_(565578, "NineCard", lambda: NineCard)}, {_n_(565579, "TenCard", lambda: TenCard)}, {_n_(565580, "JackCard", lambda: JackCard)}, {_n_(565581, "QueenCard", lambda: QueenCard)}, {_n_(565582, "KingCard", lambda: KingCard)})
    _l_(565584)
    embed = _c_(565588, _a_(565586, _n_(565585, "discord", lambda: discord), "Embed"), title="Welcome to HighLow", description=f"You have {_n_(565587, 'randomCard', lambda: randomCard)}", colour=0x87CEEB)
    _l_(565589)
    _c_(565592, _a_(565591, _n_(565590, "embed", lambda: embed), "set_author"), name="Anwais#6857")
    _l_(565593)
    _c_(565596, _a_(565595, _n_(565594, "embed", lambda: embed), "add_field"), name="Higher", value="React 1 for higher", inline=False)
    _l_(565597)
    _c_(565600, _a_(565599, _n_(565598, "embed", lambda: embed), "add_field"), name="Lower", value="React 2 for lower", inline=True) 
    _l_(565601) 
    global one
    _l_(565602)
    one = _c_(565605, _a_(565604, _n_(565603, "client", lambda: client), "get_emoji"), 946853495628238878)
    _l_(565606)
    global two
    _l_(565607)
    two = _c_(565610, _a_(565609, _n_(565608, "client", lambda: client), "get_emoji"), 946853495716327504)
    _l_(565611)
    messageBeforeCard1 = await _c_(565616, _a_(565614, _a_(565613, _n_(565612, "ctx", lambda: ctx), "channel"), "send"), embed=_n_(565615, "embed", lambda: embed))
    _l_(565617)
    await _c_(565621, _a_(565619, _n_(565618, "messageBeforeCard1", lambda: messageBeforeCard1), "add_reaction"), _n_(565620, "one", lambda: one))
    _l_(565622)
    await _c_(565626, _a_(565624, _n_(565623, "messageBeforeCard1", lambda: messageBeforeCard1), "add_reaction"), _n_(565625, "two", lambda: two))
    _l_(565627)
    _c_(565629, _n_(565628, "print", lambda: print), "a")
    _l_(565630)
@_a_(565633, _n_(565632, "client", lambda: client), "event")
async def on_reaction_add(reaction, user, ctx: _a_(565635, _n_(565634, "commands", lambda: commands), "Context")):
    _l_(565668)

    one= 1
    _l_(565636)
    HigherLowerId = 0
    _l_(565637)
    oneReaction = 0
    _l_(565638)
    twoReaction = 0
    _l_(565639)
    if _a_(565642, _a_(565641, _n_(565640, "reaction", lambda: reaction), "emoji"), "id") == _n_(565643, "one", lambda: one):
        _l_(565667)

        if _a_(565645, _n_(565644, "user", lambda: user), "id") == _n_(565646, "HigherLowerId", lambda: HigherLowerId) :
            _l_(565660)

            await _c_(565650, _a_(565648, _n_(565647, "ctx", lambda: ctx), "send"), f"You chose {_n_(565649, 'one', lambda: one)}")
            _l_(565651)
        else:
            await _c_(565658, _a_(565655, _a_(565654, _a_(565653, _n_(565652, "reaction", lambda: reaction), "message"), "channel"), "send"), f"This is not your game, {_a_(565657, _n_(565656, 'user', lambda: user), 'mention')}")
            _l_(565659)
    elif _a_(565663, _a_(565662, _n_(565661, "reaction", lambda: reaction), "emoji"), "id") != _n_(565664, "oneReaction", lambda: oneReaction):
        _l_(565666)

        pass 
        _l_(565665) 