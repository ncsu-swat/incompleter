# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62525458/attributeerror-str-object-has-no-attribute-write-youtube-dl-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import youtube_dl
    _l_(388323)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(388325)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(388327)

except ImportError:
    pass


class MusicApp(_n_(388328, "App", lambda: App)):
    _l_(388333)

    def build(self):
        _l_(388332)

        aux = _c_(388330, _n_(388329, "Button", lambda: Button), text='Example')
        _l_(388331)
        return aux


ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'audio-format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
_l_(388334)
with _c_(388338, _a_(388336, _n_(388335, "youtube_dl", lambda: youtube_dl), "YoutubeDL"), _n_(388337, "ydl_opts", lambda: ydl_opts)) as ydl:
    _l_(388343)

    _c_(388341, _a_(388340, _n_(388339, "ydl", lambda: ydl), "download"), ['https://www.youtube.com/watch?v=BaW_jenozKc'])
    _l_(388342)