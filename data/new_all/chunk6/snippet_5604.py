# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63975849/code-shows-type-error-must-be-str-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Account:
  _l_(338523)

  def __init__(self,balance):
    _l_(338518)

    _n_(338515, "self", lambda: self)._balance = _n_(338516, "balance", lambda: balance)
    _l_(338517)
  def getBalance(self):
    _l_(338522)

    aux = _a_(338520, _n_(338519, "self", lambda: self), "_balance")
    _l_(338521)
    return aux

class CheckingAccount(_n_(338524, "Account", lambda: Account)):
  _l_(338543)

  numberOfAccount = 0
  _l_(338525)
  
  def __init__(self,balance=0):
    _l_(338536)

    _n_(338526, "self", lambda: self).balance = _n_(338527, "balance", lambda: balance) 
    _l_(338528) 
    _c_(338532, _a_(338530, _n_(338529, "super", lambda: super)(), "__init__"), _n_(338531, "balance", lambda: balance))
    _l_(338533)
    _n_(338534, "CheckingAccount", lambda: CheckingAccount).numberOfAccount =+ 1
    _l_(338535)
  
  def __str__(self):
    _l_(338542)

    aux = 'Account Balance: '+_c_(338540, _n_(338537, "str", lambda: str), _a_(338539, _n_(338538, "self", lambda: self), "balance")) 
    _l_(338541) 
    return aux 

_c_(338547, _n_(338544, "print", lambda: print), 'Number of Checking Accounts: '+_a_(338546, _n_(338545, "CheckingAccount", lambda: CheckingAccount), "numberOfAccount"))
_l_(338548)
_c_(338552, _n_(338549, "print", lambda: print), _c_(338551, _n_(338550, "CheckingAccount", lambda: CheckingAccount)))
_l_(338553)
_c_(338557, _n_(338554, "print", lambda: print), _c_(338556, _n_(338555, "CheckingAccount", lambda: CheckingAccount), 100.00))
_l_(338558)
_c_(338562, _n_(338559, "print", lambda: print), _c_(338561, _n_(338560, "CheckingAccount", lambda: CheckingAccount), 200.00))
_l_(338563)
_c_(338567, _n_(338564, "print", lambda: print), 'Number of Checking Accounts: '+_a_(338566, _n_(338565, "CheckingAccount", lambda: CheckingAccount), "numberOfAccount"))
_l_(338568)