# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53038121/typeerror-function-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(686520)

except ImportError:
    pass
try:
    from random import randint
    _l_(686522)

except ImportError:
    pass
try:
    import statistics
    _l_(686524)

except ImportError:
    pass
try:
    from scipy import stats
    _l_(686526)

except ImportError:
    pass
try:
    from enum import Enum
    _l_(686528)

except ImportError:
    pass
try:
    import uuid
    _l_(686530)

except ImportError:
    pass


class EmployeeStatus(_n_(686531, "Enum", lambda: Enum)):
    _l_(686537)

    NEW_HIRE = 1
    _l_(686532)
    WORKING = 2
    _l_(686533)
    PROMOTE = 3
    _l_(686534)
    FIRED = 4
    _l_(686535)
    QUIT = 5
    _l_(686536)


class Person(_n_(686538, "object", lambda: object)):
    _l_(686610)

    def __init__(self, is_new_hire = True):
        _l_(686564)

        _n_(686539, "self", lambda: self).person_id = _c_(686542, _a_(686541, _n_(686540, "uuid", lambda: uuid), "uuid4"))
        _l_(686543)
        _n_(686544, "self", lambda: self).performance = 0.
        _l_(686545)
        years_at_work = 0 if _n_(686546, "is_new_hire", lambda: is_new_hire) else _c_(686548, _n_(686547, "randint", lambda: randint), 1, 9)        
        _l_(686549)        
        _n_(686550, "self", lambda: self).status = _a_(686552, _n_(686551, "EmployeeStatus", lambda: EmployeeStatus), "NEW_HIRE") if _n_(686553, "years_at_work", lambda: years_at_work) == 0 else _a_(686555, _n_(686554, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")
        _l_(686556)
        _n_(686557, "self", lambda: self).status_history = [_a_(686559, _n_(686558, "EmployeeStatus", lambda: EmployeeStatus), "WORKING") for year in _c_(686562, _n_(686560, "range", lambda: range), _n_(686561, "years_at_work", lambda: years_at_work))]
        _l_(686563)


    def step(self, status, new_status=_a_(686566, _n_(686565, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")):
        _l_(686580)

        #self.years_at_work += 1
        _n_(686567, "self", lambda: self).status = _n_(686568, "new_status", lambda: new_status)
        _l_(686569)
        _c_(686572, _a_(686571, _n_(686570, "self", lambda: self), "should_quit"))
        _l_(686573)
        _c_(686578, _a_(686576, _a_(686575, _n_(686574, "self", lambda: self), "status_history"), "append"), _n_(686577, "status", lambda: status))        
        _l_(686579)        

    def should_quit(self, status_history):
        _l_(686595)

        if _c_(686585, _a_(686582, _n_(686581, "status_history", lambda: status_history)[-3:], "count"), _a_(686584, _n_(686583, "EmployeeStatus", lambda: EmployeeStatus), "WORKING")) >= 3 and not _a_(686587, _n_(686586, "self", lambda: self), "status") != _a_(686589, _n_(686588, "EmployeeStatus", lambda: EmployeeStatus), "PROMOTE"):
            _l_(686594)

            _n_(686590, "self", lambda: self).status = _a_(686592, _n_(686591, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")
            _l_(686593)


    def calculate_performance(self, universal_cases):
        _l_(686609)

        cases_assigned = _c_(686598, _n_(686596, "random", lambda: random), 1, _n_(686597, "universal_cases", lambda: (universal_cases)))
        _l_(686599)
        cases_won = _c_(686603, _n_(686600, "random", lambda: random), 0, _a_(686602, _n_(686601, "self", lambda: self), "cases_assigned"))
        _l_(686604)
        _n_(686605, "self", lambda: self).performance = _n_(686606, "cases_won", lambda: cases_won)/_n_(686607, "cases_assigned", lambda: cases_assigned)
        _l_(686608)



class Firm(_n_(686611, "object", lambda: object)):
    _l_(686749)

    # constructor: define all the attributes and what need to do when creating an instance
    def __init__(self, market):
        _l_(686628)

        _n_(686612, "self", lambda: self).market = _n_(686613, "market", lambda: market)
        _l_(686614)
        _n_(686615, "self", lambda: self).universal_cases = _c_(686618, _a_(686617, _n_(686616, "random", lambda: random), "gauss"), 100, 10)
        _l_(686619)
        _n_(686620, "self", lambda: self).persons = [_c_(686624, _a_(686623, _a_(686622, _n_(686621, "self", lambda: self), "market"), "get_person_from_market"), False) for i in _c_(686626, _n_(686625, "range", lambda: range), 100)]
        _l_(686627)

    def step(self):
        _l_(686663)

        # 1. work
        for person in _a_(686630, _n_(686629, "self", lambda: self), "persons"):
            _l_(686635)

            _c_(686633, _a_(686632, _n_(686631, "person", lambda: person), "calculate_performance")) # TODO assign cases to person not universal cases (or everyone can do everything)
            _l_(686634) # TODO assign cases to person not universal cases (or everyone can do everything)
        # 2. evaluate
        # TODO promote tied people.
        top_performers = _c_(686638, _a_(686637, _n_(686636, "self", lambda: self), "get_top_performers"))
        _l_(686639)
        for person in _a_(686641, _n_(686640, "self", lambda: self), "persons"):
            _l_(686658)

            if _n_(686642, "person", lambda: person) in _n_(686643, "top_performers", lambda: top_performers):
                _l_(686647)

                new_status = _a_(686645, _n_(686644, "EmployeeStatus", lambda: EmployeeStatus), "PROMOTE")
                _l_(686646)
            _c_(686651, _a_(686649, _n_(686648, "person", lambda: person), "step"), _n_(686650, "new_status", lambda: new_status))
            _l_(686652)
            _c_(686656, _a_(686654, _n_(686653, "self", lambda: self), "should_fire_person"), _n_(686655, "person", lambda: person))
            _l_(686657)
        # 3. hire
        _c_(686661, _a_(686660, _n_(686659, "self", lambda: self), "hire_new_people"))
        _l_(686662)

    def is_top_performer(self, person):
        _l_(686669)

        aux = _n_(686664, "person", lambda: person) in _c_(686667, _a_(686666, _n_(686665, "self", lambda: self), "get_top_performers"))
        _l_(686668)
        return aux

    def get_top_performers(self):
        _l_(686679)

        ranked_persons = _c_(686675, _n_(686670, "sorted", lambda: sorted), _a_(686672, _n_(686671, "self", lambda: self), "persons"), key = lambda x: _a_(686674, _n_(686673, "x", lambda: x), "performance"), reverse= True)
        _l_(686676)
        aux = _n_(686677, "ranked_persons", lambda: ranked_persons)[:10]
        _l_(686678)
        return aux

    def get_bottom_performers(self):
        _l_(686696)

        ranked_persons = _c_(686685, _n_(686680, "sorted", lambda: sorted), _a_(686682, _n_(686681, "self", lambda: self), "persons"), key = lambda x: _a_(686684, _n_(686683, "x", lambda: x), "performance"), reverse= True)
        _l_(686686)
        remaining_people = [_n_(686687, "person", lambda: person) for person in _n_(686688, "ranked_persons", lambda: ranked_persons) if _a_(686690, _n_(686689, "person", lambda: person), "status") != _a_(686692, _n_(686691, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")]
        _l_(686693)
        aux = _n_(686694, "remaining_people", lambda: remaining_people)[-10:]
        _l_(686695)
        return aux

    def should_fire_person(self, person):
        _l_(686713)

        if _n_(686697, "person", lambda: person) in _c_(686700, _a_(686699, _n_(686698, "self", lambda: self), "get_bottom_performers")):
            _l_(686711)

            _n_(686701, "person", lambda: person).status = _a_(686703, _n_(686702, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")
            _l_(686704)
            _a_(686706, _n_(686705, "person", lambda: person), "status_history")[-1] = _a_(686708, _n_(686707, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")
            _l_(686709)
            aux = True
            _l_(686710)
            return aux
        aux = False
        _l_(686712)
        return aux

    def hire_new_people(self):
        _l_(686748)

        n_fired = _c_(686722, _n_(686714, "len", lambda: len), [_n_(686715, "person", lambda: person) for person in _a_(686717, _n_(686716, "self", lambda: self), "persons") if _a_(686719, _n_(686718, "person", lambda: person), "status") == _a_(686721, _n_(686720, "EmployeeStatus", lambda: EmployeeStatus), "FIRED")])
        _l_(686723)
        # remoive fired and quit
        new_persons = [_n_(686724, "person", lambda: person) for person in _a_(686726, _n_(686725, "self", lambda: self), "persons") if _a_(686728, _n_(686727, "person", lambda: person), "status") not in  [_a_(686730, _n_(686729, "EmployeeStatus", lambda: EmployeeStatus), "FIRED"),_a_(686732, _n_(686731, "EmployeeStatus", lambda: EmployeeStatus), "QUIT")] ]
        _l_(686733)
        # hire new
        _c_(686743, _a_(686735, _n_(686734, "new_persons", lambda: new_persons), "extend"), [_c_(686739, _a_(686738, _a_(686737, _n_(686736, "self", lambda: self), "market"), "get_person_from_market")) for i in _c_(686742, _n_(686740, "range", lambda: range), _n_(686741, "n_fired", lambda: n_fired))])
        _l_(686744)
        _n_(686745, "self", lambda: self).persons = _n_(686746, "new_persons", lambda: new_persons)
        _l_(686747)


class Sim(_n_(686750, "object", lambda: object)):
    _l_(686811)

    def __init__(self, n_simulations=100):
        _l_(686763)

        _n_(686751, "self", lambda: self).n_simulations = _n_(686752, "n_simulations", lambda: n_simulations) 
        _l_(686753) 
        _n_(686754, "self", lambda: self).firm = _c_(686757, _n_(686755, "Firm", lambda: Firm), _n_(686756, "self", lambda: self)) #firm object inherits all attributes of Firm class
        _l_(686758) #firm object inherits all attributes of Firm class
        _n_(686759, "self", lambda: self).persons = {0: []}
        _l_(686760)
        _n_(686761, "self", lambda: self).current_simulation = 0 #we are starting at zero simulation
        _l_(686762) #we are starting at zero simulation

    def get_person_from_market(self, persons, person, is_new_hire = True):
        _l_(686782)

        person = _c_(686766, _n_(686764, "Person", lambda: Person), _n_(686765, "is_new_hire", lambda: is_new_hire))
        _l_(686767)
        _c_(686774, _a_(686772, _a_(686769, _n_(686768, "self", lambda: self), "persons")[_a_(686771, _n_(686770, "self", lambda: self), "current_simulation")], "append"), _n_(686773, "person", lambda: person)) #for the persons population marked by [index] of current simulation, append this new person
        _l_(686775) #for the persons population marked by [index] of current simulation, append this new person
        aux = _c_(686780, _n_(686776, "person", lambda: person), _a_(686778, _n_(686777, "self", lambda: self), "firm"), _n_(686779, "is_new_hire", lambda: is_new_hire))
        _l_(686781)
        return aux

    def step(self):
        _l_(686800)

        _n_(686783, "self", lambda: self).current_simulation += 1
        _l_(686784)
        if not _a_(686786, _n_(686785, "self", lambda: self), "current_simulation") in _a_(686788, _n_(686787, "self", lambda: self), "persons"):
            _l_(686794)

            _a_(686790, _n_(686789, "self", lambda: self), "persons")[_a_(686792, _n_(686791, "self", lambda: self), "current_simulation")] = []
            _l_(686793)
        _c_(686798, _a_(686797, _a_(686796, _n_(686795, "self", lambda: self), "firm"), "step"))
        _l_(686799)

    def Run(self):
        _l_(686810)

        for step in _c_(686804, _n_(686801, "range", lambda: range), _a_(686803, _n_(686802, "self", lambda: self), "n_simulations")):
            _l_(686809)

            _c_(686807, _a_(686806, _n_(686805, "self", lambda: self), "step"))
            _l_(686808)


if _n_(686812, "__name__", lambda: __name__) == '__main__':
    _l_(686823)


    aSim = _c_(686814, _n_(686813, "Sim", lambda: Sim), 1)
    _l_(686815)
    _c_(686817, _n_(686816, "print", lambda: print), "simulation starts...")
    _l_(686818)
    _c_(686821, _a_(686820, _n_(686819, "aSim", lambda: aSim), "Run"))                    
    _l_(686822)                    