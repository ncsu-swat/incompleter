# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56414033/python-nameerror-name-is-not-defined-in-bankaccount-example
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BankAccount:
    _l_(662646)

    def __init__(self, FirstName, LastName, AccNum, Balance, CreationYear, CreationMonth, CreationDay):
        _l_(662544)

        _n_(662523, "self", lambda: self).FirstName = _n_(662524, "FirstName", lambda: FirstName)
        _l_(662525)
        _n_(662526, "self", lambda: self).LirstName = _n_(662527, "LirstName", lambda: LirstName)
        _l_(662528)
        _n_(662529, "self", lambda: self).AccNum = _n_(662530, "AccNum", lambda: AccNum)
        _l_(662531)
        _n_(662532, "self", lambda: self).Balance = _n_(662533, "Balance", lambda: Balance)
        _l_(662534)
        _n_(662535, "self", lambda: self).CreationYear = _n_(662536, "CreationYear", lambda: CreationYear)
        _l_(662537)
        _n_(662538, "self", lambda: self).CreationMonth = _n_(662539, "CreationMonth", lambda: CreationMonth)
        _l_(662540)
        _n_(662541, "self", lambda: self).CreationDay = _n_(662542, "CreationDay", lambda: CreationDay)
        _l_(662543)

    def AddAccount(self):
        _l_(662588)

        _n_(662545, "self", lambda: self).FirstName = _c_(662547, _n_(662546, "input", lambda: input), "First Name: ")
        _l_(662548)
        _n_(662549, "self", lambda: self).LastName = _c_(662551, _n_(662550, "input", lambda: input), "Last Name: ")
        _l_(662552)
        _n_(662553, "self", lambda: self).AccNum = _c_(662555, _n_(662554, "input", lambda: input), "Account Number: ")
        _l_(662556)
        _n_(662557, "self", lambda: self).Balance = _c_(662559, _n_(662558, "input", lambda: input), "Balance: ")
        _l_(662560)
        _n_(662561, "self", lambda: self).CreationYear = _c_(662563, _n_(662562, "input", lambda: input), "Creatin Year: ")
        _l_(662564)
        _n_(662565, "self", lambda: self).CreationMonth = _c_(662567, _n_(662566, "input", lambda: input), "Creation Month: ")
        _l_(662568)
        _n_(662569, "self", lambda: self).CreationDay = _c_(662571, _n_(662570, "input", lambda: input), "Creation Day: ")
        _l_(662572)
        aux = _a_(662574, _n_(662573, "self", lambda: self), "FirstName") , _a_(662576, _n_(662575, "self", lambda: self), "LastName") , _a_(662578, _n_(662577, "self", lambda: self), "AccNum") , _a_(662580, _n_(662579, "self", lambda: self), "Balance") , _a_(662582, _n_(662581, "self", lambda: self), "CreationYear") , _a_(662584, _n_(662583, "self", lambda: self), "CreationMonth") , _a_(662586, _n_(662585, "self", lambda: self), "CreationDay")
        _l_(662587)
        return aux


    def Deposit(self):
        _l_(662611)

        amount = _c_(662590, _n_(662589, "input", lambda: input), "How much do you want to Deposit? ")
        _l_(662591)
        _n_(662592, "self", lambda: self).Balance = _c_(662601, _n_(662593, "str", lambda: str), _c_(662596, _n_(662594, "float", lambda: float), _n_(662595, "amount", lambda: amount)) + _c_(662600, _n_(662597, "float", lambda: float), _a_(662599, _n_(662598, "self", lambda: self), "Balance")))
        _l_(662602)
        _c_(662606, _n_(662603, "print", lambda: print), "Balance: ", _a_(662605, _n_(662604, "self", lambda: self), "Balance"))
        _l_(662607)
        aux = _a_(662609, _n_(662608, "self", lambda: self), "Balance")
        _l_(662610)
        return aux

    def Withdrawl(self):
        _l_(662645)

        amount = _c_(662613, _n_(662612, "input", lambda: input), "How much do you want to withdrawl? ")
        _l_(662614)
        if (_c_(662617, _n_(662615, "float", lambda: float), _n_(662616, "amount", lambda: amount)) > _c_(662621, _n_(662618, "float", lambda: float), _a_(662620, _n_(662619, "self", lambda: self), "Balance"))):
            _l_(662641)

            _c_(662623, _n_(662622, "print", lambda: print), "Insufficent Balance.")
            _l_(662624)
        else:
            _n_(662625, "self", lambda: self).Balance = _c_(662634, _n_(662626, "str", lambda: str), _c_(662630, _n_(662627, "float", lambda: float), _a_(662629, _n_(662628, "self", lambda: self), "Balance")) - _c_(662633, _n_(662631, "float", lambda: float), _n_(662632, "amount", lambda: amount)))
            _l_(662635)
            _c_(662639, _n_(662636, "print", lambda: print), "Balance: ", _a_(662638, _n_(662637, "self", lambda: self), "Balance"))
            _l_(662640)
        aux = _a_(662643, _n_(662642, "self", lambda: self), "Balance")
        _l_(662644)
        return aux


x = _c_(662655, _n_(662647, "BankAccount", lambda: BankAccount), _n_(662648, "FirstName", lambda: FirstName), _n_(662649, "LastName", lambda: LastName), _n_(662650, "AccNum", lambda: AccNum), _n_(662651, "Balance", lambda: Balance), _n_(662652, "CreationYear", lambda: CreationYear), _n_(662653, "CreationMonth", lambda: CreationMonth), _n_(662654, "CreationDay", lambda: CreationDay))
_l_(662656)
_c_(662659, _a_(662658, _n_(662657, "x", lambda: x), "AddAccount"))
_l_(662660)