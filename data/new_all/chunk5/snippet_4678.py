# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53038121/typeerror-function-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(704471)

except ImportError:
    pass
try:
    from random import randint
    _l_(704473)

except ImportError:
    pass
try:
    import statistics
    _l_(704475)

except ImportError:
    pass
try:
    from scipy import stats
    _l_(704477)

except ImportError:
    pass
try:
    from enum import Enum
    _l_(704479)

except ImportError:
    pass
try:
    import uuid
    _l_(704481)

except ImportError:
    pass


class EmployeeStatus(_n_(704482, "Enum", lambda: Enum)):
    _l_(704488)

    NEW_HIRE = 1
    _l_(704483)
    WORKING = 2
    _l_(704484)
    PROMOTE = 3
    _l_(704485)
    FIRED = 4
    _l_(704486)
    QUIT = 5
    _l_(704487)


class Person(_n_(704489, "object", lambda: object)):
    _l_(704561)

    def __init__(self, is_new_hire = True):
        _l_(704515)

        _n_(704490, "self", lambda: self).person_id = _c_(704493, _a_(704492, _n_(704491, "uuid", lambda: uuid), "uuid4"))
        _l_(704494)
        _n_(704495, "self", lambda: self).performance = 0.
        _l_(704496)
        years_at_work = 0 if _n_(704497, "is_new_hire", lambda: is_new_hire) else _c_(704499, _n_(704498, "randint", lambda: randint), 1, 9)        
        _l_(704500)        
        _n_(704501, "self", lambda: self).status = _a_(704503, _n_(704502, "EmployeeStatus", lambda: EmployeeStatus), "NEW_HIRE") if _n_(704504, "years_at_work", lambda: years_at_work) == 0 else _a_(704506, _n_(704505, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")
        _l_(704507)
        _n_(704508, "self", lambda: self).status_history = [_a_(704510, _n_(704509, "EmployeeStatus", lambda: EmployeeStatus), "WORKING") for year in _c_(704513, _n_(704511, "range", lambda: range), _n_(704512, "years_at_work", lambda: years_at_work))]
        _l_(704514)


    def step(self, status, new_status=_a_(704517, _n_(704516, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")):
        _l_(704531)

        #self.years_at_work += 1
        _n_(704518, "self", lambda: self).status = _n_(704519, "new_status", lambda: new_status)
        _l_(704520)
        _c_(704523, _a_(704522, _n_(704521, "self", lambda: self), "should_quit"))
        _l_(704524)
        _c_(704529, _a_(704527, _a_(704526, _n_(704525, "self", lambda: self), "status_history"), "append"), _n_(704528, "status", lambda: status))        
        _l_(704530)        

    def should_quit(self, status_history):
        _l_(704546)

        if _c_(704536, _a_(704533, _n_(704532, "status_history", lambda: status_history)[-3:], "count"), _a_(704535, _n_(704534, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")) >= 3 and not _a_(704538, _n_(704537, "self", lambda: self), "status") != _a_(704540, _n_(704539, "EmployeeStatus", lambda: EmployeeStatus), "PROMOTE"):
            _l_(704545)

            _n_(704541, "self", lambda: self).status = _a_(704543, _n_(704542, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")
            _l_(704544)


    def calculate_performance(self, universal_cases):
        _l_(704560)

        cases_assigned = _c_(704549, _n_(704547, "random", lambda: random), 1, _n_(704548, "universal_cases", lambda: (universal_cases)))
        _l_(704550)
        cases_won = _c_(704554, _n_(704551, "random", lambda: random), 0, _a_(704553, _n_(704552, "self", lambda: self), "cases_assigned"))
        _l_(704555)
        _n_(704556, "self", lambda: self).performance = _n_(704557, "cases_won", lambda: cases_won)/_n_(704558, "cases_assigned", lambda: cases_assigned)
        _l_(704559)



class Firm(_n_(704562, "object", lambda: object)):
    _l_(704700)

    # constructor: define all the attributes and what need to do when creating an instance
    def __init__(self, market):
        _l_(704579)

        _n_(704563, "self", lambda: self).market = _n_(704564, "market", lambda: market)
        _l_(704565)
        _n_(704566, "self", lambda: self).universal_cases = _c_(704569, _a_(704568, _n_(704567, "random", lambda: random), "gauss"), 100, 10)
        _l_(704570)
        _n_(704571, "self", lambda: self).persons = [_c_(704575, _a_(704574, _a_(704573, _n_(704572, "self", lambda: self), "market"), "get_person_from_market"), False) for i in _c_(704577, _n_(704576, "range", lambda: range), 100)]
        _l_(704578)

    def step(self):
        _l_(704614)

        # 1. work
        for person in _a_(704581, _n_(704580, "self", lambda: self), "persons"):
            _l_(704586)

            _c_(704584, _a_(704583, _n_(704582, "person", lambda: person), "calculate_performance")) # TODO assign cases to person not universal cases (or everyone can do everything)
            _l_(704585) # TODO assign cases to person not universal cases (or everyone can do everything)
        # 2. evaluate
        # TODO promote tied people.
        top_performers = _c_(704589, _a_(704588, _n_(704587, "self", lambda: self), "get_top_performers"))
        _l_(704590)
        for person in _a_(704592, _n_(704591, "self", lambda: self), "persons"):
            _l_(704609)

            if _n_(704593, "person", lambda: person) in _n_(704594, "top_performers", lambda: top_performers):
                _l_(704598)

                new_status = _a_(704596, _n_(704595, "EmployeeStatus", lambda: EmployeeStatus), "PROMOTE")
                _l_(704597)
            _c_(704602, _a_(704600, _n_(704599, "person", lambda: person), "step"), _n_(704601, "new_status", lambda: new_status))
            _l_(704603)
            _c_(704607, _a_(704605, _n_(704604, "self", lambda: self), "should_fire_person"), _n_(704606, "person", lambda: person))
            _l_(704608)
        # 3. hire
        _c_(704612, _a_(704611, _n_(704610, "self", lambda: self), "hire_new_people"))
        _l_(704613)

    def is_top_performer(self, person):
        _l_(704620)

        aux = _n_(704615, "person", lambda: person) in _c_(704618, _a_(704617, _n_(704616, "self", lambda: self), "get_top_performers"))
        _l_(704619)
        return aux

    def get_top_performers(self):
        _l_(704630)

        ranked_persons = _c_(704626, _n_(704621, "sorted", lambda: sorted), _a_(704623, _n_(704622, "self", lambda: self), "persons"), key = lambda x: _a_(704625, _n_(704624, "x", lambda: x), "performance"), reverse= True)
        _l_(704627)
        aux = _n_(704628, "ranked_persons", lambda: ranked_persons)[:10]
        _l_(704629)
        return aux

    def get_bottom_performers(self):
        _l_(704647)

        ranked_persons = _c_(704636, _n_(704631, "sorted", lambda: sorted), _a_(704633, _n_(704632, "self", lambda: self), "persons"), key = lambda x: _a_(704635, _n_(704634, "x", lambda: x), "performance"), reverse= True)
        _l_(704637)
        remaining_people = [_n_(704638, "person", lambda: person) for person in _n_(704639, "ranked_persons", lambda: ranked_persons) if _a_(704641, _n_(704640, "person", lambda: person), "status") != _a_(704643, _n_(704642, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")]
        _l_(704644)
        aux = _n_(704645, "remaining_people", lambda: remaining_people)[-10:]
        _l_(704646)
        return aux

    def should_fire_person(self, person):
        _l_(704664)

        if _n_(704648, "person", lambda: person) in _c_(704651, _a_(704650, _n_(704649, "self", lambda: self), "get_bottom_performers")):
            _l_(704662)

            _n_(704652, "person", lambda: person).status = _a_(704654, _n_(704653, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")
            _l_(704655)
            _a_(704657, _n_(704656, "person", lambda: person), "status_history")[-1] = _a_(704659, _n_(704658, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")
            _l_(704660)
            aux = True
            _l_(704661)
            return aux
        aux = False
        _l_(704663)
        return aux

    def hire_new_people(self):
        _l_(704699)

        n_fired = _c_(704673, _n_(704665, "len", lambda: len), [_n_(704666, "person", lambda: person) for person in _a_(704668, _n_(704667, "self", lambda: self), "persons") if _a_(704670, _n_(704669, "person", lambda: person), "status") == _a_(704672, _n_(704671, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")])
        _l_(704674)
        # remoive fired and quit
        new_persons = [_n_(704675, "person", lambda: person) for person in _a_(704677, _n_(704676, "self", lambda: self), "persons") if _a_(704679, _n_(704678, "person", lambda: person), "status") not in  [_a_(704681, _n_(704680, "EmployeeStatus", lambda: EmployeeStatus), "FIRED"),_a_(704683, _n_(704682, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")] ]
        _l_(704684)
        # hire new
        _c_(704694, _a_(704686, _n_(704685, "new_persons", lambda: new_persons), "extend"), [_c_(704690, _a_(704689, _a_(704688, _n_(704687, "self", lambda: self), "market"), "get_person_from_market")) for i in _c_(704693, _n_(704691, "range", lambda: range), _n_(704692, "n_fired", lambda: n_fired))])
        _l_(704695)
        _n_(704696, "self", lambda: self).persons = _n_(704697, "new_persons", lambda: new_persons)
        _l_(704698)


class Sim(_n_(704701, "object", lambda: object)):
    _l_(704762)

    def __init__(self, n_simulations=100):
        _l_(704714)

        _n_(704702, "self", lambda: self).n_simulations = _n_(704703, "n_simulations", lambda: n_simulations) 
        _l_(704704) 
        _n_(704705, "self", lambda: self).firm = _c_(704708, _n_(704706, "Firm", lambda: Firm), _n_(704707, "self", lambda: self)) #firm object inherits all attributes of Firm class
        _l_(704709) #firm object inherits all attributes of Firm class
        _n_(704710, "self", lambda: self).persons = {0: []}
        _l_(704711)
        _n_(704712, "self", lambda: self).current_simulation = 0 #we are starting at zero simulation
        _l_(704713) #we are starting at zero simulation

    def get_person_from_market(self, persons, person, is_new_hire = True):
        _l_(704733)

        person = _c_(704717, _n_(704715, "Person", lambda: Person), _n_(704716, "is_new_hire", lambda: is_new_hire))
        _l_(704718)
        _c_(704725, _a_(704723, _a_(704720, _n_(704719, "self", lambda: self), "persons")[_a_(704722, _n_(704721, "self", lambda: self), "current_simulation")], "append"), _n_(704724, "person", lambda: person)) #for the persons population marked by [index] of current simulation, append this new person
        _l_(704726) #for the persons population marked by [index] of current simulation, append this new person
        aux = _c_(704731, _n_(704727, "person", lambda: person), _a_(704729, _n_(704728, "self", lambda: self), "firm"), _n_(704730, "is_new_hire", lambda: is_new_hire))
        _l_(704732)
        return aux

    def step(self):
        _l_(704751)

        _n_(704734, "self", lambda: self).current_simulation += 1
        _l_(704735)
        if not _a_(704737, _n_(704736, "self", lambda: self), "current_simulation") in _a_(704739, _n_(704738, "self", lambda: self), "persons"):
            _l_(704745)

            _a_(704741, _n_(704740, "self", lambda: self), "persons")[_a_(704743, _n_(704742, "self", lambda: self), "current_simulation")] = []
            _l_(704744)
        _c_(704749, _a_(704748, _a_(704747, _n_(704746, "self", lambda: self), "firm"), "step"))
        _l_(704750)

    def Run(self):
        _l_(704761)

        for step in _c_(704755, _n_(704752, "range", lambda: range), _a_(704754, _n_(704753, "self", lambda: self), "n_simulations")):
            _l_(704760)

            _c_(704758, _a_(704757, _n_(704756, "self", lambda: self), "step"))
            _l_(704759)


if _n_(704763, "__name__", lambda: __name__) == '__main__':
    _l_(704774)


    aSim = _c_(704765, _n_(704764, "Sim", lambda: Sim), 1)
    _l_(704766)
    _c_(704768, _n_(704767, "print", lambda: print), "simulation starts...")
    _l_(704769)
    _c_(704772, _a_(704771, _n_(704770, "aSim", lambda: aSim), "Run"))                    
    _l_(704773)                    