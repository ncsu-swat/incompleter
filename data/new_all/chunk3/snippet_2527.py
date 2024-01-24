# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73349559/ctx-player-ctx-attributeerror-player-object-has-no-attribute-ctx
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import wavelink
    _l_(546308)

except ImportError:
    pass
try:
    import discord
    _l_(546310)

except ImportError:
    pass
try:
    from discord.ext import commands
    _l_(546312)

except ImportError:
    pass
try:
    import asyncio
    _l_(546314)

except ImportError:
    pass
try:
    import os
    _l_(546316)

except ImportError:
    pass

bot = _c_(546319, _a_(546318, _n_(546317, "commands", lambda: commands), "Bot"), command_prefix='>>')
_l_(546320)


@_a_(546322, _n_(546321, "bot", lambda: bot), "event")
async def on_ready():
    _l_(546333)

    _c_(546324, _n_(546323, "print", lambda: print), 'Bot Online')
    _l_(546325)
    _c_(546331, _a_(546328, _a_(546327, _n_(546326, "bot", lambda: bot), "loop"), "create_task"), _c_(546330, _n_(546329, "node_connect", lambda: node_connect)))
    _l_(546332)


@_a_(546335, _n_(546334, "bot", lambda: bot), "event")
async def on_wavelink_node_ready(node: _a_(546337, _n_(546336, "wavelink", lambda: wavelink), "Node")):
    _l_(546343)

    _c_(546341, _n_(546338, "print", lambda: print), f'Node <{_a_(546340, _n_(546339, "node", lambda: node), "identifier")}> is ready')
    _l_(546342)


async def node_connect():
    _l_(546354)

    await _c_(546346, _a_(546345, _n_(546344, 'bot', lambda: bot), 'wait_until_ready'))
    _l_(546347)
    await _c_(546352, _a_(546350, _a_(546349, _n_(546348, 'wavelink', lambda: wavelink), 'NodePool'), 'create_node'), bot=_n_(546351, 'bot', lambda: bot), host='ash-01.thermalhosting.com', port=2008, password='ASH-01')
    _l_(546353)


@_a_(546356, _n_(546355, 'bot', lambda: bot), 'event')
async def on_wavelink_track_end(player: _a_(546358, _n_(546357, 'wavelink', lambda: wavelink), 'Player'), track: _a_(546360, _n_(546359, 'wavelink', lambda: wavelink), 'Track'), reason):
    _l_(546404)

    ctx = _a_(546362, _n_(546361, 'player', lambda: player), 'ctx')
    _l_(546363)
    vc: _n_(546364, 'player', lambda: player) = _n_(546365, 'ctx', lambda: ctx).voice_client
    _l_(546366)
    if _a_(546368, _n_(546367, 'vc', lambda: vc), 'loop'):
        _l_(546374)

        aux = await _c_(546372, _a_(546370, _n_(546369, 'vc', lambda: vc), 'play'), _n_(546371, 'track', lambda: track))
        _l_(546373)
        return aux
    try:
        _l_(546403)

        next_song = _c_(546378, _a_(546377, _a_(546376, _n_(546375, 'vc', lambda: vc), 'queue'), 'get'))
        _l_(546379)
        await _c_(546383, _a_(546381, _n_(546380, 'vc', lambda: vc), 'play'), _n_(546382, 'next_song', lambda: next_song))
        _l_(546384)
        embed = _c_(546391, _a_(546386, _n_(546385, 'discord', lambda: discord), 'Embed'), title="Now playing", description=f'Song name: **{_a_(546388, _n_(546387, "next_song", lambda: next_song), "title")}**\nSong author: **{_a_(546390, _n_(546389, "next_song", lambda: next_song), "author")}**')
        _l_(546392)
        await _c_(546396, _a_(546394, _n_(546393, 'ctx', lambda: ctx), 'send'), embed=_n_(546395, 'embed', lambda: embed))
        _l_(546397)
    except:
        _l_(546402)

        # An exception when after the track end, the queue is now empty. If you dont do this, it will get error.
        await _c_(546400, _a_(546399, _n_(546398, 'vc', lambda: vc), 'stop'))
        _l_(546401)
@_c_(546407, _a_(546406, _n_(546405, 'bot', lambda: bot), 'command'))
async def play(ctx: _a_(546409, _n_(546408, 'commands', lambda: commands), 'Context'), *, search: _a_(546411, _n_(546410, 'wavelink', lambda: wavelink), 'YouTubeTrack')):
    _l_(546495)

    if not _a_(546413, _n_(546412, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546439)

        vc: _a_(546415, _n_(546414, 'wavelink', lambda: wavelink), 'Player') = await _c_(546423, _a_(546420, _a_(546419, _a_(546418, _a_(546417, _n_(546416, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel'), 'connect'), cls=_a_(546422, _n_(546421, 'wavelink', lambda: wavelink), 'Player'))
        _l_(546424)
    elif not _c_(546429, _n_(546425, 'getattr', lambda: getattr), _a_(546428, _a_(546427, _n_(546426, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546438)

        await _c_(546432, _a_(546431, _n_(546430, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546433)
    else:
        vc: _a_(546435, _n_(546434, 'wavelink', lambda: wavelink), 'Player') = _n_(546436, 'ctx', lambda: ctx).voice_client
        _l_(546437)
    song_name = _a_(546441, _n_(546440, 'search', lambda: search), 'title')
    _l_(546442)
    song_author = _a_(546444, _n_(546443, 'search', lambda: search), 'author')
    _l_(546445)
    if _n_(546446, 'song_author', lambda: song_author) == None:
        _l_(546448)

        song_author = 'Unknown'
        _l_(546447)
    # embed = discord.Embed(title="Added to queue", description=f'Song name: **{song_name}**\nSong author: **{song_author}**')
    # await vc.play(search)
    # await ctx.send(embed=embed)
    if _a_(546451, _a_(546450, _n_(546449, 'vc', lambda: vc), 'queue'), 'is_empty') and _a_(546453, _n_(546452, 'vc', lambda: vc), 'is_playing'):
        _l_(546487)

        await _c_(546457, _a_(546455, _n_(546454, 'vc', lambda: vc), 'play'), _n_(546456, 'search', lambda: search))
        _l_(546458)
        embed = _c_(546463, _a_(546460, _n_(546459, 'discord', lambda: discord), 'Embed'), title="Playing", description=f'Song name: **{_n_(546461, "song_name", lambda: song_name)}**\nSong author: **{_n_(546462, "song_author", lambda: song_author)}**')
        _l_(546464)
        aux = await _c_(546468, _a_(546466, _n_(546465, 'ctx', lambda: ctx), 'send'), embed=_n_(546467, 'embed', lambda: embed))
        _l_(546469)
        return aux
    else:
        await _c_(546474, _a_(546472, _a_(546471, _n_(546470, 'vc', lambda: vc), 'queue'), 'put_wait'), _n_(546473, 'search', lambda: search))
        _l_(546475)
        embed = _c_(546480, _a_(546477, _n_(546476, 'discord', lambda: discord), 'Embed'), title="Added to queue", description=f'Song name: **{_n_(546478, "song_name", lambda: song_name)}**\nSong author: **{_n_(546479, "song_author", lambda: song_author)}**')
        _l_(546481)
        aux = await _c_(546485, _a_(546483, _n_(546482, 'ctx', lambda: ctx), 'send'), embed=_n_(546484, 'embed', lambda: embed))
        _l_(546486)
        return aux
    _n_(546488, 'vc', lambda: vc).ctx = _n_(546489, 'ctx', lambda: ctx)
    _l_(546490)
    _c_(546493, _n_(546491, 'setattr', lambda: setattr), _n_(546492, 'vc', lambda: vc), "loop", False)
    _l_(546494)
@_c_(546498, _a_(546497, _n_(546496, 'bot', lambda: bot), 'command'))
async def pause(ctx: _a_(546500, _n_(546499, 'commands', lambda: commands), 'Context')):
    _l_(546530)

    if not _a_(546502, _n_(546501, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546521)

        aux = await _c_(546505, _a_(546504, _n_(546503, 'ctx', lambda: ctx), 'send'), 'Im not playing any music!')
        _l_(546506)
        return aux
    elif not _c_(546511, _n_(546507, 'getattr', lambda: getattr), _a_(546510, _a_(546509, _n_(546508, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546520)

        await _c_(546514, _a_(546513, _n_(546512, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546515)
    else:
        vc: _a_(546517, _n_(546516, 'wavelink', lambda: wavelink), 'Player') = _n_(546518, 'ctx', lambda: ctx).voice_client
        _l_(546519)
    await _c_(546524, _a_(546523, _n_(546522, 'vc', lambda: vc), 'pause'))
    _l_(546525)
    await _c_(546528, _a_(546527, _n_(546526, 'ctx', lambda: ctx), 'send'), f'Paused!')
    _l_(546529)

@_c_(546533, _a_(546532, _n_(546531, 'bot', lambda: bot), 'command'))
async def resume(ctx: _a_(546535, _n_(546534, 'commands', lambda: commands), 'Context')):
    _l_(546565)

    if not _a_(546537, _n_(546536, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546556)

        aux = await _c_(546540, _a_(546539, _n_(546538, 'ctx', lambda: ctx), 'send'), 'Im not playing any music!')
        _l_(546541)
        return aux
    elif not _c_(546546, _n_(546542, 'getattr', lambda: getattr), _a_(546545, _a_(546544, _n_(546543, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546555)

        await _c_(546549, _a_(546548, _n_(546547, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546550)
    else:
        vc: _a_(546552, _n_(546551, 'wavelink', lambda: wavelink), 'Player') = _n_(546553, 'ctx', lambda: ctx).voice_client
        _l_(546554)
    await _c_(546559, _a_(546558, _n_(546557, 'vc', lambda: vc), 'resume'))
    _l_(546560)
    await _c_(546563, _a_(546562, _n_(546561, 'ctx', lambda: ctx), 'send'), f'Resumed!')
    _l_(546564)

@_c_(546568, _a_(546567, _n_(546566, 'bot', lambda: bot), 'command'))
async def stop(ctx: _a_(546570, _n_(546569, 'commands', lambda: commands), 'Context')):
    _l_(546600)

    if not _a_(546572, _n_(546571, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546591)

        aux = await _c_(546575, _a_(546574, _n_(546573, 'ctx', lambda: ctx), 'send'), 'Im not playing any music!')
        _l_(546576)
        return aux
    elif not _c_(546581, _n_(546577, 'getattr', lambda: getattr), _a_(546580, _a_(546579, _n_(546578, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546590)

        await _c_(546584, _a_(546583, _n_(546582, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546585)
    else:
        vc: _a_(546587, _n_(546586, 'wavelink', lambda: wavelink), 'Player') = _n_(546588, 'ctx', lambda: ctx).voice_client
        _l_(546589)
    await _c_(546594, _a_(546593, _n_(546592, 'vc', lambda: vc), 'stop'))
    _l_(546595)
    await _c_(546598, _a_(546597, _n_(546596, 'ctx', lambda: ctx), 'send'), f'Stopped!')
    _l_(546599)

@_c_(546603, _a_(546602, _n_(546601, 'bot', lambda: bot), 'command'))
async def disconnect(ctx: _a_(546605, _n_(546604, 'commands', lambda: commands), 'Context')):
    _l_(546635)

    if not _a_(546607, _n_(546606, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546626)

        aux = await _c_(546610, _a_(546609, _n_(546608, 'ctx', lambda: ctx), 'send'), 'Im not playing any music!')
        _l_(546611)
        return aux
    elif not _c_(546616, _n_(546612, 'getattr', lambda: getattr), _a_(546615, _a_(546614, _n_(546613, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546625)

        await _c_(546619, _a_(546618, _n_(546617, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546620)
    else:
        vc: _a_(546622, _n_(546621, 'wavelink', lambda: wavelink), 'Player') = _n_(546623, 'ctx', lambda: ctx).voice_client
        _l_(546624)
    await _c_(546629, _a_(546628, _n_(546627, 'vc', lambda: vc), 'disconnect'))
    _l_(546630)
    await _c_(546633, _a_(546632, _n_(546631, 'ctx', lambda: ctx), 'send'), 'Bye!')
    _l_(546634)

@_c_(546638, _a_(546637, _n_(546636, 'bot', lambda: bot), 'command'))
async def loop(ctx: _a_(546640, _n_(546639, 'commands', lambda: commands), 'Context')):
    _l_(546684)

    if not _a_(546642, _n_(546641, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546661)

        aux = await _c_(546645, _a_(546644, _n_(546643, 'ctx', lambda: ctx), 'send'), 'Im not playing any music!')
        _l_(546646)
        return aux
    elif not _c_(546651, _n_(546647, 'getattr', lambda: getattr), _a_(546650, _a_(546649, _n_(546648, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546660)

        await _c_(546654, _a_(546653, _n_(546652, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546655)
    else:
        vc: _a_(546657, _n_(546656, 'wavelink', lambda: wavelink), 'Player') = _n_(546658, 'ctx', lambda: ctx).voice_client
        _l_(546659)
    try:
        _l_(546670)

        _n_(546662, 'vc', lambda: vc).loop = True
        _l_(546663)
    except _n_(546664, 'Exception', lambda: Exception):
        _l_(546669)

        _c_(546667, _n_(546665, 'setattr', lambda: setattr), _n_(546666, 'vc', lambda: vc), "loop", False)
        _l_(546668)
    if _a_(546672, _n_(546671, 'vc', lambda: vc), 'loop'):
        _l_(546683)

        aux = await _c_(546675, _a_(546674, _n_(546673, 'ctx', lambda: ctx), 'send'), 'Loop is now enabled!')
        _l_(546676)
        return aux
    else:
        _n_(546677, 'vc', lambda: vc).loop = False
        _l_(546678)
        aux = await _c_(546681, _a_(546680, _n_(546679, 'ctx', lambda: ctx), 'send'), 'Loop is now disabled')
        _l_(546682)
        return aux

@_c_(546687, _a_(546686, _n_(546685, 'bot', lambda: bot), 'command'))
async def queue(ctx: _a_(546689, _n_(546688, 'commands', lambda: commands), 'Context')):
    _l_(546744)

    if not _a_(546691, _n_(546690, 'ctx', lambda: ctx), 'voice_client'):
        _l_(546710)

        aux = await _c_(546694, _a_(546693, _n_(546692, 'ctx', lambda: ctx), 'send'), 'Im not playing any music!')
        _l_(546695)
        return aux
    elif not _c_(546700, _n_(546696, 'getattr', lambda: getattr), _a_(546699, _a_(546698, _n_(546697, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel', None):
        _l_(546709)

        await _c_(546703, _a_(546702, _n_(546701, 'ctx', lambda: ctx), 'send'), f'Connect to a voice channel to use this command!')
        _l_(546704)
    else:
        vc: _a_(546706, _n_(546705, 'wavelink', lambda: wavelink), 'Player') = _n_(546707, 'ctx', lambda: ctx).voice_client
        _l_(546708)

    if _a_(546713, _a_(546712, _n_(546711, 'vc', lambda: vc), 'queue'), 'is_empty'):
        _l_(546718)

        aux = await _c_(546716, _a_(546715, _n_(546714, 'ctx', lambda: ctx), 'send'), 'Queue is empty!')
        _l_(546717)
        return aux
    embed = _c_(546721, _a_(546720, _n_(546719, 'discord', lambda: discord), 'Embed'), title="Queue")
    _l_(546722)
    queue = _c_(546726, _a_(546725, _a_(546724, _n_(546723, 'vc', lambda: vc), 'queue'), 'copy'))
    _l_(546727)
    song_count = 0
    _l_(546728)
    for song in _n_(546729, 'queue', lambda: queue):
        _l_(546738)

        song_count += 1
        _l_(546730)
        _c_(546736, _a_(546732, _n_(546731, 'embed', lambda: embed), 'add_field'), name=f"Song number {_n_(546733, 'song_count', lambda: song_count)}", value=f"{_a_(546735, _n_(546734, 'song', lambda: song), 'title')}")
        _l_(546737)
    aux = await _c_(546742, _a_(546740, _n_(546739, "ctx", lambda: ctx), "send"), embed=_n_(546741, "embed", lambda: embed))
    _l_(546743)

    return aux
_c_(546747, _a_(546746, _n_(546745, "bot", lambda: bot), "run"), 'secret')
_l_(546748)