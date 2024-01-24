# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46018123/attributeerror-float-object-has-no-attribute-get-coords
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math, random, pylab, copy
    _l_(652839)

except ImportError:
    pass

class Location(_n_(652840, "object", lambda: object)):
    _l_(652891)

    def __init__(self, x, y):
        _l_(652851)

        _n_(652841, "self", lambda: self).x = _c_(652844, _n_(652842, "float", lambda: float), _n_(652843, "x", lambda: x))
        _l_(652845)
        _n_(652846, "self", lambda: self).y = _c_(652849, _n_(652847, "float", lambda: float), _n_(652848, "y", lambda: y))
        _l_(652850)
    def move(self, xc, yc):
        _l_(652865)

        aux = _c_(652863, _n_(652852, "Location", lambda: Location), _a_(652854, _n_(652853, "self", lambda: self), "x")+_c_(652857, _n_(652855, "float", lambda: float), _n_(652856, "xc", lambda: xc)), _a_(652859, _n_(652858, "self", lambda: self), "y")+_c_(652862, _n_(652860, "float", lambda: float), _n_(652861, "yc", lambda: yc)))
        _l_(652864)
        return aux
    def get_coords(self):
        _l_(652871)

        aux = _a_(652867, _n_(652866, "self", lambda: self), "x"), _a_(652869, _n_(652868, "self", lambda: self), "y")
        _l_(652870)
        return aux
    def get_dist(self, other):
        _l_(652890)

        ox, oy = _c_(652874, _a_(652873, _n_(652872, "other", lambda: other), "get_coords"))
        _l_(652875)
        x_dist = _a_(652877, _n_(652876, "self", lambda: self), "x") - _n_(652878, "ox", lambda: ox)
        _l_(652879)
        y_dist = _a_(652881, _n_(652880, "self", lambda: self), "y") - _n_(652882, "oy", lambda: oy)
        _l_(652883)
        aux = _c_(652888, _a_(652885, _n_(652884, "math", lambda: math), "sqrt"), _n_(652886, "x_dist", lambda: x_dist)**2 + _n_(652887, "y_dist", lambda: y_dist)**2)
        _l_(652889)
        return aux

class Compass_Pt(_n_(652892, "object", lambda: object)):
    _l_(652922)

    possibles = ('N', 'S', 'E', 'W')
    _l_(652893)
    def __init__(self, pt):
        _l_(652902)

        if _n_(652894, "pt", lambda: pt) in _a_(652896, _n_(652895, "self", lambda: self), "possibles"):
            _l_(652901)

_n_(652897, "self", lambda: self).pt = _n_(652898, "pt", lambda: pt)        else: raise _c_(652900, _n_(652899, "ValueError", lambda: ValueError), 'in Compass_Pt.__init__')

    def move(self, dist):
        _l_(652921)

        if _a_(652904, _n_(652903, "self", lambda: self), "pt") == 'N':
            _l_(652920)

return (0, _n_(652905, "dist", lambda: dist))        elif _a_(652907, _n_(652906, "self", lambda: self), "pt") == 'S':
            _l_(652919)

return (0, -_n_(652908, "dist", lambda: dist))        elif _a_(652910, _n_(652909, "self", lambda: self), "pt") == 'E':
            _l_(652918)

return (_n_(652911, "dist", lambda: dist), 0)        elif _a_(652913, _n_(652912, "self", lambda: self), "pt") == 'W':
            _l_(652917)

return (-_n_(652914, "dist", lambda: dist), 0)        else: raise _c_(652916, _n_(652915, "ValueError", lambda: ValueError), 'in Compass_Pt.move')

class Field(_n_(652923, "object", lambda: object)):
    _l_(652956)

    ''' Cartesian plane where object will be located '''
    _l_(652924)
    def __init__(self, drunk, loc):
        _l_(652931)

        _n_(652925, "self", lambda: self).drunk = _n_(652926, "drunk", lambda: drunk)
        _l_(652927)
        _n_(652928, "self", lambda: self).loc = _n_(652929, "loc", lambda: loc)
        _l_(652930)
    def move(self, cp, dist):
        _l_(652947)

        old_loc = _a_(652933, _n_(652932, "self", lambda: self), "loc")
        _l_(652934)
        xc, yc = _c_(652938, _a_(652936, _n_(652935, "cp", lambda: cp), "move"), _n_(652937, "dist", lambda: dist))
        _l_(652939)
        _n_(652940, "self", lambda: self).loc = _c_(652945, _a_(652942, _n_(652941, "old_loc", lambda: old_loc), "move"), _n_(652943, "xc", lambda: xc), _n_(652944, "yc", lambda: yc))
        _l_(652946)
    def get_loc(self):
        _l_(652951)

        aux = _a_(652949, _n_(652948, "self", lambda: self), "loc")
        _l_(652950)
        return aux
    def get_drunk(self):
        _l_(652955)

        aux = _a_(652953, _n_(652952, "self", lambda: self), "drunk")
        _l_(652954)
        return aux

class Drunk(_n_(652957, "object", lambda: object)):
    _l_(652983)

    ''' Point itself '''
    _l_(652958)
    def __init__(self, name):
        _l_(652962)

        _n_(652959, "self", lambda: self).name = _n_(652960, "name", lambda: name)
        _l_(652961)
    def move(self, field, cp, dist = 1):
        _l_(652982)

        if _a_(652966, _c_(652965, _a_(652964, _n_(652963, "field", lambda: field), "get_drunk")), "name") != _a_(652968, _n_(652967, "self", lambda: self), "name"):
            _l_(652972)

            raise _c_(652970, _n_(652969, "ValueError", lambda: ValueError), 'Drunk.move called with drunk not in the field')
            _l_(652971)
        for i in _c_(652975, _n_(652973, "range", lambda: range), _n_(652974, "dist", lambda: dist)):
            _l_(652981)

            _c_(652979, _a_(652977, _n_(652976, "field", lambda: field), "move"), _n_(652978, "cp", lambda: cp), 1)
            _l_(652980)

class Usual_Drunk(_n_(652984, "Drunk", lambda: Drunk)):
    _l_(653003)

    def move(self, field, dist = 1):
        _l_(653002)

        ''' Drunk.move superclass method override. Sends additional cp attribute.'''
        _l_(652985)
        cp = _c_(652990, _a_(652987, _n_(652986, "random", lambda: random), "choice"), _a_(652989, _n_(652988, "Compass_Pt", lambda: Compass_Pt), "possibles"))
        _l_(652991)
        _c_(653000, _a_(652993, _n_(652992, "Drunk", lambda: Drunk), "move"), _n_(652994, "self", lambda: self), _n_(652995, "field", lambda: field), _c_(652998, _n_(652996, "Compass_Pt", lambda: Compass_Pt), _n_(652997, "cp", lambda: cp)), _n_(652999, "dist", lambda: dist))
        _l_(653001)


class Cold_Drunk(_n_(653004, "Drunk", lambda: Drunk)):
    _l_(653034)

    def move(self, field, dist = 1):
        _l_(653033)

        cp = _c_(653009, _a_(653006, _n_(653005, "random", lambda: random), "choice"), _a_(653008, _n_(653007, "Compass_Pt", lambda: Compass_Pt), "possibles"))
        _l_(653010)
        if _n_(653011, "cp", lambda: cp) == 'S':
            _l_(653032)

            _c_(653020, _a_(653013, _n_(653012, "Drunk", lambda: Drunk), "move"), _n_(653014, "self", lambda: self), _n_(653015, "field", lambda: field), _c_(653018, _n_(653016, "Compass_Pt", lambda: Compass_Pt), _n_(653017, "cp", lambda: cp)), 2*_n_(653019, "dist", lambda: dist))
            _l_(653021)
        else:
            _c_(653030, _a_(653023, _n_(653022, "Drunk", lambda: Drunk), "move"), _n_(653024, "self", lambda: self), _n_(653025, "field", lambda: field), _c_(653028, _n_(653026, "Compass_Pt", lambda: Compass_Pt), _n_(653027, "cp", lambda: cp)), _n_(653029, "dist", lambda: dist))
            _l_(653031)

class EW_Drunk(_n_(653035, "Drunk", lambda: Drunk)):
    _l_(653062)

    def move(self, field, time = 1):
        _l_(653061)

        cp = _c_(653040, _a_(653037, _n_(653036, "random", lambda: random), "choice"), _a_(653039, _n_(653038, "Compass_Pt", lambda: Compass_Pt), "possibles"))
        _l_(653041)
        while _n_(653042, "cp", lambda: cp) != 'E' and  _n_(653043, "cp", lambda: cp) != 'W':
            _l_(653050)

            cp = _c_(653048, _a_(653045, _n_(653044, "random", lambda: random), "choice"), _a_(653047, _n_(653046, "Compass_Pt", lambda: Compass_Pt), "possibles"))
            _l_(653049)
        _c_(653059, _a_(653052, _n_(653051, "Drunk", lambda: Drunk), "move"), _n_(653053, "self", lambda: self), _n_(653054, "field", lambda: field), _c_(653057, _n_(653055, "Compass_Pt", lambda: Compass_Pt), _n_(653056, "cp", lambda: cp)), _n_(653058, "time", lambda: time))
        _l_(653060)

def perform_trial(time, f):
    _l_(653095)

    start = _c_(653065, _a_(653064, _n_(653063, "f", lambda: f), "get_loc"))
    _l_(653066)
    distances = [0,0]
    _l_(653067)
    for t in _c_(653070, _n_(653068, "range", lambda: range), 1, _n_(653069, "time", lambda: time) + 1):
        _l_(653092)

        _c_(653076, _a_(653074, _c_(653073, _a_(653072, _n_(653071, "f", lambda: f), "get_drunk")), "move"), _n_(653075, "f", lambda: f))
        _l_(653077)
        new_loc = _c_(653080, _a_(653079, _n_(653078, "f", lambda: f), "get_loc"))
        _l_(653081)
        distance = _c_(653085, _a_(653083, _n_(653082, "new_loc", lambda: new_loc), "get_dist"), _n_(653084, "start", lambda: start))
        _l_(653086)
        _c_(653090, _a_(653088, _n_(653087, "distances", lambda: distances), "append"), _n_(653089, "distance", lambda: distance))
        _l_(653091)
    aux = _n_(653093, "distances", lambda: distances)
    _l_(653094)
    return aux

def perform_sim(time, num_trials, drunk_type):
    _l_(653137)

    dist_lists = []
    _l_(653096)
    loc_lists = []
    _l_(653097)
    for trial in _c_(653100, _n_(653098, "range", lambda: range), _n_(653099, "num_trials", lambda: num_trials)):
        _l_(653133)

        d = _c_(653105, _n_(653101, "drunk_type", lambda: drunk_type), 'Drunk' + _c_(653104, _n_(653102, "str", lambda: str), _n_(653103, "trial", lambda: trial)))
        _l_(653106)
        f = _c_(653111, _n_(653107, "Field", lambda: Field), _n_(653108, "d", lambda: d), _c_(653110, _n_(653109, "Location", lambda: Location), 0, 0))
        _l_(653112)
        distances = _c_(653116, _n_(653113, "perform_trial", lambda: perform_trial), _n_(653114, "time", lambda: time), _n_(653115, "f", lambda: f))
        _l_(653117)
        locs = _c_(653121, _a_(653119, _n_(653118, "copy", lambda: copy), "deepcopy"), _n_(653120, "distances", lambda: distances))
        _l_(653122)
        _c_(653126, _a_(653124, _n_(653123, "dist_lists", lambda: dist_lists), "append"), _n_(653125, "distances", lambda: distances))
        _l_(653127)
        _c_(653131, _a_(653129, _n_(653128, "loc_lists", lambda: loc_lists), "append"), _n_(653130, "locs", lambda: locs))
        _l_(653132)
    aux = _n_(653134, "dist_lists", lambda: dist_lists), _n_(653135, "loc_lists", lambda: loc_lists)
    _l_(653136)
    return aux


def ans_quest(max_time, num_trials, drunk_type, title):
    _l_(653250)

    dist_lists, loc_lists = _c_(653142, _n_(653138, "perform_sim", lambda: perform_sim), _n_(653139, "max_time", lambda: max_time), _n_(653140, "num_trials", lambda: num_trials), _n_(653141, "drunk_type", lambda: drunk_type))
    _l_(653143)
    means = []
    _l_(653144)
    for t in _c_(653147, _n_(653145, "range", lambda: range), _n_(653146, "max_time", lambda: max_time) + 1):
        _l_(653162)

        tot = 0.0
        _l_(653148)
        for dist_l in _n_(653149, "dist_lists", lambda: dist_lists):
            _l_(653153)

            tot += _n_(653150, "dist_l", lambda: dist_l)[_n_(653151, "t", lambda: t)]
            _l_(653152)
        _c_(653160, _a_(653155, _n_(653154, "means", lambda: means), "append"), _n_(653156, "tot", lambda: tot)/_c_(653159, _n_(653157, "len", lambda: len), _n_(653158, "dist_lists", lambda: dist_lists)))
        _l_(653161)
    _c_(653165, _a_(653164, _n_(653163, "pylab", lambda: pylab), "figure"))
    _l_(653166)
    _c_(653170, _a_(653168, _n_(653167, "pylab", lambda: pylab), "plot"), _n_(653169, "means", lambda: means))
    _l_(653171)
    _c_(653174, _a_(653173, _n_(653172, "pylab", lambda: pylab), "ylabel"), 'distance')
    _l_(653175)
    _c_(653178, _a_(653177, _n_(653176, "pylab", lambda: pylab), "xlabel"), 'time')
    _l_(653179)
    _c_(653185, _a_(653181, _n_(653180, "pylab", lambda: pylab), "title"), _c_(653184, _a_(653182, '{} Ave. Distance', "format"), _n_(653183, "title", lambda: title)))
    _l_(653186)
    lastX = []
    _l_(653187)
    lastY = []
    _l_(653188)
    for loc_list in _n_(653189, "loc_lists", lambda: loc_lists):
        _l_(653204)

        x, y = _c_(653192, _a_(653191, _n_(653190, "loc_list", lambda: loc_list)[-1], "get_coords"))
        _l_(653193)
        _c_(653197, _a_(653195, _n_(653194, "lastX", lambda: lastX), "append"), _n_(653196, "x", lambda: x))
        _l_(653198)
        _c_(653202, _a_(653200, _n_(653199, "lastY", lambda: lastY), "append"), _n_(653201, "y", lambda: y))
        _l_(653203)
    _c_(653207, _a_(653206, _n_(653205, "pylab", lambda: pylab), "figure"))
    _l_(653208)
    _c_(653213, _a_(653210, _n_(653209, "pylab", lambda: pylab), "scatter"), _n_(653211, "lastX", lambda: lastX), _n_(653212, "lastY", lambda: lastY))
    _l_(653214)
    _c_(653217, _a_(653216, _n_(653215, "pylab", lambda: pylab), "ylabel"), 'NW Distance')
    _l_(653218)
    _c_(653224, _a_(653220, _n_(653219, "pylab", lambda: pylab), "title"), _c_(653223, _a_(653221, '{} Final location', "format"), _n_(653222, "title", lambda: title)))
    _l_(653225)
    _c_(653228, _a_(653227, _n_(653226, "pylab", lambda: pylab), "figure"))
    _l_(653229)
    _c_(653233, _a_(653231, _n_(653230, "pylab", lambda: pylab), "hist"), _n_(653232, "lastX", lambda: lastX))
    _l_(653234)
    _c_(653237, _a_(653236, _n_(653235, "pylab", lambda: pylab), "xlabel"), 'EW Value')
    _l_(653238)
    _c_(653241, _a_(653240, _n_(653239, "pylab", lambda: pylab), "ylabel"), 'Number of Trials')
    _l_(653242)
    _c_(653248, _a_(653244, _n_(653243, "pylab", lambda: pylab), "title"), _c_(653247, _a_(653245, '{} Distribution of Final EW Values', "format"), _n_(653246, "title", lambda: title)))
    _l_(653249)


num_steps = 50
_l_(653251)
num_trials = 10
_l_(653252)


_c_(653260, _n_(653253, "ans_quest", lambda: ans_quest), _n_(653254, "num_steps", lambda: num_steps), _n_(653255, "num_trials", lambda: num_trials), _n_(653256, "Usual_Drunk", lambda: Usual_Drunk), 'Usual Drunk ' + _c_(653259, _n_(653257, "str", lambda: str), _n_(653258, "num_trials", lambda: num_trials)) + ' Trials')
_l_(653261)
_c_(653269, _n_(653262, "ans_quest", lambda: ans_quest), _n_(653263, "num_steps", lambda: num_steps), _n_(653264, "num_trials", lambda: num_trials), _n_(653265, "Cold_Drunk", lambda: Cold_Drunk), 'Cold Drunk ' + _c_(653268, _n_(653266, "str", lambda: str), _n_(653267, "num_trials", lambda: num_trials)) + ' Trials')
_l_(653270)
_c_(653278, _n_(653271, "ans_quest", lambda: ans_quest), _n_(653272, "num_steps", lambda: num_steps), _n_(653273, "num_trials", lambda: num_trials), _n_(653274, "EW_Drunk", lambda: EW_Drunk), 'EW Drunk ' + _c_(653277, _n_(653275, "str", lambda: str), _n_(653276, "num_trials", lambda: num_trials)) + ' Trials')
_l_(653279)

_c_(653282, _a_(653281, _n_(653280, "pylab", lambda: pylab), "show"))
_l_(653283)