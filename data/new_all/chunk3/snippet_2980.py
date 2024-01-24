# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56056538/attributeerror-io-textiowrapper-object-has-no-attribute-replace
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
artists = _c_(541876, _n_(541875, "open", lambda: open), 'artists.txt') ## IF YOU WANT TO EDIT THE SONG NAMES AND ARTISTS
_l_(541877) ## IF YOU WANT TO EDIT THE SONG NAMES AND ARTISTS
songs = _c_(541879, _n_(541878, "open", lambda: open), 'songs.txt') ## YOU NEED TO LEAVE THEM IN ORDER
_l_(541880) ## YOU NEED TO LEAVE THEM IN ORDER

songfilter = 'abcdefghijklmnopqrstuvwxyz\/' #Lowercase Alphabet With Some Slashes To Remove "/n"
_l_(541881) #Lowercase Alphabet With Some Slashes To Remove "/n"

songsFiltered = [_c_(541885, _a_(541883, _n_(541882, "songs", lambda: songs), "replace"), _n_(541884, "alphabet", lambda: alphabet), '') for w in _n_(541886, "songs", lambda: songs)]
_l_(541887)

guessList = _c_(541893, _n_(541888, "list", lambda: list), _c_(541892, _n_(541889, "zip", lambda: zip), _n_(541890, "artists", lambda: artists), _n_(541891, "songs", lambda: songs)))
_l_(541894)

songSelect = _c_(541898, _a_(541896, _n_(541895, "random", lambda: random), "choice"), _n_(541897, "guessList", lambda: guessList))
_l_(541899)

_c_(541902, _n_(541900, "print", lambda: print), _n_(541901, "songSelect", lambda: songSelect))
_l_(541903)