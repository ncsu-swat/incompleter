# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70428799/discord-py-musicbot-gives-nonetype-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(449211, _a_(449210, _n_(449209, "commands", lambda: commands), "command"))
async def join(self,ctx):
    _l_(449238)

    if _a_(449214, _a_(449213, _n_(449212, "ctx", lambda: ctx), "author"), "voice") is None:
        _l_(449219)

        await _c_(449217, _a_(449216, _n_(449215, "ctx", lambda: ctx), "send"), "Du bist in keinem VC!")
        _l_(449218)
    voice_channel = _a_(449223, _a_(449222, _a_(449221, _n_(449220, "ctx", lambda: ctx), "author"), "voice"), "channel")
    _l_(449224)
    if _a_(449226, _n_(449225, "ctx", lambda: ctx), "voice_client") is None:
        _l_(449237)

        await _c_(449229, _a_(449228, _n_(449227, "voice_channel", lambda: voice_channel), "connect"))
        _l_(449230)
    else:
        await _c_(449235, _a_(449233, _a_(449232, _n_(449231, "ctx", lambda: ctx), "voice_client"), "move_to"), _n_(449234, "voice_channel", lambda: voice_channel))
        _l_(449236)
@_c_(449241, _a_(449240, _n_(449239, "commands", lambda: commands), "command"))
async def stop(self,ctx):
    _l_(449247)

    await _c_(449245, _a_(449244, _a_(449243, _n_(449242, "ctx", lambda: ctx), "voice_client"), "disconnect"))
    _l_(449246)

@_c_(449250, _a_(449249, _n_(449248, "commands", lambda: commands), "command"))
async def play(self,ctx,url):
    _l_(449285)

    _c_(449254, _a_(449253, _a_(449252, _n_(449251, "ctx", lambda: ctx), "voice_client"), "stop"))
    _l_(449255)
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    _l_(449256)
    YDL_OPTIONS = {'format':"bestaudio"}
    _l_(449257)
    vc = _a_(449259, _n_(449258, "ctx", lambda: ctx), "voice_client")
    _l_(449260)

    with _c_(449264, _a_(449262, _n_(449261, "youtube_dl", lambda: youtube_dl), "YoutubeDL"), _n_(449263, "YDL_Options", lambda: YDL_Options)) as ydl:
        _l_(449284)

        info = _c_(449268, _a_(449266, _n_(449265, "ydl", lambda: ydl), "extract_info"), _n_(449267, "url", lambda: url), download=False)
        _l_(449269)
        url2 = _n_(449270, "info", lambda: info)['formats'][0]['url']
        _l_(449271)
        source = await _c_(449277, _a_(449274, _a_(449273, _n_(449272, "discord", lambda: discord), "FFmpegOpusAudio"), "from_probe"), _n_(449275, "url2", lambda: url2),
        **_n_(449276, "FFMPEG_OPTIONS", lambda: FFMPEG_OPTIONS))
        _l_(449278)
        _c_(449282, _a_(449280, _n_(449279, "vc", lambda: vc), "play"), _n_(449281, "source", lambda: source))
        _l_(449283)

@_c_(449288, _a_(449287, _n_(449286, "commands", lambda: commands), "command"))
async def pause(self,ctx):
    _l_(449298)

    await _c_(449292, _a_(449291, _a_(449290, _n_(449289, "ctx", lambda: ctx), "voice_client"), "pause"))
    _l_(449293)
    await _c_(449296, _a_(449295, _n_(449294, "ctx", lambda: ctx), "send"), "Pausiert")
    _l_(449297)

@_c_(449301, _a_(449300, _n_(449299, "commands", lambda: commands), "command"))
async def resume(self,ctx):
    _l_(449311)

    await _c_(449305, _a_(449304, _a_(449303, _n_(449302, "ctx", lambda: ctx), "voice_client"), "resume"))
    _l_(449306)
    await _c_(449309, _a_(449308, _n_(449307, "ctx", lambda: ctx), "send"), "wird Weitergespielt...")
    _l_(449310)