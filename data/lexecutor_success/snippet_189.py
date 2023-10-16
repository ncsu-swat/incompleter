# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/472000/usage-of-slots
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Person:
    _l_(1539577)


    __slots__ = {
        "birthday":
            "A datetime.date object representing the person's birthday.",
        "name":
            "The first and last name.",
        "public_variable":
            None,
        "_private_variable":
            "Description",
    }
    _l_(1539576)


_c_(1539580, _n_(1539578, "help", lambda: help), _n_(1539579, "Person", lambda: Person))
_l_(1539581)
"""
Help on class Person in module __main__:

class Person(builtins.object)
 |  Data descriptors defined here:
 |
 |  birthday
 |      A datetime.date object representing the person's birthday.
 |
 |  name
 |      The first and last name.
 |
 |  public_variable
"""

