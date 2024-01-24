# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35389866/filenotfounderror-errno-2-no-such-file-or-directory-abc-txt
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(665843, _n_(665841, "open", lambda: open), _n_(665842, "filename", lambda: filename), "r+b") as reviewfile:
    _l_(665863)

    with _c_(665845, _n_(665844, "open", lambda: open), 'database_set.txt', "wb") as aprior:
        _l_(665862)

        _c_(665850, _a_(665847, _n_(665846, "reviewfile", lambda: reviewfile), "write"), "\n \t \t \t \t \t" + _n_(665848, "titlelist", lambda: titlelist)[_n_(665849, "user_choice", lambda: user_choice) - 1])
        _l_(665851)
        _c_(665860, _a_(665853, _n_(665852, "reviewfile", lambda: reviewfile), "write"), "\n \n \t \t \t \t \tAverage rating " +
                         _c_(665856, _n_(665854, "str", lambda: str), _n_(665855, "avg_rating", lambda: avg_rating)) + " based on " + _c_(665859, _n_(665857, "str", lambda: str), _n_(665858, "total_no_ratings", lambda: total_no_ratings)) + " ratings")
        _l_(665861)