# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48721067/global-variable-in-python-getting-nameerror-while-performing-a-comparison
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.sax
    _l_(647128)

except ImportError:
    pass

class Employee :
    _l_(647133)

    def __init__(self, id):
        _l_(647132)

        _n_(647129, "self", lambda: self).id = _n_(647130, "id", lambda: id)
        _l_(647131)


class EmployeeHandler(_a_(647135, _a_(647134, xml, "sax"), "ContentHandler")):
    _l_(647221)


    emp = None
    _l_(647136)
    emplist = []
    _l_(647137)
    fName = False
    _l_(647138)
    lName = False
    _l_(647139)
    age = False
    _l_(647140)
    company = False
    _l_(647141)

    def __init__(self):
        _l_(647148)

        _c_(647146, _a_(647144, _a_(647143, _a_(647142, xml, "sax"), "ContentHandler"), "__init__"), _n_(647145, "self", lambda: self))
        _l_(647147)

    def startElement(self, name, attrs):
        _l_(647182)

        _c_(647151, _n_(647149, "print", lambda: print), "startElement '" + _n_(647150, "name", lambda: name) + "'")
        _l_(647152)

        if _n_(647153, "name", lambda: name) == "Employees" :
            _l_(647156)

            global emplist
            _l_(647154)
            emplist = []
            _l_(647155)

        if _n_(647157, "name", lambda: name) == "Employee":
            _l_(647181)

            global emp
            _l_(647158)
            emp = _c_(647163, _n_(647159, "Employee", lambda: Employee), _c_(647162, _a_(647161, _n_(647160, "attrs", lambda: attrs), "getValue"), "id"))
            _l_(647164)
        elif _n_(647165, "name", lambda: name) == "FirstName":
            _l_(647180)

            global fName
            _l_(647166)
            fName = True
            _l_(647167)
        elif _n_(647168, "name", lambda: name) == "LastName":
            _l_(647179)

            global lName
            _l_(647169)
            lName = True
            _l_(647170)
        elif _n_(647171, "name", lambda: name) == "Age":
            _l_(647178)

            global age
            _l_(647172)
            age = True
            _l_(647173)
        elif _n_(647174, "name", lambda: name) == "Company":
            _l_(647177)

            global company
            _l_(647175)
            company = True
            _l_(647176)

    def characters(self, content):
        _l_(647208)

        _c_(647185, _n_(647183, "print", lambda: print), "characters '" + _n_(647184, "content", lambda: content) + "'")
        _l_(647186)
        global fName, lName, age, company
        _l_(647187)
        if _n_(647188, "fName", lambda: fName) is True:
            _l_(647207)

            _n_(647189, "emp", lambda: emp).firstName = _n_(647190, "content", lambda: content)
            _l_(647191)
        elif _n_(647192, "lName", lambda: lName) is True:
            _l_(647206)

            _n_(647193, "emp", lambda: emp).lastName = _n_(647194, "content", lambda: content)
            _l_(647195)
        elif _n_(647196, "age", lambda: age) is True:
            _l_(647205)

            _n_(647197, "emp", lambda: emp).age = _n_(647198, "content", lambda: content)
            _l_(647199)
        elif _n_(647200, "company", lambda: company) is True:
            _l_(647204)

            _n_(647201, "emp", lambda: emp).company = _n_(647202, "content", lambda: content)
            _l_(647203)



    def endElement(self, name):
        _l_(647220)

        _c_(647211, _n_(647209, "print", lambda: print), "endElement '" + _n_(647210, "name", lambda: name) + "'")
        _l_(647212)
        if _n_(647213, "name", lambda: name) == "Employee":
            _l_(647219)

            #global emplist : To use list methods global is not required
            _c_(647217, _a_(647215, _n_(647214, "emplist", lambda: emplist), "append"), _n_(647216, "emp", lambda: emp))
            _l_(647218)


def main(sourceFileName):
    _l_(647233)

    source = _c_(647224, _n_(647222, "open", lambda: open), _n_(647223, "sourceFileName", lambda: sourceFileName))
    _l_(647225)
    _c_(647231, _a_(647227, _a_(647226, xml, "sax"), "parse"), _n_(647228, "source", lambda: source), _c_(647230, _n_(647229, "EmployeeHandler", lambda: EmployeeHandler)))
    _l_(647232)


if _n_(647234, "__name__", lambda: __name__) == "__main__":
    _l_(647245)

    _c_(647236, _n_(647235, "main", lambda: main), "EmployeeData")
    _l_(647237)
    _c_(647243, _n_(647238, "print", lambda: print), "Ids ", _a_(647240, _n_(647239, "emplist", lambda: emplist)[0], "id") , _a_(647242, _n_(647241, "emplist", lambda: emplist)[1], "id"))
    _l_(647244)