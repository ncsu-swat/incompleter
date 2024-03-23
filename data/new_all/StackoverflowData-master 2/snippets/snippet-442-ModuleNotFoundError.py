#Source: https://stackoverflow.com/questions/62525458/attributeerror-str-object-has-no-attribute-write-youtube-dl-kivy
import youtube_dl
from kivy.app import App
from kivy.uix.button import Button


class MusicApp(App):
    def build(self):
        return Button(text='Example')


ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
    'audio-format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=nTj4wVJAbNg'])