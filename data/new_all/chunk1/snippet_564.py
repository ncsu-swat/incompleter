# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47028093/attributeerror-spotify-object-has-no-attribute-current-user-saved-tracks
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
token = _c_(387838, _a_(387832, _n_(387831, "util", lambda: util), "prompt_for_user_token"), _n_(387833, "username", lambda: username), scope = _n_(387834, "scope", lambda: scope), client_id=_n_(387835, "client_id", lambda: client_id), client_secret=_n_(387836, "client_secret", lambda: client_secret), redirect_uri=_n_(387837, "redirect_uri", lambda: redirect_uri))
_l_(387839)

sp = _c_(387843, _a_(387841, _n_(387840, "spotipy", lambda: spotipy), "Spotify"), auth = _n_(387842, "token", lambda: token))
_l_(387844)

saved = _c_(387847, _a_(387846, _n_(387845, "sp", lambda: sp), "current_user_saved_tracks"))
_l_(387848)
_c_(387851, _n_(387849, "print", lambda: print), _n_(387850, "saved", lambda: saved))
_l_(387852)
recent = _c_(387855, _a_(387854, _n_(387853, "sp", lambda: sp), "current_user_recently_played"))
_l_(387856)
_c_(387859, _n_(387857, "print", lambda: print), _n_(387858, "recent", lambda: recent))
_l_(387860)