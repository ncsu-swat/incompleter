# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53038121/typeerror-function-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(680671)

except ImportError:
    pass
try:
    from random import randint
    _l_(680673)

except ImportError:
    pass
try:
    import statistics
    _l_(680675)

except ImportError:
    pass
try:
    from scipy import stats
    _l_(680677)

except ImportError:
    pass
try:
    from enum import Enum
    _l_(680679)

except ImportError:
    pass
try:
    import uuid
    _l_(680681)

except ImportError:
    pass


class EmployeeStatus(_n_(680682, "Enum", lambda: Enum)):
    _l_(680688)

    NEW_HIRE = 1
    _l_(680683)
    WORKING = 2
    _l_(680684)
    PROMOTE = 3
    _l_(680685)
    FIRED = 4
    _l_(680686)
    QUIT = 5
    _l_(680687)


class Person(_n_(680689, "object", lambda: object)):
    _l_(680761)

    def __init__(self, is_new_hire = True):
        _l_(680715)

        _n_(680690, "self", lambda: self).person_id = _c_(680693, _a_(680692, _n_(680691, "uuid", lambda: uuid), "uuid4"))
        _l_(680694)
        _n_(680695, "self", lambda: self).performance = 0.
        _l_(680696)
        years_at_work = 0 if _n_(680697, "is_new_hire", lambda: is_new_hire) else _c_(680699, _n_(680698, "randint", lambda: randint), 1, 9)        
        _l_(680700)        
        _n_(680701, "self", lambda: self).status = _a_(680703, _n_(680702, "EmployeeStatus", lambda: EmployeeStatus), "NEW_HIRE") if _n_(680704, "years_at_work", lambda: years_at_work) == 0 else _a_(680706, _n_(680705, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")
        _l_(680707)
        _n_(680708, "self", lambda: self).status_history = [_a_(680710, _n_(680709, "EmployeeStatus", lambda: EmployeeStatus), "WORKING") for year in _c_(680713, _n_(680711, "range", lambda: range), _n_(680712, "years_at_work", lambda: years_at_work))]
        _l_(680714)


    def step(self, status, new_status=_a_(680717, _n_(680716, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")):
        _l_(680731)

        #self.years_at_work += 1
        _n_(680718, "self", lambda: self).status = _n_(680719, "new_status", lambda: new_status)
        _l_(680720)
        _c_(680723, _a_(680722, _n_(680721, "self", lambda: self), "should_quit"))
        _l_(680724)
        _c_(680729, _a_(680727, _a_(680726, _n_(680725, "self", lambda: self), "status_history"), "append"), _n_(680728, "status", lambda: status))        
        _l_(680730)        

    def should_quit(self, status_history):
        _l_(680746)

        if _c_(680736, _a_(680733, _n_(680732, "status_history", lambda: status_history)[-3:], "count"), _a_(680735, _n_(680734, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")) >= 3 and not _a_(680738, _n_(680737, "self", lambda: self), "status") != _a_(680740, _n_(680739, "EmployeeStatus", lambda: EmployeeStatus), "PROMOTE"):
            _l_(680745)

            _n_(680741, "self", lambda: self).status = _a_(680743, _n_(680742, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")
            _l_(680744)


    def calculate_performance(self, universal_cases):
        _l_(680760)

        cases_assigned = _c_(680749, _n_(680747, "random", lambda: random), 1, _n_(680748, "universal_cases", lambda: (universal_cases)))
        _l_(680750)
        cases_won = _c_(680754, _n_(680751, "random", lambda: random), 0, _a_(680753, _n_(680752, "self", lambda: self), "cases_assigned"))
        _l_(680755)
        _n_(680756, "self", lambda: self).performance = _n_(680757, "cases_won", lambda: cases_won)/_n_(680758, "cases_assigned", lambda: cases_assigned)
        _l_(680759)



class Firm(_n_(680762, "object", lambda: object)):
    _l_(680900)

    # constructor: define all the attributes and what need to do when creating an instance
    def __init__(self, market):
        _l_(680779)

        _n_(680763, "self", lambda: self).market = _n_(680764, "market", lambda: market)
        _l_(680765)
        _n_(680766, "self", lambda: self).universal_cases = _c_(680769, _a_(680768, _n_(680767, "random", lambda: random), "gauss"), 100, 10)
        _l_(680770)
        _n_(680771, "self", lambda: self).persons = [_c_(680775, _a_(680774, _a_(680773, _n_(680772, "self", lambda: self), "market"), "get_person_from_market"), False) for i in _c_(680777, _n_(680776, "range", lambda: range), 100)]
        _l_(680778)

    def step(self):
        _l_(680814)

        # 1. work
        for person in _a_(680781, _n_(680780, "self", lambda: self), "persons"):
            _l_(680786)

            _c_(680784, _a_(680783, _n_(680782, "person", lambda: person), "calculate_performance")) # TODO assign cases to person not universal cases (or everyone can do everything)
            _l_(680785) # TODO assign cases to person not universal cases (or everyone can do everything)
        # 2. evaluate
        # TODO promote tied people.
        top_performers = _c_(680789, _a_(680788, _n_(680787, "self", lambda: self), "get_top_performers"))
        _l_(680790)
        for person in _a_(680792, _n_(680791, "self", lambda: self), "persons"):
            _l_(680809)

            if _n_(680793, "person", lambda: person) in _n_(680794, "top_performers", lambda: top_performers):
                _l_(680798)

                new_status = _a_(680796, _n_(680795, "EmployeeStatus", lambda: EmployeeStatus), "PROMOTE")
                _l_(680797)
            _c_(680802, _a_(680800, _n_(680799, "person", lambda: person), "step"), _n_(680801, "new_status", lambda: new_status))
            _l_(680803)
            _c_(680807, _a_(680805, _n_(680804, "self", lambda: self), "should_fire_person"), _n_(680806, "person", lambda: person))
            _l_(680808)
        # 3. hire
        _c_(680812, _a_(680811, _n_(680810, "self", lambda: self), "hire_new_people"))
        _l_(680813)

    def is_top_performer(self, person):
        _l_(680820)

        aux = _n_(680815, "person", lambda: person) in _c_(680818, _a_(680817, _n_(680816, "self", lambda: self), "get_top_performers"))
        _l_(680819)
        return aux

    def get_top_performers(self):
        _l_(680830)

        ranked_persons = _c_(680826, _n_(680821, "sorted", lambda: sorted), _a_(680823, _n_(680822, "self", lambda: self), "persons"), key = lambda x: _a_(680825, _n_(680824, "x", lambda: x), "performance"), reverse= True)
        _l_(680827)
        aux = _n_(680828, "ranked_persons", lambda: ranked_persons)[:10]
        _l_(680829)
        return aux

    def get_bottom_performers(self):
        _l_(680847)

        ranked_persons = _c_(680836, _n_(680831, "sorted", lambda: sorted), _a_(680833, _n_(680832, "self", lambda: self), "persons"), key = lambda x: _a_(680835, _n_(680834, "x", lambda: x), "performance"), reverse= True)
        _l_(680837)
        remaining_people = [_n_(680838, "person", lambda: person) for person in _n_(680839, "ranked_persons", lambda: ranked_persons) if _a_(680841, _n_(680840, "person", lambda: person), "status") != _a_(680843, _n_(680842, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")]
        _l_(680844)
        aux = _n_(680845, "remaining_people", lambda: remaining_people)[-10:]
        _l_(680846)
        return aux

    def should_fire_person(self, person):
        _l_(680864)

        if _n_(680848, "person", lambda: person) in _c_(680851, _a_(680850, _n_(680849, "self", lambda: self), "get_bottom_performers")):
            _l_(680862)

            _n_(680852, "person", lambda: person).status = _a_(680854, _n_(680853, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")
            _l_(680855)
            _a_(680857, _n_(680856, "person", lambda: person), "status_history")[-1] = _a_(680859, _n_(680858, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")
            _l_(680860)
            aux = True
            _l_(680861)
            return aux
        aux = False
        _l_(680863)
        return aux

    def hire_new_people(self):
        _l_(680899)

        n_fired = _c_(680873, _n_(680865, "len", lambda: len), [_n_(680866, "person", lambda: person) for person in _a_(680868, _n_(680867, "self", lambda: self), "persons") if _a_(680870, _n_(680869, "person", lambda: person), "status") == _a_(680872, _n_(680871, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")])
        _l_(680874)
        # remoive fired and quit
        new_persons = [_n_(680875, "person", lambda: person) for person in _a_(680877, _n_(680876, "self", lambda: self), "persons") if _a_(680879, _n_(680878, "person", lambda: person), "status") not in  [_a_(680881, _n_(680880, "EmployeeStatus", lambda: EmployeeStatus), "FIRED"),_a_(680883, _n_(680882, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")] ]
        _l_(680884)
        # hire new
        _c_(680894, _a_(680886, _n_(680885, "new_persons", lambda: new_persons), "extend"), [_c_(680890, _a_(680889, _a_(680888, _n_(680887, "self", lambda: self), "market"), "get_person_from_market")) for i in _c_(680893, _n_(680891, "range", lambda: range), _n_(680892, "n_fired", lambda: n_fired))])
        _l_(680895)
        _n_(680896, "self", lambda: self).persons = _n_(680897, "new_persons", lambda: new_persons)
        _l_(680898)


class Sim(_n_(680901, "object", lambda: object)):
    _l_(680962)

    def __init__(self, n_simulations=100):
        _l_(680914)

        _n_(680902, "self", lambda: self).n_simulations = _n_(680903, "n_simulations", lambda: n_simulations) 
        _l_(680904) 
        _n_(680905, "self", lambda: self).firm = _c_(680908, _n_(680906, "Firm", lambda: Firm), _n_(680907, "self", lambda: self)) #firm object inherits all attributes of Firm class
        _l_(680909) #firm object inherits all attributes of Firm class
        _n_(680910, "self", lambda: self).persons = {0: []}
        _l_(680911)
        _n_(680912, "self", lambda: self).current_simulation = 0 #we are starting at zero simulation
        _l_(680913) #we are starting at zero simulation

    def get_person_from_market(self, persons, person, is_new_hire = True):
        _l_(680933)

        person = _c_(680917, _n_(680915, "Person", lambda: Person), _n_(680916, "is_new_hire", lambda: is_new_hire))
        _l_(680918)
        _c_(680925, _a_(680923, _a_(680920, _n_(680919, "self", lambda: self), "persons")[_a_(680922, _n_(680921, "self", lambda: self), "current_simulation")], "append"), _n_(680924, "person", lambda: person)) #for the persons population marked by [index] of current simulation, append this new person
        _l_(680926) #for the persons population marked by [index] of current simulation, append this new person
        aux = _c_(680931, _n_(680927, "person", lambda: person), _a_(680929, _n_(680928, "self", lambda: self), "firm"), _n_(680930, "is_new_hire", lambda: is_new_hire))
        _l_(680932)
        return aux

    def step(self):
        _l_(680951)

        _n_(680934, "self", lambda: self).current_simulation += 1
        _l_(680935)
        if not _a_(680937, _n_(680936, "self", lambda: self), "current_simulation") in _a_(680939, _n_(680938, "self", lambda: self), "persons"):
            _l_(680945)

            _a_(680941, _n_(680940, "self", lambda: self), "persons")[_a_(680943, _n_(680942, "self", lambda: self), "current_simulation")] = []
            _l_(680944)
        _c_(680949, _a_(680948, _a_(680947, _n_(680946, "self", lambda: self), "firm"), "step"))
        _l_(680950)

    def Run(self):
        _l_(680961)

        for step in _c_(680955, _n_(680952, "range", lambda: range), _a_(680954, _n_(680953, "self", lambda: self), "n_simulations")):
            _l_(680960)

            _c_(680958, _a_(680957, _n_(680956, "self", lambda: self), "step"))
            _l_(680959)


if _n_(680963, "__name__", lambda: __name__) == '__main__':
    _l_(680974)


    aSim = _c_(680965, _n_(680964, "Sim", lambda: Sim), 1)
    _l_(680966)
    _c_(680968, _n_(680967, "print", lambda: print), "simulation starts...")
    _l_(680969)
    _c_(680972, _a_(680971, _n_(680970, "aSim", lambda: aSim), "Run"))                    
    _l_(680973)                    