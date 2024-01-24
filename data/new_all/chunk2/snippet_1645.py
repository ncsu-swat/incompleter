# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67300476/attribute-error-in-python-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Person:
    _l_(428526)

    def __init__(self, name, age, occupation):
        _l_(428513)

        _n_(428504, "self", lambda: self).name = _n_(428505, "name", lambda: name)
        _l_(428506)
        _n_(428507, "self", lambda: self).age = _n_(428508, "age", lambda: age)
        _l_(428509)
        _n_(428510, "self", lambda: self).occupation = _n_(428511, "occupation", lambda: occupation)
        _l_(428512)
  
    def say_hello(self):
        _l_(428519)

        _c_(428517, _n_(428514, "print", lambda: print), f"Hello, my name is {_a_(428516, _n_(428515, 'self', lambda: self), 'name')}.")
        _l_(428518)
  
    def say_age(self):
        _l_(428525)

        _c_(428523, _n_(428520, "print", lambda: print), f"I am {_a_(428522, _n_(428521, 'self', lambda: self), 'age')} years old.")
        _l_(428524)
class Superhero(_n_(428527, "Person", lambda: Person)):
    _l_(428535)

    def __init__(self, name, age, occupation, secret_identity, nemesis):
        _l_(428534)

        _n_(428528, "self", lambda: self).secret_identity = _n_(428529, "secret_identity", lambda: secret_identity)
        _l_(428530)
        _n_(428531, "self", lambda: self).nemesis = _n_(428532, "nemesis", lambda: nemesis)
        _l_(428533)

hero = _c_(428537, _n_(428536, "Superhero", lambda: Superhero), "Spider-Man", 17, "student", "Peter Parker", "Green Goblin")
_l_(428538)
_c_(428543, _n_(428539, "print", lambda: print), _c_(428542, _a_(428541, _n_(428540, "hero", lambda: hero), "name")))
_l_(428544)