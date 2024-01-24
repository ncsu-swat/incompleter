# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46018123/attributeerror-float-object-has-no-attribute-get-coords
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math, random, pylab, copy
    _l_(689176)

except ImportError:
    pass

class Location(_n_(689177, "object", lambda: object)):
    _l_(689228)

    def __init__(self, x, y):
        _l_(689188)

        _n_(689178, "self", lambda: self).x = _c_(689181, _n_(689179, "float", lambda: float), _n_(689180, "x", lambda: x))
        _l_(689182)
        _n_(689183, "self", lambda: self).y = _c_(689186, _n_(689184, "float", lambda: float), _n_(689185, "y", lambda: y))
        _l_(689187)
    def move(self, xc, yc):
        _l_(689202)

        aux = _c_(689200, _n_(689189, "Location", lambda: Location), _a_(689191, _n_(689190, "self", lambda: self), "x")+_c_(689194, _n_(689192, "float", lambda: float), _n_(689193, "xc", lambda: xc)), _a_(689196, _n_(689195, "self", lambda: self), "y")+_c_(689199, _n_(689197, "float", lambda: float), _n_(689198, "yc", lambda: yc)))
        _l_(689201)
        return aux
    def get_coords(self):
        _l_(689208)

        aux = _a_(689204, _n_(689203, "self", lambda: self), "x"), _a_(689206, _n_(689205, "self", lambda: self), "y")
        _l_(689207)
        return aux
    def get_dist(self, other):
        _l_(689227)

        ox, oy = _c_(689211, _a_(689210, _n_(689209, "other", lambda: other), "get_coords"))
        _l_(689212)
        x_dist = _a_(689214, _n_(689213, "self", lambda: self), "x") - _n_(689215, "ox", lambda: ox)
        _l_(689216)
        y_dist = _a_(689218, _n_(689217, "self", lambda: self), "y") - _n_(689219, "oy", lambda: oy)
        _l_(689220)
        aux = _c_(689225, _a_(689222, _n_(689221, "math", lambda: math), "sqrt"), _n_(689223, "x_dist", lambda: x_dist)**2 + _n_(689224, "y_dist", lambda: y_dist)**2)
        _l_(689226)
        return aux

class Compass_Pt(_n_(689229, "object", lambda: object)):
    _l_(689259)

    possibles = ('N', 'S', 'E', 'W')
    _l_(689230)
    def __init__(self, pt):
        _l_(689239)

        if _n_(689231, "pt", lambda: pt) in _a_(689233, _n_(689232, "self", lambda: self), "possibles"):
            _l_(689238)

_n_(689234, "self", lambda: self).pt = _n_(689235, "pt", lambda: pt)        else: raise _c_(689237, _n_(689236, "ValueError", lambda: ValueError), 'in Compass_Pt.__init__')

    def move(self, dist):
        _l_(689258)

        if _a_(689241, _n_(689240, "self", lambda: self), "pt") == 'N':
            _l_(689257)

return (0, _n_(689242, "dist", lambda: dist))        elif _a_(689244, _n_(689243, "self", lambda: self), "pt") == 'S':
            _l_(689256)

return (0, -_n_(689245, "dist", lambda: dist))        elif _a_(689247, _n_(689246, "self", lambda: self), "pt") == 'E':
            _l_(689255)

return (_n_(689248, "dist", lambda: dist), 0)        elif _a_(689250, _n_(689249, "self", lambda: self), "pt") == 'W':
            _l_(689254)

return (-_n_(689251, "dist", lambda: dist), 0)        else: raise _c_(689253, _n_(689252, "ValueError", lambda: ValueError), 'in Compass_Pt.move')

class Field(_n_(689260, "object", lambda: object)):
    _l_(689293)

    ''' Cartesian plane where object will be located '''
    _l_(689261)
    def __init__(self, drunk, loc):
        _l_(689268)

        _n_(689262, "self", lambda: self).drunk = _n_(689263, "drunk", lambda: drunk)
        _l_(689264)
        _n_(689265, "self", lambda: self).loc = _n_(689266, "loc", lambda: loc)
        _l_(689267)
    def move(self, cp, dist):
        _l_(689284)

        old_loc = _a_(689270, _n_(689269, "self", lambda: self), "loc")
        _l_(689271)
        xc, yc = _c_(689275, _a_(689273, _n_(689272, "cp", lambda: cp), "move"), _n_(689274, "dist", lambda: dist))
        _l_(689276)
        _n_(689277, "self", lambda: self).loc = _c_(689282, _a_(689279, _n_(689278, "old_loc", lambda: old_loc), "move"), _n_(689280, "xc", lambda: xc), _n_(689281, "yc", lambda: yc))
        _l_(689283)
    def get_loc(self):
        _l_(689288)

        aux = _a_(689286, _n_(689285, "self", lambda: self), "loc")
        _l_(689287)
        return aux
    def get_drunk(self):
        _l_(689292)

        aux = _a_(689290, _n_(689289, "self", lambda: self), "drunk")
        _l_(689291)
        return aux

class Drunk(_n_(689294, "object", lambda: object)):
    _l_(689320)

    ''' Point itself '''
    _l_(689295)
    def __init__(self, name):
        _l_(689299)

        _n_(689296, "self", lambda: self).name = _n_(689297, "name", lambda: name)
        _l_(689298)
    def move(self, field, cp, dist = 1):
        _l_(689319)

        if _a_(689303, _c_(689302, _a_(689301, _n_(689300, "field", lambda: field), "get_drunk")), "name") != _a_(689305, _n_(689304, "self", lambda: self), "name"):
            _l_(689309)

            raise _c_(689307, _n_(689306, "ValueError", lambda: ValueError), 'Drunk.move called with drunk not in the field')
            _l_(689308)
        for i in _c_(689312, _n_(689310, "range", lambda: range), _n_(689311, "dist", lambda: dist)):
            _l_(689318)

            _c_(689316, _a_(689314, _n_(689313, "field", lambda: field), "move"), _n_(689315, "cp", lambda: cp), 1)
            _l_(689317)

class Usual_Drunk(_n_(689321, "Drunk", lambda: Drunk)):
    _l_(689340)

    def move(self, field, dist = 1):
        _l_(689339)

        ''' Drunk.move superclass method override. Sends additional cp attribute.'''
        _l_(689322)
        cp = _c_(689327, _a_(689324, _n_(689323, "random", lambda: random), "choice"), _a_(689326, _n_(689325, "Compass_Pt", lambda: Compass_Pt), "possibles"))
        _l_(689328)
        _c_(689337, _a_(689330, _n_(689329, "Drunk", lambda: Drunk), "move"), _n_(689331, "self", lambda: self), _n_(689332, "field", lambda: field), _c_(689335, _n_(689333, "Compass_Pt", lambda: Compass_Pt), _n_(689334, "cp", lambda: cp)), _n_(689336, "dist", lambda: dist))
        _l_(689338)


class Cold_Drunk(_n_(689341, "Drunk", lambda: Drunk)):
    _l_(689371)

    def move(self, field, dist = 1):
        _l_(689370)

        cp = _c_(689346, _a_(689343, _n_(689342, "random", lambda: random), "choice"), _a_(689345, _n_(689344, "Compass_Pt", lambda: Compass_Pt), "possibles"))
        _l_(689347)
        if _n_(689348, "cp", lambda: cp) == 'S':
            _l_(689369)

            _c_(689357, _a_(689350, _n_(689349, "Drunk", lambda: Drunk), "move"), _n_(689351, "self", lambda: self), _n_(689352, "field", lambda: field), _c_(689355, _n_(689353, "Compass_Pt", lambda: Compass_Pt), _n_(689354, "cp", lambda: cp)), 2*_n_(689356, "dist", lambda: dist))
            _l_(689358)
        else:
            _c_(689367, _a_(689360, _n_(689359, "Drunk", lambda: Drunk), "move"), _n_(689361, "self", lambda: self), _n_(689362, "field", lambda: field), _c_(689365, _n_(689363, "Compass_Pt", lambda: Compass_Pt), _n_(689364, "cp", lambda: cp)), _n_(689366, "dist", lambda: dist))
            _l_(689368)

class EW_Drunk(_n_(689372, "Drunk", lambda: Drunk)):
    _l_(689399)

    def move(self, field, time = 1):
        _l_(689398)

        cp = _c_(689377, _a_(689374, _n_(689373, "random", lambda: random), "choice"), _a_(689376, _n_(689375, "Compass_Pt", lambda: Compass_Pt), "possibles"))
        _l_(689378)
        while _n_(689379, "cp", lambda: cp) != 'E' and  _n_(689380, "cp", lambda: cp) != 'W':
            _l_(689387)

            cp = _c_(689385, _a_(689382, _n_(689381, "random", lambda: random), "choice"), _a_(689384, _n_(689383, "Compass_Pt", lambda: Compass_Pt), "possibles"))
            _l_(689386)
        _c_(689396, _a_(689389, _n_(689388, "Drunk", lambda: Drunk), "move"), _n_(689390, "self", lambda: self), _n_(689391, "field", lambda: field), _c_(689394, _n_(689392, "Compass_Pt", lambda: Compass_Pt), _n_(689393, "cp", lambda: cp)), _n_(689395, "time", lambda: time))
        _l_(689397)

def perform_trial(time, f):
    _l_(689432)

    start = _c_(689402, _a_(689401, _n_(689400, "f", lambda: f), "get_loc"))
    _l_(689403)
    distances = [0,0]
    _l_(689404)
    for t in _c_(689407, _n_(689405, "range", lambda: range), 1, _n_(689406, "time", lambda: time) + 1):
        _l_(689429)

        _c_(689413, _a_(689411, _c_(689410, _a_(689409, _n_(689408, "f", lambda: f), "get_drunk")), "move"), _n_(689412, "f", lambda: f))
        _l_(689414)
        new_loc = _c_(689417, _a_(689416, _n_(689415, "f", lambda: f), "get_loc"))
        _l_(689418)
        distance = _c_(689422, _a_(689420, _n_(689419, "new_loc", lambda: new_loc), "get_dist"), _n_(689421, "start", lambda: start))
        _l_(689423)
        _c_(689427, _a_(689425, _n_(689424, "distances", lambda: distances), "append"), _n_(689426, "distance", lambda: distance))
        _l_(689428)
    aux = _n_(689430, "distances", lambda: distances)
    _l_(689431)
    return aux

def perform_sim(time, num_trials, drunk_type):
    _l_(689474)

    dist_lists = []
    _l_(689433)
    loc_lists = []
    _l_(689434)
    for trial in _c_(689437, _n_(689435, "range", lambda: range), _n_(689436, "num_trials", lambda: num_trials)):
        _l_(689470)

        d = _c_(689442, _n_(689438, "drunk_type", lambda: drunk_type), 'Drunk' + _c_(689441, _n_(689439, "str", lambda: str), _n_(689440, "trial", lambda: trial)))
        _l_(689443)
        f = _c_(689448, _n_(689444, "Field", lambda: Field), _n_(689445, "d", lambda: d), _c_(689447, _n_(689446, "Location", lambda: Location), 0, 0))
        _l_(689449)
        distances = _c_(689453, _n_(689450, "perform_trial", lambda: perform_trial), _n_(689451, "time", lambda: time), _n_(689452, "f", lambda: f))
        _l_(689454)
        locs = _c_(689458, _a_(689456, _n_(689455, "copy", lambda: copy), "deepcopy"), _n_(689457, "distances", lambda: distances))
        _l_(689459)
        _c_(689463, _a_(689461, _n_(689460, "dist_lists", lambda: dist_lists), "append"), _n_(689462, "distances", lambda: distances))
        _l_(689464)
        _c_(689468, _a_(689466, _n_(689465, "loc_lists", lambda: loc_lists), "append"), _n_(689467, "locs", lambda: locs))
        _l_(689469)
    aux = _n_(689471, "dist_lists", lambda: dist_lists), _n_(689472, "loc_lists", lambda: loc_lists)
    _l_(689473)
    return aux


def ans_quest(max_time, num_trials, drunk_type, title):
    _l_(689587)

    dist_lists, loc_lists = _c_(689479, _n_(689475, "perform_sim", lambda: perform_sim), _n_(689476, "max_time", lambda: max_time), _n_(689477, "num_trials", lambda: num_trials), _n_(689478, "drunk_type", lambda: drunk_type))
    _l_(689480)
    means = []
    _l_(689481)
    for t in _c_(689484, _n_(689482, "range", lambda: range), _n_(689483, "max_time", lambda: max_time) + 1):
        _l_(689499)

        tot = 0.0
        _l_(689485)
        for dist_l in _n_(689486, "dist_lists", lambda: dist_lists):
            _l_(689490)

            tot += _n_(689487, "dist_l", lambda: dist_l)[_n_(689488, "t", lambda: t)]
            _l_(689489)
        _c_(689497, _a_(689492, _n_(689491, "means", lambda: means), "append"), _n_(689493, "tot", lambda: tot)/_c_(689496, _n_(689494, "len", lambda: len), _n_(689495, "dist_lists", lambda: dist_lists)))
        _l_(689498)
    _c_(689502, _a_(689501, _n_(689500, "pylab", lambda: pylab), "figure"))
    _l_(689503)
    _c_(689507, _a_(689505, _n_(689504, "pylab", lambda: pylab), "plot"), _n_(689506, "means", lambda: means))
    _l_(689508)
    _c_(689511, _a_(689510, _n_(689509, "pylab", lambda: pylab), "ylabel"), 'distance')
    _l_(689512)
    _c_(689515, _a_(689514, _n_(689513, "pylab", lambda: pylab), "xlabel"), 'time')
    _l_(689516)
    _c_(689522, _a_(689518, _n_(689517, "pylab", lambda: pylab), "title"), _c_(689521, _a_(689519, '{} Ave. Distance', "format"), _n_(689520, "title", lambda: title)))
    _l_(689523)
    lastX = []
    _l_(689524)
    lastY = []
    _l_(689525)
    for loc_list in _n_(689526, "loc_lists", lambda: loc_lists):
        _l_(689541)

        x, y = _c_(689529, _a_(689528, _n_(689527, "loc_list", lambda: loc_list)[-1], "get_coords"))
        _l_(689530)
        _c_(689534, _a_(689532, _n_(689531, "lastX", lambda: lastX), "append"), _n_(689533, "x", lambda: x))
        _l_(689535)
        _c_(689539, _a_(689537, _n_(689536, "lastY", lambda: lastY), "append"), _n_(689538, "y", lambda: y))
        _l_(689540)
    _c_(689544, _a_(689543, _n_(689542, "pylab", lambda: pylab), "figure"))
    _l_(689545)
    _c_(689550, _a_(689547, _n_(689546, "pylab", lambda: pylab), "scatter"), _n_(689548, "lastX", lambda: lastX), _n_(689549, "lastY", lambda: lastY))
    _l_(689551)
    _c_(689554, _a_(689553, _n_(689552, "pylab", lambda: pylab), "ylabel"), 'NW Distance')
    _l_(689555)
    _c_(689561, _a_(689557, _n_(689556, "pylab", lambda: pylab), "title"), _c_(689560, _a_(689558, '{} Final location', "format"), _n_(689559, "title", lambda: title)))
    _l_(689562)
    _c_(689565, _a_(689564, _n_(689563, "pylab", lambda: pylab), "figure"))
    _l_(689566)
    _c_(689570, _a_(689568, _n_(689567, "pylab", lambda: pylab), "hist"), _n_(689569, "lastX", lambda: lastX))
    _l_(689571)
    _c_(689574, _a_(689573, _n_(689572, "pylab", lambda: pylab), "xlabel"), 'EW Value')
    _l_(689575)
    _c_(689578, _a_(689577, _n_(689576, "pylab", lambda: pylab), "ylabel"), 'Number of Trials')
    _l_(689579)
    _c_(689585, _a_(689581, _n_(689580, "pylab", lambda: pylab), "title"), _c_(689584, _a_(689582, '{} Distribution of Final EW Values', "format"), _n_(689583, "title", lambda: title)))
    _l_(689586)


num_steps = 50
_l_(689588)
num_trials = 10
_l_(689589)


_c_(689597, _n_(689590, "ans_quest", lambda: ans_quest), _n_(689591, "num_steps", lambda: num_steps), _n_(689592, "num_trials", lambda: num_trials), _n_(689593, "Usual_Drunk", lambda: Usual_Drunk), 'Usual Drunk ' + _c_(689596, _n_(689594, "str", lambda: str), _n_(689595, "num_trials", lambda: num_trials)) + ' Trials')
_l_(689598)
_c_(689606, _n_(689599, "ans_quest", lambda: ans_quest), _n_(689600, "num_steps", lambda: num_steps), _n_(689601, "num_trials", lambda: num_trials), _n_(689602, "Cold_Drunk", lambda: Cold_Drunk), 'Cold Drunk ' + _c_(689605, _n_(689603, "str", lambda: str), _n_(689604, "num_trials", lambda: num_trials)) + ' Trials')
_l_(689607)
_c_(689615, _n_(689608, "ans_quest", lambda: ans_quest), _n_(689609, "num_steps", lambda: num_steps), _n_(689610, "num_trials", lambda: num_trials), _n_(689611, "EW_Drunk", lambda: EW_Drunk), 'EW Drunk ' + _c_(689614, _n_(689612, "str", lambda: str), _n_(689613, "num_trials", lambda: num_trials)) + ' Trials')
_l_(689616)

_c_(689619, _a_(689618, _n_(689617, "pylab", lambda: pylab), "show"))
_l_(689620)