# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62525458/attributeerror-str-object-has-no-attribute-write-youtube-dl-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import youtube_dl
    _l_(406302)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(406304)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(406306)

except ImportError:
    pass


class MusicApp(_n_(406307, "App", lambda: App)):
    _l_(406312)

    def build(self):
        _l_(406311)

        aux = _c_(406309, _n_(406308, "Button", lambda: Button), text='Example')
        _l_(406310)
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
_l_(406313)
with _c_(406317, _a_(406315, _n_(406314, "youtube_dl", lambda: youtube_dl), "YoutubeDL"), _n_(406316, "ydl_opts", lambda: ydl_opts)) as ydl:
    _l_(406322)

    _c_(406320, _a_(406319, _n_(406318, "ydl", lambda: ydl), "download"), ['https://www.youtube.com/watch?v=nTj4wVJAbNg'])
    _l_(406321)