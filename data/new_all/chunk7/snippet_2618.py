# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68782504/spotify-voice-assistant-attribute-error-enter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(575071)

except ImportError:
    pass
try:
    from speech_recognition import Microphone, Recognizer, UnknownValueError
    _l_(575073)

except ImportError:
    pass
try:
    import spotipy as sp
    _l_(575075)

except ImportError:
    pass
try:
    from spotipy.oauth2 import SpotifyOAuth
    _l_(575077)

except ImportError:
    pass
try:
    from pepper import *
    _l_(575079)

except ImportError:
    pass

# Set variables from setup.txt
setup = _c_(575082, _a_(575081, _n_(575080, "pd", lambda: pd), "read_csv"), r'C:\Users\Yousif\Documents\Python spotify\setup.txt', sep='=', index_col=0, squeeze=True, header=None)
_l_(575083)
client_id = _n_(575084, "setup", lambda: setup)['client_id']
_l_(575085)
client_secret = _n_(575086, "setup", lambda: setup)['client_secret']
_l_(575087)
device_name = _n_(575088, "setup", lambda: setup)['device_name']
_l_(575089)
redirect_uri = _n_(575090, "setup", lambda: setup)['redirect_uri']
_l_(575091)
scope = _n_(575092, "setup", lambda: setup)['scope']
_l_(575093)
username = _n_(575094, "setup", lambda: setup)['username']
_l_(575095)

# Connecting to the Spotify account
auth_manager = _c_(575102, _n_(575096, "SpotifyOAuth", lambda: SpotifyOAuth), client_id=_n_(575097, "client_id", lambda: client_id),
    client_secret=_n_(575098, "client_secret", lambda: client_secret),
    redirect_uri=_n_(575099, "redirect_uri", lambda: redirect_uri),
    scope=_n_(575100, "scope", lambda: scope),
    username=_n_(575101, "username", lambda: username))
_l_(575103)
spotify = _c_(575107, _a_(575105, _n_(575104, "sp", lambda: sp), "Spotify"), auth_manager=_n_(575106, "auth_manager", lambda: auth_manager))
_l_(575108)

# Selecting device to play from
devices = _c_(575111, _a_(575110, _n_(575109, "spotify", lambda: spotify), "devices"))
_l_(575112)
deviceID = None
_l_(575113)
for d in _n_(575114, "devices", lambda: devices)['devices']:
    _l_(575126)

    _n_(575115, "d", lambda: d)['name'] = _c_(575118, _a_(575117, _n_(575116, "d", lambda: d)['name'], "replace"), '’', '\'')
    _l_(575119)
    if _n_(575120, "d", lambda: d)['name'] == _n_(575121, "device_name", lambda: device_name):
        _l_(575125)

        deviceID = _n_(575122, "d", lambda: d)['id']
        _l_(575123)
        break
        _l_(575124)

# Setup microphone and speech recognizer
r = _c_(575128, _n_(575127, "Recognizer", lambda: Recognizer))
_l_(575129)
m = None
_l_(575130)
input_mic = 'Voicemod Virtual Audio Device (WDM)'  # Use whatever is your desired input
_l_(575131)  # Use whatever is your desired input
for i, microphone_name in _c_(575136, _n_(575132, "enumerate", lambda: enumerate), _c_(575135, _a_(575134, _n_(575133, "Microphone", lambda: Microphone), "list_microphone_names"))):
    _l_(575144)

    if _n_(575137, "microphone_name", lambda: microphone_name) == _n_(575138, "input_mic", lambda: input_mic):
        _l_(575143)

        m = _c_(575141, _n_(575139, "Microphone", lambda: Microphone), device_index=_n_(575140, "i", lambda: i))
        _l_(575142)

while True:
    _l_(575237)

    """
    Commands will be entered in the specific format explained here:
     - the first word will be one of: 'album', 'artist', 'play'
     - then the name of whatever item is wanted
    """
    with _n_(575145, "m", lambda: m) as source:
        _l_(575156)

        _c_(575149, _a_(575147, _n_(575146, "r", lambda: r), "adjust_for_ambient_noise"), source=_n_(575148, "source", lambda: source))
        _l_(575150)
        audio = _c_(575154, _a_(575152, _n_(575151, "r", lambda: r), "listen"), source=_n_(575153, "source", lambda: source))
        _l_(575155)

    command = None
    _l_(575157)
    try:
        _l_(575168)

        command = _c_(575163, _a_(575162, _c_(575161, _a_(575159, _n_(575158, "r", lambda: r), "recognize_google"), audio_data=_n_(575160, "audio", lambda: audio)), "lower"))
        _l_(575164)
    except _n_(575165, "UnknownValueError", lambda: UnknownValueError):
        _l_(575167)

        continue
        _l_(575166)

    _c_(575171, _n_(575169, "print", lambda: print), _n_(575170, "command", lambda: command))
    _l_(575172)
    words = _c_(575175, _a_(575174, _n_(575173, "command", lambda: command), "split"))
    _l_(575176)
    if _c_(575179, _n_(575177, "len", lambda: len), _n_(575178, "words", lambda: words)) <= 1:
        _l_(575184)

        _c_(575181, _n_(575180, "print", lambda: print), 'Could not understand. Try again')
        _l_(575182)
        continue
        _l_(575183)

    name = _c_(575187, _a_(575185, ' ', "join"), _n_(575186, "words", lambda: words)[1:])
    _l_(575188)
    try:
        _l_(575236)

        if _n_(575189, "words", lambda: words)[0] == 'album':
            _l_(575230)

            uri = _c_(575193, _n_(575190, "get_album_uri", lambda: get_album_uri), spotify=_n_(575191, "spotify", lambda: spotify), name=_n_(575192, "name", lambda: name))
            _l_(575194)
            _c_(575199, _n_(575195, "play_album", lambda: play_album), spotify=_n_(575196, "spotify", lambda: spotify), device_id=_n_(575197, "deviceID", lambda: deviceID), uri=_n_(575198, "uri", lambda: uri))
            _l_(575200)
        elif _n_(575201, "words", lambda: words)[0] == 'artist':
            _l_(575229)

            uri = _c_(575205, _n_(575202, "get_artist_uri", lambda: get_artist_uri), spotify=_n_(575203, "spotify", lambda: spotify), name=_n_(575204, "name", lambda: name))
            _l_(575206)
            _c_(575211, _n_(575207, "play_artist", lambda: play_artist), spotify=_n_(575208, "spotify", lambda: spotify), device_id=_n_(575209, "deviceID", lambda: deviceID), uri=_n_(575210, "uri", lambda: uri))
            _l_(575212)
        elif _n_(575213, "words", lambda: words)[0] == 'play':
            _l_(575228)

            uri = _c_(575217, _n_(575214, "get_track_uri", lambda: get_track_uri), spotify=_n_(575215, "spotify", lambda: spotify), name=_n_(575216, "name", lambda: name))
            _l_(575218)
            _c_(575223, _n_(575219, "play_track", lambda: play_track), spotify=_n_(575220, "spotify", lambda: spotify), device_id=_n_(575221, "deviceID", lambda: deviceID), uri=_n_(575222, "uri", lambda: uri))
            _l_(575224)
        else:
            _c_(575226, _n_(575225, "print", lambda: print), 'Specify either "album", "artist" or "play". Try Again')
            _l_(575227)
    except _n_(575231, "InvalidSearchError", lambda: InvalidSearchError):
        _l_(575235)

        _c_(575233, _n_(575232, "print", lambda: print), 'InvalidSearchError. Try Again')
        _l_(575234)