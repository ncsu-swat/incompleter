# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73551025/discord-py-self-aftererror-typeerror-lambda-takes-0-positional-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
players = {}
_l_(632959)
queues = {}
_l_(632960)

class music(_a_(632962, _n_(632961, "commands", lambda: commands), "Cog")):
  _l_(633089)

  def __init__(self, client):
    _l_(632966)

    _n_(632963, "self", lambda: self).client = _n_(632964, "client", lambda: client)
    _l_(632965)

  def queueCheck(self, id, vc):
    _l_(632984)

    if _n_(632967, "queues", lambda: queues)[_n_(632968, "id", lambda: id)] != []:
      _l_(632983)

      stream = _c_(632972, _a_(632971, _n_(632969, "queues", lambda: queues)[_n_(632970, "id", lambda: id)], "pop"), 0, None)
      _l_(632973)
      _n_(632974, "players", lambda: players)[_n_(632975, "id", lambda: id)] = _n_(632976, "stream", lambda: stream)
      _l_(632977)
      _c_(632981, _a_(632979, _n_(632978, "vc", lambda: vc), "play"), _n_(632980, "stream", lambda: stream))
      _l_(632982)

  

  async def playSong(self, ctx, url):
    _l_(633014)

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    _l_(632985)
    YDL_OPTIONS = {'format':"bestaudio",
                    'default_search':'auto'}
    _l_(632986)
    
    with _c_(632990, _a_(632988, _n_(632987, "youtube_dl", lambda: youtube_dl), "YoutubeDL"), _n_(632989, "YDL_OPTIONS", lambda: YDL_OPTIONS)) as ydl:
      _l_(633011)

      info = _c_(632994, _a_(632992, _n_(632991, "ydl", lambda: ydl), "extract_info"), _n_(632993, "url", lambda: url), download=False)
      _l_(632995)
      if 'entries' in _n_(632996, "info", lambda: info):
        _l_(633003)

        url2 = _n_(632997, "info", lambda: info)['entries'][0]['formats'][0]['url']
        _l_(632998)
      elif 'formats' in _n_(632999, "info", lambda: info):
        _l_(633002)

        url2 = _n_(633000, "info", lambda: info)['formats'][0]['url']
        _l_(633001)
      stream = await _c_(633009, _a_(633006, _a_(633005, _n_(633004, "discord", lambda: discord), "FFmpegOpusAudio"), "from_probe"), _n_(633007, "url2", lambda: url2), **_n_(633008, "FFMPEG_OPTIONS", lambda: FFMPEG_OPTIONS))
      _l_(633010)
    aux = _n_(633012, "stream", lambda: stream)
    _l_(633013)

    return aux
  
  @_c_(633016, _a_(633015, commands, "command"))
  async def play(self, ctx, *, url):
    _l_(633055)

    if _a_(633018, _n_(633017, "ctx", lambda: ctx), "voice_client") is None:
      _l_(633026)

      await _c_(633024, _a_(633023, _a_(633022, _a_(633021, _a_(633020, _n_(633019, "ctx", lambda: ctx), "author"), "voice"), "channel"), "connect"))
      _l_(633025)

    stream = await _c_(633031, _a_(633028, _n_(633027, "self", lambda: self), "playSong"), _n_(633029, "ctx", lambda: ctx), _n_(633030, "url", lambda: url))
    _l_(633032)
    guild = _a_(633035, _a_(633034, _n_(633033, "ctx", lambda: ctx), "message"), "guild")
    _l_(633036)
    vc = _a_(633038, _n_(633037, "ctx", lambda: ctx), "voice_client")
    _l_(633039)
    _n_(633040, "players", lambda: players)[_a_(633042, _n_(633041, "guild", lambda: guild), "id")] = _n_(633043, "stream", lambda: stream)
    _l_(633044)
    _c_(633053, _a_(633046, _n_(633045, "vc", lambda: vc), "play"), _n_(633047, "stream", lambda: stream), after=lambda: _c_(633052, _a_(633049, _n_(633048, "self", lambda: self), "queueCheck"), _n_(633050, "guild", lambda: guild), _n_(633051, "vc", lambda: vc)))
    _l_(633054)

  @_c_(633057, _a_(633056, commands, "command"))
  async def queue(self, ctx, url):
    _l_(633088)

    guild = _a_(633060, _a_(633059, _n_(633058, "ctx", lambda: ctx), "message"), "guild")
    _l_(633061)
    stream = await _c_(633066, _a_(633063, _n_(633062, "self", lambda: self), "playSong"), _n_(633064, "ctx", lambda: ctx), _n_(633065, "url", lambda: url))
    _l_(633067)

    if _a_(633069, _n_(633068, "guild", lambda: guild), "id") in _n_(633070, "queues", lambda: queues):
      _l_(633083)

      _c_(633076, _a_(633074, _n_(633071, "queues", lambda: queues)[_a_(633073, _n_(633072, "guild", lambda: guild), "id")], "append"), _n_(633075, "stream", lambda: stream))
      _l_(633077)
    else:
      _n_(633078, "queues", lambda: queues)[_a_(633080, _n_(633079, "guild", lambda: guild), "id")] = [_n_(633081, "stream", lambda: stream)]
      _l_(633082)

    await _c_(633086, _a_(633085, _n_(633084, "ctx", lambda: ctx), "send"), "Song queued.")
    _l_(633087)