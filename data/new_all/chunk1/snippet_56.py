# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43477958/typeerror-not-supported-between-instances-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(419663)

except ImportError:
    pass


class part():
    _l_(419681)

    def __init__(self, number):
        _l_(419669)

        _n_(419664, "self", lambda: self).number = _n_(419665, "number", lambda: number)
        _l_(419666)
        _n_(419667, "self", lambda: self).machine_sequence = []
        _l_(419668)

    def add_volume(self, volume):
        _l_(419673)

        _n_(419670, "self", lambda: self).volume = _n_(419671, "volume", lambda: volume)
        _l_(419672)

    def add_machine(self, machine_numbers):
        _l_(419680)

        _c_(419678, _a_(419676, _a_(419675, _n_(419674, "self", lambda: self), "machine_sequence"), "append"), _n_(419677, "machine_numbers", lambda: machine_numbers))
        _l_(419679)


def create_initial_population():
    _l_(419721)

    part_family = []
    _l_(419682)

    for i in _c_(419684, _n_(419683, "range", lambda: range), 8):
        _l_(419692)

        _c_(419690, _a_(419686, _n_(419685, "part_family", lambda: part_family), "append"), _c_(419689, _n_(419687, "part", lambda: part), _n_(419688, "i", lambda: i)))
        _l_(419691)

    part_population = []
    _l_(419693)

    for i in _c_(419695, _n_(419694, "range", lambda: range), 6):
        _l_(419707)

        _c_(419705, _a_(419697, _n_(419696, "part_population", lambda: part_population), "append"), _c_(419704, _a_(419699, _n_(419698, "random", lambda: random), "sample"), _n_(419700, "part_family", lambda: part_family), _c_(419703, _n_(419701, "len", lambda: len), _n_(419702, "part_family", lambda: part_family))))
        _l_(419706)

    for i in _n_(419708, "part_population", lambda: part_population):
        _l_(419718)

        for j in _n_(419709, "i", lambda: i):
            _l_(419717)

            _c_(419715, _a_(419711, _n_(419710, "j", lambda: j), "add_volume"), _c_(419714, _a_(419713, _n_(419712, "random", lambda: random), "randrange"), 100, 200))
            _l_(419716)
    aux = _n_(419719, "part_population", lambda: part_population)
    _l_(419720)

    return aux


def fitness(part_family):
    _l_(419761)

    sum_of_boundary = []
    _l_(419722)
    for i in _c_(419724, _n_(419723, "range", lambda: range), 0, 8, 2):
        _l_(419736)

        _c_(419734, _a_(419726, _n_(419725, "sum_of_boundary", lambda: sum_of_boundary), "append"), _c_(419733, _n_(419727, "sum", lambda: sum), (_a_(419729, _n_(419728, "j", lambda: j), "volume") for j in _n_(419730, "part_family", lambda: part_family)[_n_(419731, "i", lambda: i):_n_(419732, "i", lambda: i) + 2])))
        _l_(419735)

    fitness_value = 0
    _l_(419737)

    for i in _c_(419742, _n_(419738, "range", lambda: range), _c_(419741, _n_(419739, "len", lambda: len), _n_(419740, "sum_of_boundary", lambda: sum_of_boundary)) - 1):
        _l_(419758)

        for j in _c_(419748, _n_(419743, "range", lambda: range), _n_(419744, "i", lambda: i) + 1, _c_(419747, _n_(419745, "len", lambda: len), _n_(419746, "sum_of_boundary", lambda: sum_of_boundary))):
            _l_(419757)

            fitness_value = _n_(419749, "fitness_value", lambda: fitness_value) + _c_(419755, _n_(419750, "abs", lambda: abs), _n_(419751, "sum_of_boundary", lambda: sum_of_boundary)[_n_(419752, "i", lambda: i)] - _n_(419753, "sum_of_boundary", lambda: sum_of_boundary)[_n_(419754, "j", lambda: j)])
            _l_(419756)
    aux = _n_(419759, "fitness_value", lambda: fitness_value)
    _l_(419760)

    return aux


def sort_population_by_fitness(population):
    _l_(419787)

    pre_sorted = [[_c_(419764, _n_(419762, "fitness", lambda: fitness), _n_(419763, "x", lambda: x)),_n_(419765, "x", lambda: x)] for x in _n_(419766, "population", lambda: population)]
    _l_(419767)
    sort = [_n_(419768, "x", lambda: x)[1] for x in _c_(419771, _n_(419769, "sorted", lambda: sorted), _n_(419770, "pre_sorted", lambda: pre_sorted))]
    _l_(419772)
    for i in _n_(419773, "sort", lambda: sort):
        _l_(419784)

        for j in _n_(419774, "i", lambda: i):
            _l_(419780)

            _c_(419778, _n_(419775, "print", lambda: print), _a_(419777, _n_(419776, "j", lambda: j), "volume"), end = ' ')
            _l_(419779)
        _c_(419782, _n_(419781, "print", lambda: print))
        _l_(419783)
    aux = _n_(419785, "sort", lambda: sort)
    _l_(419786)

    return aux


def evolve(population):
    _l_(419794)

    population = _c_(419790, _n_(419788, "sort_population_by_fitness", lambda: sort_population_by_fitness), _n_(419789, "population", lambda: population))
    _l_(419791)
    aux = _n_(419792, "population", lambda: population)
    _l_(419793)
    return aux


population = _c_(419796, _n_(419795, "create_initial_population", lambda: create_initial_population))
_l_(419797)
population = _c_(419800, _n_(419798, "evolve", lambda: evolve), _n_(419799, "population", lambda: population))
_l_(419801)