# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65619742/name-error-while-trying-to-generate-some-report
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def state_from_record(state_name):
    _l_(620193)

    state_split = _c_(620189, _a_(620188, _n_(620187, "state_name", lambda: state_name), "split"), ",")
    _l_(620190)
    aux = _n_(620191, "state_split", lambda: state_split)
    _l_(620192)
    return aux

def cases_from_record(covid_cases):
    _l_(620200)

    covid_split = _c_(620196, _a_(620195, _n_(620194, "covid_cases", lambda: covid_cases), "split"), ",")
    _l_(620197)
    aux = _n_(620198, "covid_split", lambda: covid_split)
    _l_(620199)
    return aux

def deaths_from_record(covid_deaths):
    _l_(620207)

    death_split = _c_(620203, _a_(620202, _n_(620201, "covid_deaths", lambda: covid_deaths), "split"), ",")
    _l_(620204)
    aux = _n_(620205, "death_split", lambda: death_split)
    _l_(620206)
    return aux

result1 = _c_(620210, _n_(620208, "state_from_record", lambda: state_from_record), _n_(620209, "result", lambda: result)[0])
_l_(620211)
_c_(620214, _n_(620212, "print", lambda: print), _n_(620213, "result1", lambda: result1)) 
_l_(620215) 