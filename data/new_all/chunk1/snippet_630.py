# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46437095/typeerror-dict-keyiterator-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(397425, _a_(397424, _n_(397423, "main", lambda: main), "route"), "/<int:user_id>/ratings", methods=["POST"])
def add_ratings(user_id):
    _l_(397463)

    # get the ratings from the Flask POST request object
    ratings_list = _c_(397433, _a_(397432, _c_(397431, _a_(397430, _c_(397429, _a_(397428, _a_(397427, _n_(397426, "request", lambda: request), "form"), "keys"))[0], "strip")), "split"), "\n")
    _l_(397434)
    ratings_list = _c_(397440, _n_(397435, "map", lambda: map), lambda x: _c_(397438, _a_(397437, _n_(397436, "x", lambda: x), "split"), ","), _n_(397439, "ratings_list", lambda: ratings_list))
    _l_(397441)
    # create a list with the format required by the negine (user_id, movie_id, rating)
    ratings = _c_(397451, _n_(397442, "map", lambda: map), lambda x: (_n_(397443, "user_id", lambda: user_id), _c_(397446, _n_(397444, "int", lambda: int), _n_(397445, "x", lambda: x)[0]), _c_(397449, _n_(397447, "float", lambda: float), _n_(397448, "x", lambda: x)[1])), _n_(397450, "ratings_list", lambda: ratings_list))
    _l_(397452)
    # add them to the model using then engine API
    _c_(397456, _a_(397454, _n_(397453, "recommendation_engine", lambda: recommendation_engine), "add_ratings"), _n_(397455, "ratings", lambda: ratings))
    _l_(397457)
    aux = _c_(397461, _a_(397459, _n_(397458, "json", lambda: json), "dumps"), _n_(397460, "ratings", lambda: ratings))
    _l_(397462)

    return aux