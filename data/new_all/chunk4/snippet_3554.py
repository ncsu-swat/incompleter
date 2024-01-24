# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72254923/python-attributeerror-object-has-no-attribute-pointing-to-constructor-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Employee import Employee
    _l_(644017)

except ImportError:
    pass
try:
    from Student import Student
    _l_(644019)

except ImportError:
    pass
try:
    from CustomExceptions import InvalidAge
    _l_(644021)

except ImportError:
    pass
try:
    from CustomExceptions import InvalidYearsWorked
    _l_(644023)

except ImportError:
    pass
try:
    from CustomExceptions import InvalidUnits
    _l_(644025)

except ImportError:
    pass

# Try/except block
try:
    _l_(644114)

    name = _c_(644027, _n_(644026, "input", lambda: input), "Enter name: ")
    _l_(644028)
    address = _c_(644030, _n_(644029, "input", lambda: input), "Enter address: ")
    _l_(644031)
    age = _c_(644035, _n_(644032, "int", lambda: int), _c_(644034, _n_(644033, "input", lambda: input), "Enter age: "))
    _l_(644036)
    job_skills = _c_(644038, _n_(644037, "input", lambda: input), "Enter job skills: ")
    _l_(644039)
    yrs_worked = _c_(644043, _n_(644040, "float", lambda: float), _c_(644042, _n_(644041, "input", lambda: input), "Enter years worked: "))
    _l_(644044)

    # create an instance of an emplpoyee person
    my_person = _c_(644051, _n_(644045, "Employee", lambda: Employee), _n_(644046, "name", lambda: name), _n_(644047, "address", lambda: address), _n_(644048, "age", lambda: age), _n_(644049, "job_skills", lambda: job_skills), _n_(644050, "yrs_worked", lambda: yrs_worked))
    _l_(644052)

    # invoke the to_string() method and display everything
    _c_(644057, _n_(644053, "print", lambda: print), _c_(644056, _a_(644055, _n_(644054, "my_person", lambda: my_person), "to_string")))
    _l_(644058)

    name = _c_(644060, _n_(644059, "input", lambda: input), "\nEnter name: ")
    _l_(644061)
    address = _c_(644063, _n_(644062, "input", lambda: input), "Enter address: ")
    _l_(644064)
    age = _c_(644068, _n_(644065, "int", lambda: int), _c_(644067, _n_(644066, "input", lambda: input), "Enter age: "))
    _l_(644069)
    major = _c_(644071, _n_(644070, "input", lambda: input), "Enter major: ")
    _l_(644072)
    units_completed = _c_(644076, _n_(644073, "float", lambda: float), _c_(644075, _n_(644074, "input", lambda: input), "Enter units completed: "))
    _l_(644077)

    # create an instance of a student person
    my_person = _c_(644084, _n_(644078, "Student", lambda: Student), _n_(644079, "name", lambda: name), _n_(644080, "address", lambda: address), _n_(644081, "age", lambda: age), _n_(644082, "major", lambda: major), _n_(644083, "units_completed", lambda: units_completed))
    _l_(644085)

    # invoke the to_string() method and display everything
    _c_(644090, _n_(644086, "print", lambda: print), _c_(644089, _a_(644088, _n_(644087, "my_person", lambda: my_person), "to_string")))
    _l_(644091)

# Exception handling, always go from most specific exception to most generic
except _n_(644092, "InvalidAge", lambda: InvalidAge) as e:
    _l_(644097)

    _c_(644095, _n_(644093, "print", lambda: print), "Invalid age: ", _n_(644094, "e", lambda: e))
    _l_(644096)
except _n_(644098, "InvalidYearsWorked", lambda: InvalidYearsWorked) as e:
    _l_(644103)

    _c_(644101, _n_(644099, "print", lambda: print), "Invalid years worked: ", _n_(644100, "e", lambda: e))
    _l_(644102)
except _n_(644104, "InvalidUnits", lambda: InvalidUnits) as e:
    _l_(644113)

    _c_(644107, _n_(644105, "print", lambda: print), "Invalid units completed: ", _n_(644106, "e", lambda: e))
    _l_(644108)

# generic exception
#except Exception as ex:
    _c_(644111, _n_(644109, "print", lambda: print), "Generic exception: ", _n_(644110, "ex", lambda: ex))
    _l_(644112)