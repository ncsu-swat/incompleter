# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66076831/discord-py-music-bot-raising-typeerror-when-a-youtube-link-is-given-in-the-play
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MusicSource(_a_(573859, _n_(573858, "discord", lambda: discord), "PCMVolumeTransformer")):
    _l_(573965)

    _a_(573860, youtube_dl, "utils").bug_reports_message = lambda: ''  # Suppressing Random Youtube_Dl warnings
    _l_(573861)  # Suppressing Random Youtube_Dl warnings
    ytdl_format_options = {  # options for the youtube_dl module, for the audio quality
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',  # We will use Youtube for searching musics
        'source_address': '0.0.0.0',  # IPv6 causes problem sometimes so we are using IPv4
        'youtube_include_dash_manifest': False  # Turning off dash manifest
        # (Enabling it sometimes makes the bot not play anything)
    }
    _l_(573862)
    ytdl = _c_(573864, _a_(573863, youtube_dl, "YoutubeDL"), ytdl_format_options)  # Sending the options to the Youtube_DL class
    _l_(573865)  # Sending the options to the Youtube_DL class

    def __init__(self, source: _a_(573866, discord, "AudioSource"), *, data):
        _l_(573924)

        _n_(573867, "self", lambda: self).volume = 0.4
        _l_(573868)
        _c_(573874, _a_(573870, _n_(573869, "super", lambda: super)(), "__init__"), _n_(573871, "source", lambda: source), _a_(573873, _n_(573872, "self", lambda: self), "volume"))
        _l_(573875)
        _n_(573876, "self", lambda: self).data = _n_(573877, "data", lambda: data)
        _l_(573878)
        _n_(573879, "self", lambda: self).title = _c_(573882, _a_(573881, _n_(573880, "data", lambda: data), "get"), 'title')
        _l_(573883)
        _n_(573884, "self", lambda: self).url = _c_(573887, _a_(573886, _n_(573885, "data", lambda: data), "get"), 'url')
        _l_(573888)
        _n_(573889, "self", lambda: self).link = _c_(573892, _a_(573891, _n_(573890, "data", lambda: data), "get"), 'webpage_url')  # Fetching the youtube link for the song and
        _l_(573893)  # Fetching the youtube link for the song and
        # will be used later for sending it to the user
        _n_(573894, "self", lambda: self).time = _c_(573897, _a_(573896, _n_(573895, "data", lambda: data), "get"), 'duration')
        _l_(573898)
        _n_(573899, "self", lambda: self).img = _c_(573902, _a_(573901, _n_(573900, "data", lambda: data), "get"), 'thumbnail')
        _l_(573903)
        _n_(573904, "self", lambda: self).artist = _c_(573907, _a_(573906, _n_(573905, "data", lambda: data), "get"), 'artist')
        _l_(573908)
        _n_(573909, "self", lambda: self).likes = _c_(573912, _a_(573911, _n_(573910, "data", lambda: data), "get"), 'like_count')
        _l_(573913)
        _n_(573914, "self", lambda: self).dislikes = _c_(573917, _a_(573916, _n_(573915, "data", lambda: data), "get"), 'dislike_count')
        _l_(573918)
        _n_(573919, "self", lambda: self).albm = _c_(573922, _a_(573921, _n_(573920, "data", lambda: data), "get"), 'album')
        _l_(573923)

    @_n_(573925, "classmethod", lambda: classmethod)
    async def from_url(cls, url, *, loop=None, stream=False, timestamp=0):
        _l_(573964)

        # audio from the url
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': f'-vn -ss {_n_(573926, "timestamp", lambda: timestamp)}'
        }
        _l_(573927)
        loop = _n_(573928, 'loop', lambda: loop) or _c_(573931, _a_(573930, _n_(573929, 'asyncio', lambda: asyncio), 'get_event_loop'))
        _l_(573932)
        data = await _c_(573941, _a_(573934, _n_(573933, 'loop', lambda: loop), 'run_in_executor'), None, lambda: _c_(573940, _a_(573937, _a_(573936, _n_(573935, 'cls', lambda: cls), 'ytdl'), 'extract_info'), _n_(573938, 'url', lambda: url), download=not _n_(573939, 'stream', lambda: stream)))
        _l_(573942)
        if 'entries' in _n_(573943, 'data', lambda: data):
            _l_(573963)

            data = _n_(573944, 'data', lambda: data)['entries'][0]  # Taking the first item from the search results
            _l_(573945)  # Taking the first item from the search results
            filename = _n_(573946, 'data', lambda: data)['url'] if _n_(573947, 'stream', lambda: stream) else _c_(573952, _a_(573950, _a_(573949, _n_(573948, 'cls', lambda: cls), 'ytdl'), 'prepare_filename'), _n_(573951, 'data', lambda: data))
            _l_(573953)
            aux = _c_(573961, _n_(573954, 'cls', lambda: cls), _c_(573959, _a_(573956, _n_(573955, 'discord', lambda: discord), 'FFmpegPCMAudio'), _n_(573957, 'filename', lambda: filename), **_n_(573958, 'ffmpeg_options', lambda: ffmpeg_options)), data=_n_(573960, 'data', lambda: data))
            _l_(573962)
            return aux