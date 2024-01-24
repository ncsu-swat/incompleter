# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75279769/discord-ext-commands-errors-commandinvokeerror-command-raised-an-exception-typ
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from discord.ext import commands
    _l_(614172)

except ImportError:
    pass
try:
    import youtube_dl
    _l_(614174)

except ImportError:
    pass
try:
    import music
    _l_(614176)

except ImportError:
    pass

bot = _c_(614183, _a_(614178, _n_(614177, "commands", lambda: commands), "Bot"), command_prefix="?", intents=_c_(614182, _a_(614181, _a_(614180, _n_(614179, "discord", lambda: discord), "Intents"), "all")))
_l_(614184)
_c_(614187, _a_(614186, _n_(614185, "bot", lambda: bot), "remove_command"), 'help')
_l_(614188)

class music(_a_(614190, _n_(614189, "commands", lambda: commands), "Bot")):
    _l_(614511)

    def __init__(self, client):
        _l_(614204)

        _n_(614191, "self", lambda: self).client = _n_(614192, "client", lambda: client)
        _l_(614193)

        # all the music related stuff
        _n_(614194, "self", lambda: self).is_playing = False
        _l_(614195)

        # 2d array containing [song, channel]
        _n_(614196, "self", lambda: self).music_queue = []
        _l_(614197)
        _n_(614198, "self", lambda: self).YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        _l_(614199)
        _n_(614200, "self", lambda: self).FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        _l_(614201)

        _n_(614202, "self", lambda: self).vc = ""
        _l_(614203)

     # searching the item on youtube
    def search_yt(self, item):
        _l_(614222)

        with _c_(614208, _n_(614205, "youtube_dl", lambda: youtube_dl), _a_(614207, _n_(614206, "self", lambda: self), "YDL_OPTIONS")) as ydl:
            _l_(614218)

            try:
                _l_(614217)

                info = _c_(614212, _a_(614210, _n_(614209, "ydl", lambda: ydl), "extract_info"), "ytsearch:%s" %
                                        _n_(614211, "item", lambda: item), download=False)['entries'][0]
                _l_(614213)
            except _n_(614214, "Exception", lambda: Exception):
                _l_(614216)

                aux = False
                _l_(614215)
                return aux
        aux = {'source': _n_(614219, "info", lambda: info)['formats'][0]['url'], 'title': _n_(614220, "info", lambda: info)['title']}
        _l_(614221)

        return aux

    def play_next(self):
        _l_(614254)

        if _c_(614226, _n_(614223, "len", lambda: len), _a_(614225, _n_(614224, "self", lambda: self), "music_queue")) > 0:
            _l_(614253)

            _n_(614227, "self", lambda: self).is_playing = True
            _l_(614228)

            # get the first url
            m_url = _a_(614230, _n_(614229, "self", lambda: self), "music_queue")[0][0]['source']
            _l_(614231)

            # remove the first element as you are currently playing it
            _c_(614235, _a_(614234, _a_(614233, _n_(614232, "self", lambda: self), "music_queue"), "pop"), 0)
            _l_(614236)

            _c_(614249, _a_(614239, _a_(614238, _n_(614237, "self", lambda: self), "vc"), "play"), _c_(614245, _a_(614241, _n_(614240, "discord", lambda: discord), "FFmpegPCMAudio"), _n_(614242, "m_url", lambda: m_url), **_a_(614244, _n_(614243, "self", lambda: self), "FFMPEG_OPTIONS")), after=lambda e: _c_(614248, _a_(614247, _n_(614246, "self", lambda: self), "play_next")))
            _l_(614250)
        else:
            _n_(614251, "self", lambda: self).is_playing = False
            _l_(614252)

    # infinite loop checking
    async def play_music(self):
        _l_(614318)

        if _c_(614258, _n_(614255, "len", lambda: len), _a_(614257, _n_(614256, "self", lambda: self), "music_queue")) > 0:
            _l_(614317)

            _n_(614259, "self", lambda: self).is_playing = True
            _l_(614260)

            m_url = _a_(614262, _n_(614261, "self", lambda: self), "music_queue")[0][0]['source']
            _l_(614263)

            # try to connect to voice channel if you are not already connected

            if _a_(614265, _n_(614264, "self", lambda: self), "vc") == "" or not _c_(614269, _a_(614268, _a_(614267, _n_(614266, "self", lambda: self), "vc"), "is_connected")) or _a_(614271, _n_(614270, "self", lambda: self), "vc") == None:
                _l_(614285)

                _n_(614272, "self", lambda: self).vc = await _c_(614276, _a_(614275, _a_(614274, _n_(614273, "self", lambda: self), "music_queue")[0][1], "connect"))
                _l_(614277)
            else:
                await _c_(614283, _a_(614280, _a_(614279, _n_(614278, "self", lambda: self), "vc"), "move_to"), _a_(614282, _n_(614281, "self", lambda: self), "music_queue")[0][1])
                _l_(614284)

            _c_(614289, _n_(614286, "print", lambda: print), _a_(614288, _n_(614287, "self", lambda: self), "music_queue"))
            _l_(614290)
            # remove the first element as you are currently playing it
            _c_(614294, _a_(614293, _a_(614292, _n_(614291, "self", lambda: self), "music_queue"), "pop"), 0)
            _l_(614295)

            _c_(614308, _a_(614298, _a_(614297, _n_(614296, "self", lambda: self), "vc"), "play"), _c_(614304, _a_(614300, _n_(614299, "discord", lambda: discord), "FFmpegPCMAudio"), _n_(614301, "m_url", lambda: m_url), **_a_(614303, _n_(614302, "self", lambda: self), "FFMPEG_OPTIONS")), after=lambda e: _c_(614307, _a_(614306, _n_(614305, "self", lambda: self), "play_next")))
            _l_(614309)
        else:
            _n_(614310, "self", lambda: self).is_playing = False
            _l_(614311)
            await _c_(614315, _a_(614314, _a_(614313, _n_(614312, "self", lambda: self), "vc"), "disconnect"))
            _l_(614316)

    @_c_(614321, _a_(614320, _n_(614319, "bot", lambda: bot), "command"), name="help", alisases=['ajuda'], help="Comando de ajuda")
    async def help(self, ctx):
        _l_(614353)

        helptxt = ''
        _l_(614322)
        for command in _a_(614325, _a_(614324, _n_(614323, "self", lambda: self), "client"), "commands"):
            _l_(614330)

            helptxt += f'**{_n_(614326, "command", lambda: command)}** - {_a_(614328, _n_(614327, "command", lambda: command), "help")}\n'
            _l_(614329)
        embedhelp = _c_(614338, _a_(614332, _n_(614331, 'discord', lambda: discord), 'Embed'), colour=1646116,  # grey
            title=f'Comandos do {_a_(614336, _a_(614335, _a_(614334, _n_(614333, "self", lambda: self), "client"), "user"), "name")}',
            description=_n_(614337, 'helptxt', lambda: helptxt) + \
            '\n[Crie seu próprio Bot de Música](https://youtu.be/YGx0xNHzjgE)'
        )
        _l_(614339)
        _c_(614346, _a_(614341, _n_(614340, 'embedhelp', lambda: embedhelp), 'set_thumbnail'), url=_a_(614345, _a_(614344, _a_(614343, _n_(614342, 'self', lambda: self), 'client'), 'user'), 'avatar_url'))
        _l_(614347)
        await _c_(614351, _a_(614349, _n_(614348, 'ctx', lambda: ctx), 'send'), embed=_n_(614350, 'embedhelp', lambda: embedhelp))
        _l_(614352)

    @_c_(614356, _a_(614355, _n_(614354, 'bot', lambda: bot), 'command'), name="play", help="Toca uma música do YouTube", aliases=['p', 'tocar'])
    async def p(self, ctx, *args):
        _l_(614422)

        query = _c_(614359, _a_(614357, " ", 'join'), _n_(614358, 'args', lambda: args))
        _l_(614360)

        try:
            _l_(614421)

            voice_channel = _a_(614364, _a_(614363, _a_(614362, _n_(614361, 'ctx', lambda: ctx), 'author'), 'voice'), 'channel')
            _l_(614365)
        except:
            _l_(614376)

            # if voice_channel is None:
            # you need to be connected so that the bot knows where to go
            embedvc = _c_(614368, _a_(614367, _n_(614366, 'discord', lambda: discord), 'Embed'), colour=1646116,  # grey
                description='Para tocar uma música, primeiro se conecte a um canal de voz.'
            )
            _l_(614369)
            await _c_(614373, _a_(614371, _n_(614370, 'ctx', lambda: ctx), 'send'), embed=_n_(614372, 'embedvc', lambda: embedvc))
            _l_(614374)
            aux = ""
            _l_(614375)
            return aux
        else:
            song = _c_(614380, _a_(614378, _n_(614377, 'self', lambda: self), 'search_yt'), _n_(614379, 'query', lambda: query))
            _l_(614381)
            if _c_(614384, _n_(614382, 'type', lambda: type), _n_(614383, 'song', lambda: song)) == _c_(614386, _n_(614385, 'type', lambda: type), True):
                _l_(614420)

                embedvc = _c_(614389, _a_(614388, _n_(614387, 'discord', lambda: discord), 'Embed'), colour=12255232,  # red
                    description='Algo deu errado! Tente mudar ou configurar a playlist/vídeo ou escrever o nome dele novamente!'
                )
                _l_(614390)
                await _c_(614394, _a_(614392, _n_(614391, 'ctx', lambda: ctx), 'send'), embed=_n_(614393, 'embedvc', lambda: embedvc))
                _l_(614395)
            else:
                embedvc = _c_(614399, _a_(614397, _n_(614396, 'discord', lambda: discord), 'Embed'), colour=32768,  # green
                    description=f"Você adicionou a música **{_n_(614398, 'song', lambda: song)['title']}** à fila!\n\n[Crie seu próprio Bot de Música](https://youtu.be/YGx0xNHzjgE)"
                )
                _l_(614400)
                await _c_(614404, _a_(614402, _n_(614401, "ctx", lambda: ctx), "send"), embed=_n_(614403, "embedvc", lambda: embedvc))
                _l_(614405)
                _c_(614411, _a_(614408, _a_(614407, _n_(614406, "self", lambda: self), "music_queue"), "append"), [_n_(614409, "song", lambda: song), _n_(614410, "voice_channel", lambda: voice_channel)])
                _l_(614412)

                if _a_(614414, _n_(614413, "self", lambda: self), "is_playing") == False:
                    _l_(614419)

                    await _c_(614417, _a_(614416, _n_(614415, "self", lambda: self), "play_music"))
                    _l_(614418)

    @_c_(614425, _a_(614424, _n_(614423, "bot", lambda: bot), "command"), name="queue", help="Mostra as atuais músicas da fila.", aliases=['q', 'fila'])
    async def q(self, ctx):
        _l_(614464)

        retval = ""
        _l_(614426)
        for i in _c_(614432, _n_(614427, "range", lambda: range), 0, _c_(614431, _n_(614428, "len", lambda: len), _a_(614430, _n_(614429, "self", lambda: self), "music_queue"))):
            _l_(614438)

            retval += f'**{_n_(614433, "i", lambda: i)+1} - **' + _a_(614435, _n_(614434, 'self', lambda: self), 'music_queue')[_n_(614436, 'i', lambda: i)][0]['title'] + "\n"
            _l_(614437)

        _c_(614441, _n_(614439, 'print', lambda: print), _n_(614440, 'retval', lambda: retval))
        _l_(614442)
        if _n_(614443, 'retval', lambda: retval) != "":
            _l_(614463)

            embedvc = _c_(614447, _a_(614445, _n_(614444, 'discord', lambda: discord), 'Embed'), colour=12255232,
                description=f"{_n_(614446, 'retval', lambda: retval)}"
            )
            _l_(614448)
            await _c_(614452, _a_(614450, _n_(614449, "ctx", lambda: ctx), "send"), embed=_n_(614451, "embedvc", lambda: embedvc))
            _l_(614453)
        else:
            embedvc = _c_(614456, _a_(614455, _n_(614454, "discord", lambda: discord), "Embed"), colour=1646116,
                description='Não existe músicas na fila no momento.'
            )
            _l_(614457)
            await _c_(614461, _a_(614459, _n_(614458, "ctx", lambda: ctx), "send"), embed=_n_(614460, "embedvc", lambda: embedvc))
            _l_(614462)

    @_c_(614467, _a_(614466, _n_(614465, "bot", lambda: bot), "command"), name="skip", help="Pula a atual música que está tocando.", aliases=['pular'])
    async def skip(self, ctx):
        _l_(614491)

        if _a_(614469, _n_(614468, "self", lambda: self), "vc") != "" and _a_(614471, _n_(614470, "self", lambda: self), "vc"):
            _l_(614490)

            _c_(614475, _a_(614474, _a_(614473, _n_(614472, "self", lambda: self), "vc"), "stop"))
            _l_(614476)
            # try to play next in the queue if it exists
            await _c_(614479, _a_(614478, _n_(614477, "self", lambda: self), "play_music"))
            _l_(614480)
            embedvc = _c_(614483, _a_(614482, _n_(614481, "discord", lambda: discord), "Embed"), colour=1646116,  # ggrey
                description=f"Você pulou a música."
            )
            _l_(614484)
            await _c_(614488, _a_(614486, _n_(614485, "ctx", lambda: ctx), "send"), embed=_n_(614487, "embedvc", lambda: embedvc))
            _l_(614489)

    @_a_(614492, skip, "error")  # Erros para kick
    async def skip_error(self, ctx, error):
        _l_(614510)

        if _c_(614497, _n_(614493, "isinstance", lambda: isinstance), _n_(614494, "error", lambda: error), _a_(614496, _n_(614495, "commands", lambda: commands), "MissingPermissions")):
            _l_(614509)

            embedvc = _c_(614500, _a_(614499, _n_(614498, "discord", lambda: discord), "Embed"), colour=12255232,
                description=f"Você precisa da permissão **Gerenciar canais** para pular músicas."
            )
            _l_(614501)
            await _c_(614505, _a_(614503, _n_(614502, "ctx", lambda: ctx), "send"), embed=_n_(614504, "embedvc", lambda: embedvc))
            _l_(614506)
        else:
            raise _n_(614507, "error", lambda: error)
            _l_(614508)


def setup(client):
    _l_(614519)

    _c_(614517, _a_(614513, _n_(614512, "client", lambda: client), "add_cog"), _c_(614516, _n_(614514, "music", lambda: music), _n_(614515, "client", lambda: client)))
    _l_(614518)
_c_(614522, _a_(614521, _n_(614520, "bot", lambda: bot), "run"), 'TOKEN')
_l_(614523)