# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73551025/discord-py-self-aftererror-typeerror-lambda-takes-0-positional-arguments
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
players = {}
_l_(622580)
queues = {}
_l_(622581)

class music(_a_(622583, _n_(622582, "commands", lambda: commands), "Cog")):
  _l_(622710)

  def __init__(self, client):
    _l_(622587)

    _n_(622584, "self", lambda: self).client = _n_(622585, "client", lambda: client)
    _l_(622586)

  def queueCheck(self, id, vc):
    _l_(622605)

    if _n_(622588, "queues", lambda: queues)[_n_(622589, "id", lambda: id)] != []:
      _l_(622604)

      stream = _c_(622593, _a_(622592, _n_(622590, "queues", lambda: queues)[_n_(622591, "id", lambda: id)], "pop"), 0, None)
      _l_(622594)
      _n_(622595, "players", lambda: players)[_n_(622596, "id", lambda: id)] = _n_(622597, "stream", lambda: stream)
      _l_(622598)
      _c_(622602, _a_(622600, _n_(622599, "vc", lambda: vc), "play"), _n_(622601, "stream", lambda: stream))
      _l_(622603)

  

  async def playSong(self, ctx, url):
    _l_(622635)

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    _l_(622606)
    YDL_OPTIONS = {'format':"bestaudio",
                    'default_search':'auto'}
    _l_(622607)
    
    with _c_(622611, _a_(622609, _n_(622608, "youtube_dl", lambda: youtube_dl), "YoutubeDL"), _n_(622610, "YDL_OPTIONS", lambda: YDL_OPTIONS)) as ydl:
      _l_(622632)

      info = _c_(622615, _a_(622613, _n_(622612, "ydl", lambda: ydl), "extract_info"), _n_(622614, "url", lambda: url), download=False)
      _l_(622616)
      if 'entries' in _n_(622617, "info", lambda: info):
        _l_(622624)

        url2 = _n_(622618, "info", lambda: info)['entries'][0]['formats'][0]['url']
        _l_(622619)
      elif 'formats' in _n_(622620, "info", lambda: info):
        _l_(622623)

        url2 = _n_(622621, "info", lambda: info)['formats'][0]['url']
        _l_(622622)
      stream = await _c_(622630, _a_(622627, _a_(622626, _n_(622625, "discord", lambda: discord), "FFmpegOpusAudio"), "from_probe"), _n_(622628, "url2", lambda: url2), **_n_(622629, "FFMPEG_OPTIONS", lambda: FFMPEG_OPTIONS))
      _l_(622631)
    aux = _n_(622633, "stream", lambda: stream)
    _l_(622634)

    return aux
  
  @_c_(622637, _a_(622636, commands, "command"))
  async def play(self, ctx, *, url):
    _l_(622676)

    if _a_(622639, _n_(622638, "ctx", lambda: ctx), "voice_client") is None:
      _l_(622647)

      await _c_(622645, _a_(622644, _a_(622643, _a_(622642, _a_(622641, _n_(622640, "ctx", lambda: ctx), "author"), "voice"), "channel"), "connect"))
      _l_(622646)

    stream = await _c_(622652, _a_(622649, _n_(622648, "self", lambda: self), "playSong"), _n_(622650, "ctx", lambda: ctx), _n_(622651, "url", lambda: url))
    _l_(622653)
    guild = _a_(622656, _a_(622655, _n_(622654, "ctx", lambda: ctx), "message"), "guild")
    _l_(622657)
    vc = _a_(622659, _n_(622658, "ctx", lambda: ctx), "voice_client")
    _l_(622660)
    _n_(622661, "players", lambda: players)[_a_(622663, _n_(622662, "guild", lambda: guild), "id")] = _n_(622664, "stream", lambda: stream)
    _l_(622665)
    _c_(622674, _a_(622667, _n_(622666, "vc", lambda: vc), "play"), _n_(622668, "stream", lambda: stream), after=lambda: _c_(622673, _a_(622670, _n_(622669, "self", lambda: self), "queueCheck"), _n_(622671, "guild", lambda: guild), _n_(622672, "vc", lambda: vc)))
    _l_(622675)

  @_c_(622678, _a_(622677, commands, "command"))
  async def queue(self, ctx, url):
    _l_(622709)

    guild = _a_(622681, _a_(622680, _n_(622679, "ctx", lambda: ctx), "message"), "guild")
    _l_(622682)
    stream = await _c_(622687, _a_(622684, _n_(622683, "self", lambda: self), "playSong"), _n_(622685, "ctx", lambda: ctx), _n_(622686, "url", lambda: url))
    _l_(622688)

    if _a_(622690, _n_(622689, "guild", lambda: guild), "id") in _n_(622691, "queues", lambda: queues):
      _l_(622704)

      _c_(622697, _a_(622695, _n_(622692, "queues", lambda: queues)[_a_(622694, _n_(622693, "guild", lambda: guild), "id")], "append"), _n_(622696, "stream", lambda: stream))
      _l_(622698)
    else:
      _n_(622699, "queues", lambda: queues)[_a_(622701, _n_(622700, "guild", lambda: guild), "id")] = [_n_(622702, "stream", lambda: stream)]
      _l_(622703)

    await _c_(622707, _a_(622706, _n_(622705, "ctx", lambda: ctx), "send"), "Song queued.")
    _l_(622708)