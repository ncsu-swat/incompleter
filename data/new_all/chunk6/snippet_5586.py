# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63975849/code-shows-type-error-must-be-str-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Account:
  _l_(375132)

  def __init__(self,balance):
    _l_(375127)

    _n_(375124, "self", lambda: self)._balance = _n_(375125, "balance", lambda: balance)
    _l_(375126)
  def getBalance(self):
    _l_(375131)

    aux = _a_(375129, _n_(375128, "self", lambda: self), "_balance")
    _l_(375130)
    return aux

class CheckingAccount(_n_(375133, "Account", lambda: Account)):
  _l_(375152)

  numberOfAccount = 0
  _l_(375134)
  
  def __init__(self,balance=0):
    _l_(375145)

    _n_(375135, "self", lambda: self).balance = _n_(375136, "balance", lambda: balance) 
    _l_(375137) 
    _c_(375141, _a_(375139, _n_(375138, "super", lambda: super)(), "__init__"), _n_(375140, "balance", lambda: balance))
    _l_(375142)
    _n_(375143, "CheckingAccount", lambda: CheckingAccount).numberOfAccount =+ 1
    _l_(375144)
  
  def __str__(self):
    _l_(375151)

    aux = 'Account Balance: '+_c_(375149, _n_(375146, "str", lambda: str), _a_(375148, _n_(375147, "self", lambda: self), "balance")) 
    _l_(375150) 
    return aux 

_c_(375156, _n_(375153, "print", lambda: print), 'Number of Checking Accounts: '+_a_(375155, _n_(375154, "CheckingAccount", lambda: CheckingAccount), "numberOfAccount"))
_l_(375157)
_c_(375161, _n_(375158, "print", lambda: print), _c_(375160, _n_(375159, "CheckingAccount", lambda: CheckingAccount)))
_l_(375162)
_c_(375166, _n_(375163, "print", lambda: print), _c_(375165, _n_(375164, "CheckingAccount", lambda: CheckingAccount), 100.00))
_l_(375167)
_c_(375171, _n_(375168, "print", lambda: print), _c_(375170, _n_(375169, "CheckingAccount", lambda: CheckingAccount), 200.00))
_l_(375172)
_c_(375176, _n_(375173, "print", lambda: print), 'Number of Checking Accounts: '+_a_(375175, _n_(375174, "CheckingAccount", lambda: CheckingAccount), "numberOfAccount"))
_l_(375177)