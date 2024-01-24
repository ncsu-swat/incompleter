# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48353738/typeerror-descriptor-init-requires-a-super-object-but-received-a-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Employee:
    _l_(416582)

    raise_amount=1.05
    _l_(416536)
    emp_count=0
    _l_(416537)
    def __init__(self,first_name,last_name, amount):
        _l_(416555)

        _n_(416538, "self", lambda: self).first_name=_n_(416539, "first_name", lambda: first_name)
        _l_(416540)
        _n_(416541, "self", lambda: self).last_name=_n_(416542, "last_name", lambda: last_name)
        _l_(416543)
        _n_(416544, "self", lambda: self).amount=_n_(416545, "amount", lambda: amount)
        _l_(416546)
        _n_(416547, "self", lambda: self).email_id=_c_(416551, _a_(416548, "{0}.{1}@{1}.com", "format"), _n_(416549, "first_name", lambda: first_name),_n_(416550, "last_name", lambda: last_name))
        _l_(416552)
        _n_(416553, "Employee", lambda: Employee).emp_count +=1
        _l_(416554)

    def fullname(self):
        _l_(416563)

        _c_(416561, _n_(416556, "print", lambda: print), "%s %s"%(_a_(416558, _n_(416557, "self", lambda: self), "first_name"),_a_(416560, _n_(416559, "self", lambda: self), "last_name")))
        _l_(416562)

    def print1(self):
        _l_(416574)

        _c_(416567, _n_(416564, "print", lambda: print), _a_(416566, _n_(416565, "self", lambda: self), "email"))
        _l_(416568)
        _c_(416572, _n_(416569, "print", lambda: print), "Total no of Employee are :%d" %_a_(416571, _n_(416570, "Employee", lambda: Employee), "emp_count"))
        _l_(416573)


    def raise_amount(self):
        _l_(416581)

        _n_(416575, "self", lambda: self).amount *=_n_(416576, "self", lambda: self).raise_amount
        _l_(416577)
        aux = _a_(416579, _n_(416578, "self", lambda: self), "amount")
        _l_(416580)
        return aux


class Developer(_n_(416583, "Employee", lambda: Employee)):
    _l_(416596)

    raise_amount = 1.10
    _l_(416584)
    def __init__(self,f,l,a,prog):
        _l_(416595)

        _c_(416590, _a_(416586, _n_(416585, "super", lambda: super), "__init__"), _n_(416587, "f", lambda: f),_n_(416588, "l", lambda: l),_n_(416589, "a", lambda: a))
        _l_(416591)
        _n_(416592, "self", lambda: self).programming=_n_(416593, "prog", lambda: prog)
        _l_(416594)

class Manager(_n_(416597, "Employee", lambda: Employee)):
    _l_(416648)

    def __init__(self,f,l,a,emp=None):
        _l_(416612)

        _c_(416603, _a_(416599, _n_(416598, "super", lambda: super), "__init__"), _n_(416600, "f", lambda: f),_n_(416601, "l", lambda: l),_n_(416602, "a", lambda: a))
        _l_(416604)
        if _n_(416605, "emp", lambda: emp) is None:
            _l_(416611)

            _n_(416606, "self", lambda: self).my_employee=[]
            _l_(416607)
        else:
            _n_(416608, "self", lambda: self).my_employee=_n_(416609, "emp", lambda: emp)
            _l_(416610)



    def add_employee(self,emp):
        _l_(416626)

        if _n_(416613, "emp", lambda: emp) in _a_(416615, _n_(416614, "self", lambda: self), "my_employee"):
            _l_(416625)

            _c_(416617, _n_(416616, "print", lambda: print), "employee is already exist")
            _l_(416618)
        else:
            _c_(416623, _a_(416621, _a_(416620, _n_(416619, "self", lambda: self), "my_employee"), "append"), _n_(416622, "emp", lambda: emp))
            _l_(416624)

    def remove_employee(self,emp):
        _l_(416637)

        if _n_(416627, "emp", lambda: emp) in _a_(416629, _n_(416628, "self", lambda: self), "my_employee"):
            _l_(416636)

            _c_(416634, _a_(416632, _a_(416631, _n_(416630, "self", lambda: self), "my_employee"), "remove"), _n_(416633, "emp", lambda: emp))
            _l_(416635)

    def print_employee(self):
        _l_(416647)

        for emp in _a_(416639, _n_(416638, "self", lambda: self), "my_employee"):
            _l_(416646)

            _c_(416644, _n_(416640, "print", lambda: print), _c_(416643, _a_(416642, _n_(416641, "emp", lambda: emp), "fullnamme")))
            _l_(416645)



dev1=_c_(416650, _n_(416649, "Developer", lambda: Developer), "subhendu","panda",500000,"Python")
_l_(416651)
_c_(416654, _a_(416653, _n_(416652, "dev1", lambda: dev1), "raise_amount"))
_l_(416655)
dev2=_c_(416657, _n_(416656, "Developer", lambda: Developer), 'Aditya','bishoyi',5688989,'java')
_l_(416658)
_c_(416661, _a_(416660, _n_(416659, "dev2", lambda: dev2), "fullname"))
_l_(416662)
_c_(416665, _a_(416664, _n_(416663, "dev1", lambda: dev1), "fullname"))
_l_(416666)
emp1=_c_(416668, _n_(416667, "Employee", lambda: Employee), "tonu","trip",30000)
_l_(416669)
_c_(416672, _a_(416671, _n_(416670, "emp1", lambda: emp1), "raise_amount"))
_l_(416673)
_c_(416676, _a_(416675, _n_(416674, "emp1", lambda: emp1), "fullname"))
_l_(416677)
mgr1=_c_(416679, _n_(416678, "Manager", lambda: Manager), "Biplab","choudhury",5000000)
_l_(416680)
_c_(416683, _a_(416682, _n_(416681, "mgr1", lambda: mgr1), "fullname"))
_l_(416684)
_c_(416688, _a_(416686, _n_(416685, "mgr1", lambda: mgr1), "add_employee"), _n_(416687, "dev1", lambda: dev1))
_l_(416689)
_c_(416693, _a_(416691, _n_(416690, "mgr1", lambda: mgr1), "add_employee"), _n_(416692, "emp1", lambda: emp1))
_l_(416694)
_c_(416698, _a_(416696, _n_(416695, "mgr1", lambda: mgr1), "add_employee"), _n_(416697, "dev2", lambda: dev2))
_l_(416699)
_c_(416702, _a_(416701, _n_(416700, "mgr1", lambda: mgr1), "print_employee"))
_l_(416703)
_c_(416707, _a_(416705, _n_(416704, "mgr1", lambda: mgr1), "remove_employee"), _n_(416706, "dev1", lambda: dev1))
_l_(416708)
_c_(416711, _a_(416710, _n_(416709, "mgr1", lambda: mgr1), "print_employee"))
_l_(416712)