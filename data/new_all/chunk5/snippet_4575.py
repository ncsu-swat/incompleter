# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55469766/typeerror-list-object-is-not-callable-problem-with-passing-generated-array
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(690334)

except ImportError:
    pass
try:
    import math
    _l_(690336)

except ImportError:
    pass
try:
    import random
    _l_(690338)

except ImportError:
    pass
try:
    import operator
    _l_(690340)

except ImportError:
    pass

# Global variables
a = 0.1
_l_(690341)
b = 1
_l_(690342)


def function(x):
    _l_(690355)

    aux = (_c_(690348, _a_(690344, _n_(690343, "math", lambda: math), "sin"), 40*_a_(690346, _n_(690345, "math", lambda: math), "pi")*_n_(690347, "x", lambda: x))+_c_(690352, _a_(690350, _n_(690349, "math", lambda: math), "pow"), _n_(690351, "x", lambda: x)-1, 4))/(2*_n_(690353, "x", lambda: x))
    _l_(690354)
    return aux


def initial_pop():
    _l_(690369)

    pop = _c_(690361, _a_(690358, _a_(690357, _n_(690356, "np", lambda: np), "random"), "uniform"), _n_(690359, "a", lambda: a), _n_(690360, "b", lambda: b), 20)
    _l_(690362)
    pop = _c_(690365, _a_(690364, _n_(690363, "pop", lambda: pop), "tolist"))
    _l_(690366)
    aux = _n_(690367, "pop", lambda: pop)
    _l_(690368)
    return aux


def moving_pop(population):
    _l_(690416)

    # e c
    rand_item = _n_(690370, "population", lambda: population)[_c_(690376, _a_(690372, _n_(690371, "random", lambda: random), "randrange"), _c_(690375, _n_(690373, "len", lambda: len), _n_(690374, "population", lambda: population)))]
    _l_(690377)
    # print(rand_item)
    direction_arr = [-1, 1]
    _l_(690378)
    direction = _n_(690379, "direction_arr", lambda: direction_arr)[_c_(690385, _a_(690381, _n_(690380, "random", lambda: random), "randrange"), _c_(690384, _n_(690382, "len", lambda: len), _n_(690383, "direction_arr", lambda: direction_arr)))]
    _l_(690386)
    # print(direction)
    new_element = _n_(690387, "rand_item", lambda: rand_item) + _n_(690388, "direction", lambda: direction) * _c_(690392, _a_(690391, _a_(690390, _n_(690389, "np", lambda: np), "random"), "normal"), 0, 0.2)
    _l_(690393)
    if _n_(690394, "new_element", lambda: new_element) > _n_(690395, "b", lambda: b):
        _l_(690402)

        extra = _n_(690396, "new_element", lambda: new_element) - _n_(690397, "b", lambda: b)
        _l_(690398)
        new_element = _n_(690399, "a", lambda: a) + _n_(690400, "extra", lambda: extra)
        _l_(690401)
    if _n_(690403, "new_element", lambda: new_element) < _n_(690404, "a", lambda: a):
        _l_(690413)

        extra = _c_(690408, _n_(690405, "abs", lambda: abs), _n_(690406, "new_element", lambda: new_element) - _n_(690407, "a", lambda: a))
        _l_(690409)
        new_element = _n_(690410, "b", lambda: b) - _n_(690411, "extra", lambda: extra)
        _l_(690412)
    aux = _n_(690414, "new_element", lambda: new_element)
    _l_(690415)
    # print(new_element)
    return aux


def create_moved_pop(population):
    _l_(690432)

    new_population = []
    _l_(690417)
    for x in _c_(690419, _n_(690418, "range", lambda: range), 0, 20):
        _l_(690429)

        new_element = _c_(690422, _n_(690420, "moving_pop", lambda: moving_pop), _n_(690421, "population", lambda: population))
        _l_(690423)
        _c_(690427, _a_(690425, _n_(690424, "new_population", lambda: new_population), "append"), _n_(690426, "new_element", lambda: new_element))
        _l_(690428)
    aux = _n_(690430, "new_population", lambda: new_population)
    _l_(690431)
    # print(new_population)
    return aux


def star_pop(population):
    _l_(690465)

    random_item1 = _n_(690433, "population", lambda: population)[_c_(690439, _a_(690435, _n_(690434, "random", lambda: random), "randrange"), _c_(690438, _n_(690436, "len", lambda: len), _n_(690437, "population", lambda: population)))]
    _l_(690440)
    random_item2 = _n_(690441, "population", lambda: population)[_c_(690447, _a_(690443, _n_(690442, "random", lambda: random), "randrange"), _c_(690446, _n_(690444, "len", lambda: len), _n_(690445, "population", lambda: population)))]
    _l_(690448)
    while _n_(690449, "random_item2", lambda: random_item2) == _n_(690450, "random_item1", lambda: random_item1):
        _l_(690459)

        random_item2 = _n_(690451, "population", lambda: population)[_c_(690457, _a_(690453, _n_(690452, "random", lambda: random), "randrange"), _c_(690456, _n_(690454, "len", lambda: len), _n_(690455, "population", lambda: population)))]
        _l_(690458)
    e_star = (_n_(690460, "random_item1", lambda: random_item1) + _n_(690461, "random_item2", lambda: random_item2))/2
    _l_(690462)
    aux = _n_(690463, "e_star", lambda: e_star)
    _l_(690464)
    return aux


def create_star_pop(population):
    _l_(690481)

    star_population = []
    _l_(690466)
    for x in _c_(690468, _n_(690467, "range", lambda: range), 0, 20):
        _l_(690478)

        new_element = _c_(690471, _n_(690469, "star_pop", lambda: star_pop), _n_(690470, "population", lambda: population))
        _l_(690472)
        _c_(690476, _a_(690474, _n_(690473, "star_population", lambda: star_population), "append"), _n_(690475, "new_element", lambda: new_element))
        _l_(690477)
    aux = _n_(690479, "star_population", lambda: star_population)
    _l_(690480)
    # print(new_population)
    return aux


pop = _c_(690483, _n_(690482, "initial_pop", lambda: initial_pop))
_l_(690484)
_c_(690487, _n_(690485, "print", lambda: print), _n_(690486, "pop", lambda: pop))
_l_(690488)
for i in _c_(690490, _n_(690489, "range", lambda: range), 0, 500):
    _l_(690563)

    moved_pop = _c_(690493, _n_(690491, "create_moved_pop", lambda: create_moved_pop), _n_(690492, "pop", lambda: pop))
    _l_(690494)
    star_pop = _c_(690497, _n_(690495, "create_star_pop", lambda: create_star_pop), _n_(690496, "pop", lambda: pop))
    _l_(690498)
    pop_combined = _c_(690509, _n_(690499, "sorted", lambda: sorted), _c_(690502, _n_(690500, "sorted", lambda: sorted), _n_(690501, "pop", lambda: pop)) + _c_(690505, _n_(690503, "sorted", lambda: sorted), _n_(690504, "moved_pop", lambda: moved_pop)) +                 
_c_(690508, _n_(690506, "sorted", lambda: sorted), _n_(690507, "star_pop", lambda: star_pop)))
    _l_(690510)
    y_array = []
    _l_(690511)
    for x in _c_(690516, _n_(690512, "range", lambda: range), 0, _c_(690515, _n_(690513, "len", lambda: len), _n_(690514, "pop_combined", lambda: pop_combined))):
        _l_(690525)

        _c_(690523, _a_(690518, _n_(690517, "y_array", lambda: y_array), "append"), _c_(690522, _n_(690519, "function", lambda: function), _n_(690520, "pop_combined", lambda: pop_combined)[_n_(690521, "x", lambda: x)]))
        _l_(690524)
    x_y_array = _c_(690531, _n_(690526, "dict", lambda: dict), _c_(690530, _n_(690527, "zip", lambda: zip), _n_(690528, "pop_combined", lambda: pop_combined), _n_(690529, "y_array", lambda: y_array)))
    _l_(690532)

    sorted_x_y_array = _c_(690540, _n_(690533, "sorted", lambda: sorted), _c_(690536, _a_(690535, _n_(690534, "x_y_array", lambda: x_y_array), "items")), key=_c_(690539, _a_(690538, _n_(690537, "operator", lambda: operator), "itemgetter"), 1), reverse=True)
    _l_(690541)
    sorted_x_y_array = _n_(690542, "sorted_x_y_array", lambda: sorted_x_y_array)[0:20]
    _l_(690543)
    _c_(690546, _n_(690544, "print", lambda: print), _n_(690545, "sorted_x_y_array", lambda: sorted_x_y_array))
    _l_(690547)
    _c_(690550, _a_(690549, _n_(690548, "pop", lambda: pop), "clear"))
    _l_(690551)
    for x in _n_(690552, "sorted_x_y_array", lambda: sorted_x_y_array):
        _l_(690558)

        _c_(690556, _a_(690554, _n_(690553, "pop", lambda: pop), "append"), _n_(690555, "x", lambda: x)[0])
        _l_(690557)
    _c_(690561, _n_(690559, "print", lambda: print), _n_(690560, "pop", lambda: pop))
    _l_(690562)