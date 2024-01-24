# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55469766/typeerror-list-object-is-not-callable-problem-with-passing-generated-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(653534)

except ImportError:
    pass
try:
    import math
    _l_(653536)

except ImportError:
    pass
try:
    import random
    _l_(653538)

except ImportError:
    pass
try:
    import operator
    _l_(653540)

except ImportError:
    pass

# Global variables
a = 0.1
_l_(653541)
b = 1
_l_(653542)


def function(x):
    _l_(653555)

    aux = (_c_(653548, _a_(653544, _n_(653543, "math", lambda: math), "sin"), 40*_a_(653546, _n_(653545, "math", lambda: math), "pi")*_n_(653547, "x", lambda: x))+_c_(653552, _a_(653550, _n_(653549, "math", lambda: math), "pow"), _n_(653551, "x", lambda: x)-1, 4))/(2*_n_(653553, "x", lambda: x))
    _l_(653554)
    return aux


def initial_pop():
    _l_(653569)

    pop = _c_(653561, _a_(653558, _a_(653557, _n_(653556, "np", lambda: np), "random"), "uniform"), _n_(653559, "a", lambda: a), _n_(653560, "b", lambda: b), 20)
    _l_(653562)
    pop = _c_(653565, _a_(653564, _n_(653563, "pop", lambda: pop), "tolist"))
    _l_(653566)
    aux = _n_(653567, "pop", lambda: pop)
    _l_(653568)
    return aux


def moving_pop(population):
    _l_(653616)

    # e c
    rand_item = _n_(653570, "population", lambda: population)[_c_(653576, _a_(653572, _n_(653571, "random", lambda: random), "randrange"), _c_(653575, _n_(653573, "len", lambda: len), _n_(653574, "population", lambda: population)))]
    _l_(653577)
    # print(rand_item)
    direction_arr = [-1, 1]
    _l_(653578)
    direction = _n_(653579, "direction_arr", lambda: direction_arr)[_c_(653585, _a_(653581, _n_(653580, "random", lambda: random), "randrange"), _c_(653584, _n_(653582, "len", lambda: len), _n_(653583, "direction_arr", lambda: direction_arr)))]
    _l_(653586)
    # print(direction)
    new_element = _n_(653587, "rand_item", lambda: rand_item) + _n_(653588, "direction", lambda: direction) * _c_(653592, _a_(653591, _a_(653590, _n_(653589, "np", lambda: np), "random"), "normal"), 0, 0.2)
    _l_(653593)
    if _n_(653594, "new_element", lambda: new_element) > _n_(653595, "b", lambda: b):
        _l_(653602)

        extra = _n_(653596, "new_element", lambda: new_element) - _n_(653597, "b", lambda: b)
        _l_(653598)
        new_element = _n_(653599, "a", lambda: a) + _n_(653600, "extra", lambda: extra)
        _l_(653601)
    if _n_(653603, "new_element", lambda: new_element) < _n_(653604, "a", lambda: a):
        _l_(653613)

        extra = _c_(653608, _n_(653605, "abs", lambda: abs), _n_(653606, "new_element", lambda: new_element) - _n_(653607, "a", lambda: a))
        _l_(653609)
        new_element = _n_(653610, "b", lambda: b) - _n_(653611, "extra", lambda: extra)
        _l_(653612)
    aux = _n_(653614, "new_element", lambda: new_element)
    _l_(653615)
    # print(new_element)
    return aux


def create_moved_pop(population):
    _l_(653632)

    new_population = []
    _l_(653617)
    for x in _c_(653619, _n_(653618, "range", lambda: range), 0, 20):
        _l_(653629)

        new_element = _c_(653622, _n_(653620, "moving_pop", lambda: moving_pop), _n_(653621, "population", lambda: population))
        _l_(653623)
        _c_(653627, _a_(653625, _n_(653624, "new_population", lambda: new_population), "append"), _n_(653626, "new_element", lambda: new_element))
        _l_(653628)
    aux = _n_(653630, "new_population", lambda: new_population)
    _l_(653631)
    # print(new_population)
    return aux


def star_pop(population):
    _l_(653665)

    random_item1 = _n_(653633, "population", lambda: population)[_c_(653639, _a_(653635, _n_(653634, "random", lambda: random), "randrange"), _c_(653638, _n_(653636, "len", lambda: len), _n_(653637, "population", lambda: population)))]
    _l_(653640)
    random_item2 = _n_(653641, "population", lambda: population)[_c_(653647, _a_(653643, _n_(653642, "random", lambda: random), "randrange"), _c_(653646, _n_(653644, "len", lambda: len), _n_(653645, "population", lambda: population)))]
    _l_(653648)
    while _n_(653649, "random_item2", lambda: random_item2) == _n_(653650, "random_item1", lambda: random_item1):
        _l_(653659)

        random_item2 = _n_(653651, "population", lambda: population)[_c_(653657, _a_(653653, _n_(653652, "random", lambda: random), "randrange"), _c_(653656, _n_(653654, "len", lambda: len), _n_(653655, "population", lambda: population)))]
        _l_(653658)
    e_star = (_n_(653660, "random_item1", lambda: random_item1) + _n_(653661, "random_item2", lambda: random_item2))/2
    _l_(653662)
    aux = _n_(653663, "e_star", lambda: e_star)
    _l_(653664)
    return aux


def create_star_pop(population):
    _l_(653681)

    star_population = []
    _l_(653666)
    for x in _c_(653668, _n_(653667, "range", lambda: range), 0, 20):
        _l_(653678)

        new_element = _c_(653671, _n_(653669, "star_pop", lambda: star_pop), _n_(653670, "population", lambda: population))
        _l_(653672)
        _c_(653676, _a_(653674, _n_(653673, "star_population", lambda: star_population), "append"), _n_(653675, "new_element", lambda: new_element))
        _l_(653677)
    aux = _n_(653679, "star_population", lambda: star_population)
    _l_(653680)
    # print(new_population)
    return aux


pop = _c_(653683, _n_(653682, "initial_pop", lambda: initial_pop))
_l_(653684)
_c_(653687, _n_(653685, "print", lambda: print), _n_(653686, "pop", lambda: pop))
_l_(653688)
for i in _c_(653690, _n_(653689, "range", lambda: range), 0, 500):
    _l_(653763)

    moved_pop = _c_(653693, _n_(653691, "create_moved_pop", lambda: create_moved_pop), _n_(653692, "pop", lambda: pop))
    _l_(653694)
    star_pop = _c_(653697, _n_(653695, "create_star_pop", lambda: create_star_pop), _n_(653696, "pop", lambda: pop))
    _l_(653698)
    pop_combined = _c_(653709, _n_(653699, "sorted", lambda: sorted), _c_(653702, _n_(653700, "sorted", lambda: sorted), _n_(653701, "pop", lambda: pop)) + _c_(653705, _n_(653703, "sorted", lambda: sorted), _n_(653704, "moved_pop", lambda: moved_pop)) +                 
_c_(653708, _n_(653706, "sorted", lambda: sorted), _n_(653707, "star_pop", lambda: star_pop)))
    _l_(653710)
    y_array = []
    _l_(653711)
    for x in _c_(653716, _n_(653712, "range", lambda: range), 0, _c_(653715, _n_(653713, "len", lambda: len), _n_(653714, "pop_combined", lambda: pop_combined))):
        _l_(653725)

        _c_(653723, _a_(653718, _n_(653717, "y_array", lambda: y_array), "append"), _c_(653722, _n_(653719, "function", lambda: function), _n_(653720, "pop_combined", lambda: pop_combined)[_n_(653721, "x", lambda: x)]))
        _l_(653724)
    x_y_array = _c_(653731, _n_(653726, "dict", lambda: dict), _c_(653730, _n_(653727, "zip", lambda: zip), _n_(653728, "pop_combined", lambda: pop_combined), _n_(653729, "y_array", lambda: y_array)))
    _l_(653732)

    sorted_x_y_array = _c_(653740, _n_(653733, "sorted", lambda: sorted), _c_(653736, _a_(653735, _n_(653734, "x_y_array", lambda: x_y_array), "items")), key=_c_(653739, _a_(653738, _n_(653737, "operator", lambda: operator), "itemgetter"), 1), reverse=True)
    _l_(653741)
    sorted_x_y_array = _n_(653742, "sorted_x_y_array", lambda: sorted_x_y_array)[0:20]
    _l_(653743)
    _c_(653746, _n_(653744, "print", lambda: print), _n_(653745, "sorted_x_y_array", lambda: sorted_x_y_array))
    _l_(653747)
    _c_(653750, _a_(653749, _n_(653748, "pop", lambda: pop), "clear"))
    _l_(653751)
    for x in _n_(653752, "sorted_x_y_array", lambda: sorted_x_y_array):
        _l_(653758)

        _c_(653756, _a_(653754, _n_(653753, "pop", lambda: pop), "append"), _n_(653755, "x", lambda: x)[0])
        _l_(653757)
    _c_(653761, _n_(653759, "print", lambda: print), _n_(653760, "pop", lambda: pop))
    _l_(653762)