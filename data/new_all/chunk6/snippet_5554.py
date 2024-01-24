# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54479475/how-to-fix-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import uuid
  _l_(369207)

except ImportError:
  pass
try:
  import hashlib
  _l_(369209)

except ImportError:
  pass
login_or_signup = _c_(369211, _n_(369210, "input", lambda: input), "would you like to log in? Or signup?: ")
_l_(369212)

if _c_(369214, _n_(369213, "login_or_signup", lambda: login_or_signup), "signup"):
  _l_(369276)

  def hash_password(password):
    _l_(369233)

    # uuid is used to generate a random number
    salt = _a_(369218, _c_(369217, _a_(369216, _n_(369215, "uuid", lambda: uuid), "uuid4")), "hex")
    _l_(369219)
    aux = _c_(369230, _a_(369229, _c_(369228, _a_(369221, _n_(369220, "hashlib", lambda: hashlib), "sha256"), _c_(369224, _a_(369223, _n_(369222, "salt", lambda: salt), "encode")) + _c_(369227, _a_(369226, _n_(369225, "password", lambda: password), "encode"))), "hexdigest")) + ':' + _n_(369231, "salt", lambda: salt)
    _l_(369232)
    return aux

  def check_password(hashed_password, user_password):
    _l_(369251)

    password, salt = _c_(369236, _a_(369235, _n_(369234, "hashed_password", lambda: hashed_password), "split"), ':')
    _l_(369237)
    aux = _n_(369238, "password", lambda: password) == _c_(369249, _a_(369248, _c_(369247, _a_(369240, _n_(369239, "hashlib", lambda: hashlib), "sha256"), _c_(369243, _a_(369242, _n_(369241, "salt", lambda: salt), "encode")) + _c_(369246, _a_(369245, _n_(369244, "user_password", lambda: user_password), "encode"))), "hexdigest"))
    _l_(369250)
    return aux

  new_pass = _c_(369253, _n_(369252, "input", lambda: input), 'Please enter a password: ')
  _l_(369254)
  hashed_password = _c_(369257, _n_(369255, "hash_password", lambda: hash_password), _n_(369256, "new_pass", lambda: new_pass))
  _l_(369258)
  old_pass = _c_(369260, _n_(369259, "input", lambda: input), 'Now please enter the password again to check: ')
  _l_(369261)
  if _c_(369265, _n_(369262, "check_password", lambda: check_password), _n_(369263, "hashed_password", lambda: hashed_password), _n_(369264, "old_pass", lambda: old_pass)):
    _l_(369272)

    _c_(369267, _n_(369266, "print", lambda: print), 'The passwords match!')
    _l_(369268)
  else:
      _c_(369270, _n_(369269, "print", lambda: print), 'I am sorry but the password does not match')
      _l_(369271)

else:
  _c_(369274, _n_(369273, "print", lambda: print), "(NOT CODED YET)")
  _l_(369275)