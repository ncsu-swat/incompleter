# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77129857/typeerror-when-initializing-updater-in-python-telegram-bot
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(614525)

except ImportError:
    pass
try:
    from telegram import Update
    _l_(614527)

except ImportError:
    pass
try:
    from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
    _l_(614529)

except ImportError:
    pass
try:
    import telegram.ext.filters as filters
    _l_(614531)

except ImportError:
    pass
try:
    from pytube import YouTube
    _l_(614533)

except ImportError:
    pass

def start(update: _n_(614534, "Update", lambda: Update), context: _n_(614535, "CallbackContext", lambda: CallbackContext)) -> None:
    _l_(614541)

    _c_(614539, _a_(614538, _a_(614537, _n_(614536, "update", lambda: update), "message"), "reply_text"), 'Send me a YouTube link with /download to get the video.')
    _l_(614540)

def download_video(update: _n_(614542, "Update", lambda: Update), context: _n_(614543, "CallbackContext", lambda: CallbackContext)) -> None:
    _l_(614583)

    url = _a_(614545, _n_(614544, "context", lambda: context), "args")[0]
    _l_(614546)
    yt = _c_(614549, _n_(614547, "YouTube", lambda: YouTube), _n_(614548, "url", lambda: url))
    _l_(614550)
    video = _c_(614554, _a_(614553, _a_(614552, _n_(614551, "yt", lambda: yt), "streams"), "get_highest_resolution"))
    _l_(614555)
    _c_(614558, _a_(614557, _n_(614556, "video", lambda: video), "download"))
    _l_(614559)
    filename = f"{_a_(614561, _n_(614560, 'yt', lambda: yt), 'title')}.mp4"
    _l_(614562)
    _c_(614568, _a_(614564, _n_(614563, "os", lambda: os), "rename"), _a_(614566, _n_(614565, "video", lambda: video), "default_filename"), _n_(614567, "filename", lambda: filename))
    _l_(614569)
    _c_(614576, _a_(614572, _a_(614571, _n_(614570, "update", lambda: update), "message"), "reply_document"), document=_c_(614575, _n_(614573, "open", lambda: open), _n_(614574, "filename", lambda: filename), 'rb'))
    _l_(614577)
    _c_(614581, _a_(614579, _n_(614578, "os", lambda: os), "remove"), _n_(614580, "filename", lambda: filename))
    _l_(614582)

def main() -> None:
    _l_(614623)

    updater = _c_(614585, _n_(614584, "Updater", lambda: Updater), token='646XXXXXXXXXXXXXXXXXXXXXXXXXmQM', use_context=True)
    _l_(614586)
    dispatcher = _a_(614588, _n_(614587, "updater", lambda: updater), "dispatcher")
    _l_(614589)

    _c_(614595, _a_(614591, _n_(614590, "dispatcher", lambda: dispatcher), "add_handler"), _c_(614594, _n_(614592, "CommandHandler", lambda: CommandHandler), 'start', _n_(614593, "start", lambda: start)))
    _l_(614596)
    _c_(614602, _a_(614598, _n_(614597, "dispatcher", lambda: dispatcher), "add_handler"), _c_(614601, _n_(614599, "CommandHandler", lambda: CommandHandler), 'download', _n_(614600, "download_video", lambda: download_video), pass_args=True))
    _l_(614603)
    _c_(614613, _a_(614605, _n_(614604, "dispatcher", lambda: dispatcher), "add_handler"), _c_(614612, _n_(614606, "MessageHandler", lambda: MessageHandler), _a_(614608, _n_(614607, "Filters", lambda: Filters), "TEXT") & ~_a_(614610, _n_(614609, "Filters", lambda: Filters), "COMMAND"), _n_(614611, "start", lambda: start)))
    _l_(614614)

    _c_(614617, _a_(614616, _n_(614615, "updater", lambda: updater), "start_polling"))
    _l_(614618)
    _c_(614621, _a_(614620, _n_(614619, "updater", lambda: updater), "idle"))
    _l_(614622)

if _n_(614624, "__name__", lambda: __name__) == '__main__':
    _l_(614628)

    _c_(614626, _n_(614625, "main", lambda: main))
    _l_(614627)