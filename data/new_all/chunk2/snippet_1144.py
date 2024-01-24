# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55145601/the-json-object-must-be-str-not-list-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(447955)

except ImportError:
    pass
try:
    import json
    _l_(447957)

except ImportError:
    pass
try:
    from .models import Movie
    _l_(447959)

except ImportError:
    pass

def detail(request):
    _l_(447988)


    with _c_(447961, _n_(447960, "open", lambda: open), 'movie_data.json', encoding='utf-8') as data_file:
        _l_(447975)

        json_data = _c_(447967, _a_(447963, _n_(447962, "json", lambda: json), "loads"), _c_(447966, _a_(447965, _n_(447964, "data_file", lambda: data_file), "read")))
        _l_(447968)
        _c_(447973, _n_(447969, "print", lambda: print), _c_(447972, _n_(447970, "type", lambda: type), _n_(447971, "json_data", lambda: json_data)))
        _l_(447974)

    json_dict = _c_(447979, _a_(447977, _n_(447976, "json", lambda: json), "loads"), _n_(447978, "json_data", lambda: json_data))
    _l_(447980)
    for movie_data in _n_(447981, "json_dict", lambda: json_dict):
        _l_(447987)

        movie = _c_(447985, _a_(447983, _n_(447982, "Movie", lambda: Movie), "create"), **_n_(447984, "movie_data", lambda: movie_data))
        _l_(447986)