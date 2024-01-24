# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54479475/how-to-fix-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import uuid
  _l_(373974)

except ImportError:
  pass
try:
  import hashlib
  _l_(373976)

except ImportError:
  pass
login_or_signup = _c_(373978, _n_(373977, "input", lambda: input), "would you like to log in? Or signup?: ")
_l_(373979)

if _c_(373981, _n_(373980, "login_or_signup", lambda: login_or_signup), "signup"):
  _l_(374043)

  def hash_password(password):
    _l_(374000)

    # uuid is used to generate a random number
    salt = _a_(373985, _c_(373984, _a_(373983, _n_(373982, "uuid", lambda: uuid), "uuid4")), "hex")
    _l_(373986)
    aux = _c_(373997, _a_(373996, _c_(373995, _a_(373988, _n_(373987, "hashlib", lambda: hashlib), "sha256"), _c_(373991, _a_(373990, _n_(373989, "salt", lambda: salt), "encode")) + _c_(373994, _a_(373993, _n_(373992, "password", lambda: password), "encode"))), "hexdigest")) + ':' + _n_(373998, "salt", lambda: salt)
    _l_(373999)
    return aux

  def check_password(hashed_password, user_password):
    _l_(374018)

    password, salt = _c_(374003, _a_(374002, _n_(374001, "hashed_password", lambda: hashed_password), "split"), ':')
    _l_(374004)
    aux = _n_(374005, "password", lambda: password) == _c_(374016, _a_(374015, _c_(374014, _a_(374007, _n_(374006, "hashlib", lambda: hashlib), "sha256"), _c_(374010, _a_(374009, _n_(374008, "salt", lambda: salt), "encode")) + _c_(374013, _a_(374012, _n_(374011, "user_password", lambda: user_password), "encode"))), "hexdigest"))
    _l_(374017)
    return aux

  new_pass = _c_(374020, _n_(374019, "input", lambda: input), 'Please enter a password: ')
  _l_(374021)
  hashed_password = _c_(374024, _n_(374022, "hash_password", lambda: hash_password), _n_(374023, "new_pass", lambda: new_pass))
  _l_(374025)
  old_pass = _c_(374027, _n_(374026, "input", lambda: input), 'Now please enter the password again to check: ')
  _l_(374028)
  if _c_(374032, _n_(374029, "check_password", lambda: check_password), _n_(374030, "hashed_password", lambda: hashed_password), _n_(374031, "old_pass", lambda: old_pass)):
    _l_(374039)

    _c_(374034, _n_(374033, "print", lambda: print), 'The passwords match!')
    _l_(374035)
  else:
      _c_(374037, _n_(374036, "print", lambda: print), 'I am sorry but the password does not match')
      _l_(374038)

else:
  _c_(374041, _n_(374040, "print", lambda: print), "(NOT CODED YET)")
  _l_(374042)