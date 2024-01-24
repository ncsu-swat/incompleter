# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40901405/yielding-a-typeerror-input-expected-at-most-1-arguments-got-4-this-error-was
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def randomLetters():
    _l_(667002)

    numbers = [_c_(666989, _a_(666988, _n_(666987, "random", lambda: random), "randint"), 0, 25), _c_(666992, _a_(666991, _n_(666990, "random", lambda: random), "randint"), 0, 25)]
    _l_(666993)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _l_(666994)
    letters = [_n_(666995, "alphabet", lambda: alphabet)[_n_(666996, "numbers", lambda: numbers)[0]], _n_(666997, "alphabet", lambda: alphabet)[_n_(666998, "numbers", lambda: numbers)[1]]]
    _l_(666999)
    aux = _n_(667000, "letters", lambda: letters)
    _l_(667001)
    return aux

letters = _c_(667004, _n_(667003, "randomLetters", lambda: randomLetters))
_l_(667005)
_c_(667008, _n_(667006, "print", lambda: print), _n_(667007, "letters", lambda: letters))
_l_(667009)
_c_(667012, _n_(667010, "print", lambda: print), _n_(667011, "letters", lambda: letters)[0])
_l_(667013)
user_input = _c_(667017, _n_(667014, "input", lambda: input), 'Enter a word that begins with', "'" + _n_(667015, "letters", lambda: letters)[0] + "'", 'and ends with', "'" + _n_(667016, "letters", lambda: letters)[1] + "': ")
_l_(667018)
new_user_input = _c_(667021, _a_(667020, _n_(667019, "user_input", lambda: user_input), "lower"))
_l_(667022)

while (_n_(667023, "new_user_input", lambda: new_user_input)[0] != _n_(667024, "letters", lambda: letters)[0]) and (_n_(667025, "new_user_input", lambda: new_user_input)[_c_(667028, _n_(667026, "len", lambda: len), _n_(667027, "new_user_input", lambda: new_user_input)) - 1] != _n_(667029, "letters", lambda: letters)[1]):
    _l_(667038)

    _c_(667031, _n_(667030, "print", lambda: print), 'Invalid input. Try again.')
    _l_(667032)
    new_user_input = _c_(667036, _n_(667033, "input", lambda: input), 'Enter a word that begins with', "'" + _n_(667034, "letters", lambda: letters)[0] + "'", 'and ends with', "'" + _n_(667035, "letters", lambda: letters)[1] + "': ")
    _l_(667037)